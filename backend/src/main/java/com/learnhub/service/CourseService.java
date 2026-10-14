package com.learnhub.service;

import com.learnhub.dto.CourseDetailResponse;
import com.learnhub.dto.CourseSummaryResponse;
import com.learnhub.dto.CreateCourseRequest;
import com.learnhub.dto.PageResponse;
import com.learnhub.dto.UpdateCourseRequest;
import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;
import com.learnhub.entity.Role;
import com.learnhub.entity.User;
import com.learnhub.exception.BadRequestException;
import com.learnhub.exception.ResourceNotFoundException;
import com.learnhub.repository.CourseRepository;
import com.learnhub.repository.LessonRepository;
import com.learnhub.repository.UserRepository;
import com.learnhub.security.UserPrincipal;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

/**
 * Service managing course lifecycle, ownership validation, and catalog queries.
 */
@Service
@Transactional
public class CourseService {

    private final CourseRepository courseRepository;
    private final LessonRepository lessonRepository;
    private final UserRepository userRepository;

    public CourseService(CourseRepository courseRepository,
                         LessonRepository lessonRepository,
                         UserRepository userRepository) {
        this.courseRepository = courseRepository;
        this.lessonRepository = lessonRepository;
        this.userRepository = userRepository;
    }

    /**
     * Creates a new course in DRAFT status. Only Administrators can create courses.
     */
    public CourseDetailResponse createCourse(CreateCourseRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "create");

        User instructor = null;
        if (currentUser.getAuthorities().stream().anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"))) {
            instructor = userRepository.findById(currentUser.getId())
                    .orElseThrow(() -> new ResourceNotFoundException("User", "id", currentUser.getId()));
        }

        Course course = new Course(
                request.getTitle().trim(),
                request.getDescription(),
                request.getCategory().trim(),
                request.getDifficultyLevel() != null ? request.getDifficultyLevel() : DifficultyLevel.BEGINNER,
                request.getLearningObjectives(),
                request.getPrerequisites(),
                request.getEstimatedDuration() != null ? request.getEstimatedDuration() : 60,
                instructor
        );
        course.setStatus(CourseStatus.DRAFT);

        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    /**
     * Assigns an instructor to an existing course. Only Administrators can assign instructors.
     */
    public CourseDetailResponse assignInstructor(Long courseId, Long instructorId, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "assign instructor to");

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        User instructor = userRepository.findById(instructorId)
                .orElseThrow(() -> new ResourceNotFoundException("User", "id", instructorId));

        if (instructor.getRole() != Role.ROLE_INSTRUCTOR) {
            throw new BadRequestException("Assigned user must have INSTRUCTOR role");
        }

        course.setInstructor(instructor);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    /**
     * Returns courses assigned to the authenticated instructor.
     */
    @Transactional(readOnly = true)
    public List<CourseSummaryResponse> getMyCourses(UserPrincipal currentUser) {
        if (currentUser == null) {
            throw new AccessDeniedException("Authentication required to view assigned courses");
        }
        return courseRepository.findByInstructorIdOrderByCreatedAtDesc(currentUser.getId()).stream()
                .map(CourseSummaryResponse::from)
                .collect(Collectors.toList());
    }

    /**
     * Returns course details subject to access control.
     * Published courses are publicly readable; unpublished courses require assigned instructor or admin.
     */
    @Transactional(readOnly = true)
    public CourseDetailResponse getCourseById(Long id, UserPrincipal currentUser) {
        Course course = courseRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", id));

        if (course.getStatus() == CourseStatus.PUBLISHED) {
            return CourseDetailResponse.from(course);
        }

        if (currentUser == null) {
            throw new AccessDeniedException("Authentication required to view non-published courses");
        }

        boolean isAssignedInstructor = course.getInstructor() != null &&
                course.getInstructor().getId().equals(currentUser.getId());
        boolean isAdmin = currentUser.getAuthorities().stream()
                .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));

        if (!isAssignedInstructor && !isAdmin) {
            throw new AccessDeniedException("You do not have permission to view this course");
        }

        return CourseDetailResponse.from(course);
    }

    /**
     * Updates an editable course draft. Only Administrators can update courses.
     */
    public CourseDetailResponse updateCourse(Long id, UpdateCourseRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "edit");

        Course course = courseRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", id));

        if (course.getStatus() == CourseStatus.ARCHIVED) {
            throw new BadRequestException("Archived courses cannot be modified");
        }

        course.setTitle(request.getTitle().trim());
        course.setDescription(request.getDescription());
        course.setCategory(request.getCategory().trim());
        course.setDifficultyLevel(request.getDifficultyLevel());
        course.setLearningObjectives(request.getLearningObjectives());
        course.setPrerequisites(request.getPrerequisites());
        if (request.getEstimatedDuration() != null) {
            course.setEstimatedDuration(request.getEstimatedDuration());
        }

        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    /**
     * Deletes an eligible draft course. Only Administrators can delete courses.
     */
    public void deleteCourse(Long id, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "delete");

        Course course = courseRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", id));

        if (course.getStatus() != CourseStatus.DRAFT) {
            throw new BadRequestException("Only draft courses can be deleted");
        }

        courseRepository.delete(course);
    }

    /**
     * Searches and lists published courses for the public catalog.
     */
    @Transactional(readOnly = true)
    public PageResponse<CourseSummaryResponse> searchPublishedCourses(
            String search, String category, DifficultyLevel difficulty, Pageable pageable) {

        String queryParam = (search != null && !search.trim().isEmpty()) ? search.trim() : null;
        String categoryParam = (category != null && !category.trim().isEmpty()) ? category.trim() : null;

        Page<Course> page = courseRepository.searchPublishedCourses(queryParam, categoryParam, difficulty, pageable);
        List<CourseSummaryResponse> dtoList = page.getContent().stream()
                .map(CourseSummaryResponse::from)
                .collect(Collectors.toList());

        return new PageResponse<>(
                dtoList,
                page.getNumber(),
                page.getSize(),
                page.getTotalElements(),
                page.getTotalPages(),
                page.isLast()
        );
    }

    /**
     * Publishes a course. Only Administrators can publish courses.
     */
    public CourseDetailResponse publishCourse(Long id, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "publish");

        Course course = courseRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", id));

        course.setStatus(CourseStatus.PUBLISHED);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    /**
     * Unpublishes a course back to DRAFT. Only Administrators can unpublish courses.
     */
    public CourseDetailResponse unpublishCourse(Long id, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "unpublish");

        Course course = courseRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", id));

        course.setStatus(CourseStatus.DRAFT);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    /**
     * Archives a course. Only Administrators can archive courses.
     */
    public CourseDetailResponse archiveCourse(Long id, UserPrincipal currentUser) {
        verifyAdmin(currentUser, "archive");

        Course course = courseRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", id));

        course.setStatus(CourseStatus.ARCHIVED);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    /**
     * Verifies that the current user has administrator privileges.
     */
    public void verifyAdmin(UserPrincipal currentUser, String action) {
        if (currentUser == null) {
            throw new AccessDeniedException("Authentication required to " + action + " course");
        }

        boolean isAdmin = currentUser.getAuthorities().stream()
                .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));

        if (!isAdmin) {
            throw new AccessDeniedException("Only administrators have permission to " + action + " courses");
        }
    }
}
