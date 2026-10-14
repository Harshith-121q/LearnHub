package com.learnhub.service;

import com.learnhub.dto.AdminStatsResponse;
import com.learnhub.dto.CourseDetailResponse;
import com.learnhub.dto.CourseSummaryResponse;
import com.learnhub.dto.CreateCourseRequest;
import com.learnhub.dto.CreateLessonRequest;
import com.learnhub.dto.CreateModuleRequest;
import com.learnhub.dto.LessonResponse;
import com.learnhub.dto.ModuleResponse;
import com.learnhub.dto.UpdateCourseRequest;
import com.learnhub.dto.UpdateLessonRequest;
import com.learnhub.dto.UpdateModuleRequest;
import com.learnhub.dto.UserSummaryResponse;
import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;
import com.learnhub.entity.Lesson;
import com.learnhub.entity.Module;
import com.learnhub.entity.Role;
import com.learnhub.entity.User;
import com.learnhub.exception.BadRequestException;
import com.learnhub.exception.ResourceNotFoundException;
import com.learnhub.repository.CourseRepository;
import com.learnhub.repository.EnrollmentRepository;
import com.learnhub.repository.LessonRepository;
import com.learnhub.repository.ModuleRepository;
import com.learnhub.repository.UserRepository;
import com.learnhub.security.UserPrincipal;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

/**
 * Service managing administrative operations, course authoring, curriculum structure, and instructor assignments.
 */
@Service
@Transactional
public class AdminService {

    private final CourseRepository courseRepository;
    private final ModuleRepository moduleRepository;
    private final LessonRepository lessonRepository;
    private final UserRepository userRepository;
    private final EnrollmentRepository enrollmentRepository;

    public AdminService(CourseRepository courseRepository,
                        ModuleRepository moduleRepository,
                        LessonRepository lessonRepository,
                        UserRepository userRepository,
                        EnrollmentRepository enrollmentRepository) {
        this.courseRepository = courseRepository;
        this.moduleRepository = moduleRepository;
        this.lessonRepository = lessonRepository;
        this.userRepository = userRepository;
        this.enrollmentRepository = enrollmentRepository;
    }

    private void verifyAdmin(UserPrincipal currentUser) {
        if (currentUser == null || currentUser.getAuthorities().stream().noneMatch(a -> a.getAuthority().equals("ROLE_ADMIN"))) {
            throw new AccessDeniedException("Administrative privileges required");
        }
    }

    @Transactional(readOnly = true)
    public AdminStatsResponse getStats(UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        long totalCourses = courseRepository.count();
        long publishedCourses = courseRepository.countByStatus(CourseStatus.PUBLISHED);
        long draftCourses = courseRepository.countByStatus(CourseStatus.DRAFT);
        long archivedCourses = courseRepository.countByStatus(CourseStatus.ARCHIVED);
        long totalStudents = userRepository.countByRole(Role.ROLE_STUDENT);
        long totalInstructors = userRepository.countByRole(Role.ROLE_INSTRUCTOR);
        long totalEnrollments = enrollmentRepository.count();

        return new AdminStatsResponse(
                totalCourses,
                publishedCourses,
                draftCourses,
                archivedCourses,
                totalStudents,
                totalInstructors,
                totalEnrollments
        );
    }

    @Transactional(readOnly = true)
    public List<CourseSummaryResponse> getAllCourses(UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        return courseRepository.findAllByOrderByCreatedAtDesc().stream()
                .map(c -> {
                    CourseSummaryResponse dto = CourseSummaryResponse.from(c);
                    dto.setEnrolledCount(enrollmentRepository.countByCourseId(c.getId()));
                    return dto;
                })
                .collect(Collectors.toList());
    }

    public CourseDetailResponse createCourse(CreateCourseRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        User creator = userRepository.findById(currentUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("User", "id", currentUser.getId()));

        Course course = new Course(
                request.getTitle().trim(),
                request.getDescription(),
                request.getCategory().trim(),
                request.getDifficultyLevel() != null ? request.getDifficultyLevel() : DifficultyLevel.BEGINNER,
                request.getLearningObjectives(),
                request.getPrerequisites(),
                request.getEstimatedDuration() != null ? request.getEstimatedDuration() : 60,
                creator
        );
        course.setStatus(CourseStatus.DRAFT);

        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    public CourseDetailResponse updateCourse(Long courseId, UpdateCourseRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

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
        CourseDetailResponse dto = CourseDetailResponse.from(saved);
        dto.setEnrolledCount(enrollmentRepository.countByCourseId(saved.getId()));
        return dto;
    }

    public void deleteCourse(Long courseId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        long enrollmentCount = enrollmentRepository.countByCourseId(courseId);
        if (enrollmentCount > 0) {
            throw new BadRequestException("Cannot delete course with active student enrollments. Archive it instead.");
        }

        courseRepository.delete(course);
    }

    public CourseDetailResponse publishCourse(Long courseId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        course.setStatus(CourseStatus.PUBLISHED);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    public CourseDetailResponse unpublishCourse(Long courseId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        course.setStatus(CourseStatus.DRAFT);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    public CourseDetailResponse archiveCourse(Long courseId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        course.setStatus(CourseStatus.ARCHIVED);
        Course saved = courseRepository.save(course);
        return CourseDetailResponse.from(saved);
    }

    @Transactional(readOnly = true)
    public List<UserSummaryResponse> getAvailableInstructors(UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        return userRepository.findByRole(Role.ROLE_INSTRUCTOR).stream()
                .map(UserSummaryResponse::fromEntity)
                .collect(Collectors.toList());
    }

    public CourseDetailResponse assignInstructor(Long courseId, Long instructorId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        User instructor = userRepository.findById(instructorId)
                .orElseThrow(() -> new ResourceNotFoundException("Instructor", "id", instructorId));

        if (instructor.getRole() != Role.ROLE_INSTRUCTOR) {
            throw new BadRequestException("Selected user is not an instructor");
        }

        course.addInstructor(instructor);
        Course saved = courseRepository.save(course);
        CourseDetailResponse dto = CourseDetailResponse.from(saved);
        dto.setEnrolledCount(enrollmentRepository.countByCourseId(saved.getId()));
        return dto;
    }

    public CourseDetailResponse removeInstructor(Long courseId, Long instructorId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        User instructor = userRepository.findById(instructorId)
                .orElseThrow(() -> new ResourceNotFoundException("Instructor", "id", instructorId));

        course.removeInstructor(instructor);
        Course saved = courseRepository.save(course);
        CourseDetailResponse dto = CourseDetailResponse.from(saved);
        dto.setEnrolledCount(enrollmentRepository.countByCourseId(saved.getId()));
        return dto;
    }

    // Module Management
    public ModuleResponse addModule(Long courseId, CreateModuleRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        int nextOrder = moduleRepository.findMaxSequenceOrderByCourseId(courseId) + 1;
        int order = request.getSequenceOrder() != null ? request.getSequenceOrder() : nextOrder;

        Module module = new Module(request.getTitle().trim(), request.getDescription(), order, course);
        Module saved = moduleRepository.save(module);
        return ModuleResponse.from(saved);
    }

    public ModuleResponse updateModule(Long moduleId, UpdateModuleRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Module module = moduleRepository.findById(moduleId)
                .orElseThrow(() -> new ResourceNotFoundException("Module", "id", moduleId));

        module.setTitle(request.getTitle().trim());
        module.setDescription(request.getDescription());
        if (request.getSequenceOrder() != null) {
            module.setSequenceOrder(request.getSequenceOrder());
        }

        Module saved = moduleRepository.save(module);
        return ModuleResponse.from(saved);
    }

    public void deleteModule(Long moduleId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Module module = moduleRepository.findById(moduleId)
                .orElseThrow(() -> new ResourceNotFoundException("Module", "id", moduleId));

        moduleRepository.delete(module);
    }

    public List<ModuleResponse> reorderModules(Long courseId, List<Long> moduleIds, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        List<Module> modules = moduleRepository.findByCourseIdOrderBySequenceOrderAsc(courseId);
        for (int i = 0; i < moduleIds.size(); i++) {
            Long mId = moduleIds.get(i);
            for (Module m : modules) {
                if (m.getId().equals(mId)) {
                    m.setSequenceOrder(i + 1);
                    break;
                }
            }
        }
        moduleRepository.saveAll(modules);
        return moduleRepository.findByCourseIdOrderBySequenceOrderAsc(courseId).stream()
                .map(ModuleResponse::from)
                .collect(Collectors.toList());
    }

    // Lesson Management
    public LessonResponse addLesson(Long moduleId, CreateLessonRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Module module = moduleRepository.findById(moduleId)
                .orElseThrow(() -> new ResourceNotFoundException("Module", "id", moduleId));

        int nextOrder = lessonRepository.findMaxSequenceOrderByModuleId(moduleId) + 1;
        int order = request.getSequenceOrder() != null ? request.getSequenceOrder() : nextOrder;

        Lesson lesson = new Lesson(
                request.getTitle().trim(),
                request.getContent(),
                request.getCodeExample(),
                request.getVideoUrl(),
                request.getDurationMinutes() != null ? request.getDurationMinutes() : 15,
                order,
                module
        );

        Lesson saved = lessonRepository.save(lesson);
        return LessonResponse.from(saved);
    }

    public LessonResponse updateLesson(Long lessonId, UpdateLessonRequest request, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Lesson lesson = lessonRepository.findById(lessonId)
                .orElseThrow(() -> new ResourceNotFoundException("Lesson", "id", lessonId));

        lesson.setTitle(request.getTitle().trim());
        lesson.setContent(request.getContent());
        lesson.setCodeExample(request.getCodeExample());
        lesson.setVideoUrl(request.getVideoUrl());
        if (request.getDurationMinutes() != null) {
            lesson.setDurationMinutes(request.getDurationMinutes());
        }
        if (request.getSequenceOrder() != null) {
            lesson.setSequenceOrder(request.getSequenceOrder());
        }

        Lesson saved = lessonRepository.save(lesson);
        return LessonResponse.from(saved);
    }

    public void deleteLesson(Long lessonId, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        Lesson lesson = lessonRepository.findById(lessonId)
                .orElseThrow(() -> new ResourceNotFoundException("Lesson", "id", lessonId));

        lessonRepository.delete(lesson);
    }

    public List<LessonResponse> reorderLessons(Long moduleId, List<Long> lessonIds, UserPrincipal currentUser) {
        verifyAdmin(currentUser);

        List<Lesson> lessons = lessonRepository.findByModuleIdOrderBySequenceOrderAsc(moduleId);
        for (int i = 0; i < lessonIds.size(); i++) {
            Long lId = lessonIds.get(i);
            for (Lesson l : lessons) {
                if (l.getId().equals(lId)) {
                    l.setSequenceOrder(i + 1);
                    break;
                }
            }
        }
        lessonRepository.saveAll(lessons);
        return lessonRepository.findByModuleIdOrderBySequenceOrderAsc(moduleId).stream()
                .map(LessonResponse::from)
                .collect(Collectors.toList());
    }
}
