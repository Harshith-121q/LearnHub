package com.learnhub.service;

import com.learnhub.dto.CourseDetailResponse;
import com.learnhub.dto.EnrolledStudentResponse;
import com.learnhub.dto.InstructorCourseSummaryResponse;
import com.learnhub.dto.LearningActivityResponse;
import com.learnhub.dto.StudentProgressDetailResponse;
import com.learnhub.entity.Course;
import com.learnhub.entity.Enrollment;
import com.learnhub.entity.LessonProgress;
import com.learnhub.entity.User;
import com.learnhub.exception.ResourceNotFoundException;
import com.learnhub.repository.CourseRepository;
import com.learnhub.repository.EnrollmentRepository;
import com.learnhub.repository.LearningActivityRepository;
import com.learnhub.repository.LessonProgressRepository;
import com.learnhub.repository.LessonRepository;
import com.learnhub.security.UserPrincipal;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Service managing instructor monitoring of assigned courses, enrolled students, and student learning progress.
 */
@Service
@Transactional(readOnly = true)
public class InstructorService {

    private final CourseRepository courseRepository;
    private final EnrollmentRepository enrollmentRepository;
    private final LessonProgressRepository lessonProgressRepository;
    private final LearningActivityRepository learningActivityRepository;
    private final LessonRepository lessonRepository;

    public InstructorService(CourseRepository courseRepository,
                             EnrollmentRepository enrollmentRepository,
                             LessonProgressRepository lessonProgressRepository,
                             LearningActivityRepository learningActivityRepository,
                             LessonRepository lessonRepository) {
        this.courseRepository = courseRepository;
        this.enrollmentRepository = enrollmentRepository;
        this.lessonProgressRepository = lessonProgressRepository;
        this.learningActivityRepository = learningActivityRepository;
        this.lessonRepository = lessonRepository;
    }

    private void verifyInstructorAssignment(Course course, UserPrincipal currentUser) {
        if (currentUser == null) {
            throw new AccessDeniedException("Authentication required to access instructor portal");
        }

        boolean isAdmin = currentUser.getAuthorities().stream()
                .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));

        if (isAdmin) return;

        boolean isAssigned = course.hasInstructor(currentUser.getId());
        if (!isAssigned) {
            throw new AccessDeniedException("Access denied: You are not assigned to monitor this course");
        }
    }

    /**
     * Lists courses assigned to the authenticated instructor with real-time participation metrics.
     */
    public List<InstructorCourseSummaryResponse> getAssignedCourses(UserPrincipal currentUser) {
        if (currentUser == null) {
            throw new AccessDeniedException("Authentication required");
        }

        List<Course> courses = courseRepository.findAssignedCoursesForInstructor(currentUser.getId());

        return courses.stream().map(c -> {
            InstructorCourseSummaryResponse dto = new InstructorCourseSummaryResponse();
            dto.setId(c.getId());
            dto.setTitle(c.getTitle());
            dto.setDescription(c.getDescription());
            dto.setCategory(c.getCategory());
            dto.setDifficultyLevel(c.getDifficultyLevel());
            dto.setStatus(c.getStatus());

            long totalStudents = enrollmentRepository.countByCourseId(c.getId());
            long started = enrollmentRepository.countByCourseIdAndCompletedLessonsCountGreaterThan(c.getId(), 0);
            long completed = enrollmentRepository.countByCourseIdAndCompletedTrue(c.getId());
            Double avgProgress = enrollmentRepository.getAverageProgressByCourseId(c.getId());

            dto.setTotalEnrolledStudents(totalStudents);
            dto.setStudentsStarted(started);
            dto.setStudentsCompleted(completed);
            dto.setAverageCompletionPercentage(avgProgress != null ? Math.round(avgProgress * 10.0) / 10.0 : 0.0);
            dto.setTotalModules(c.getModules() != null ? c.getModules().size() : 0);
            dto.setTotalLessons(lessonRepository.countTotalLessonsByCourseId(c.getId()));

            return dto;
        }).collect(Collectors.toList());
    }

    /**
     * Reads course curriculum and content for an assigned course.
     */
    public CourseDetailResponse getAssignedCourseContent(Long courseId, UserPrincipal currentUser) {
        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        verifyInstructorAssignment(course, currentUser);

        CourseDetailResponse dto = CourseDetailResponse.from(course);
        dto.setEnrolledCount(enrollmentRepository.countByCourseId(courseId));
        return dto;
    }

    /**
     * Lists students enrolled in the assigned course with their progress percentages and last activities.
     */
    public List<EnrolledStudentResponse> getEnrolledStudents(Long courseId, String filter, UserPrincipal currentUser) {
        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        verifyInstructorAssignment(course, currentUser);

        List<Enrollment> enrollments = enrollmentRepository.findByCourseIdOrderByEnrolledAtDesc(courseId);

        // Filter: all, in-progress, completed
        if ("completed".equalsIgnoreCase(filter)) {
            enrollments = enrollments.stream().filter(Enrollment::getCompleted).collect(Collectors.toList());
        } else if ("in-progress".equalsIgnoreCase(filter)) {
            enrollments = enrollments.stream().filter(e -> !e.getCompleted()).collect(Collectors.toList());
        }

        return enrollments.stream().map(e -> {
            User student = e.getStudent();
            EnrolledStudentResponse dto = new EnrolledStudentResponse();
            dto.setStudentId(student.getId());
            dto.setStudentName(student.getFullName());
            dto.setStudentUsername(student.getUsername());
            dto.setStudentEmail(student.getEmail());
            dto.setEnrolledAt(e.getEnrolledAt());
            dto.setCompletedLessonsCount(e.getCompletedLessonsCount());
            dto.setTotalLessonsCount(e.getTotalLessonsCount());
            dto.setProgressPercentage(e.getProgressPercentage());
            dto.setCompleted(Boolean.TRUE.equals(e.getCompleted()));

            learningActivityRepository.findFirstByStudentIdAndCourseIdOrderByTimestampDesc(student.getId(), courseId)
                    .ifPresent(activity -> {
                        dto.setLastActivityDate(activity.getTimestamp());
                        dto.setLastActivityDescription(activity.getDescription());
                    });

            return dto;
        }).collect(Collectors.toList());
    }

    /**
     * Retrieves detailed progress and activity audit trail for an individual student in an assigned course.
     */
    public StudentProgressDetailResponse getStudentProgressDetail(Long courseId, Long studentId, UserPrincipal currentUser) {
        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        verifyInstructorAssignment(course, currentUser);

        Enrollment enrollment = enrollmentRepository.findByStudentIdAndCourseId(studentId, courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Enrollment", "studentId", studentId));

        User student = enrollment.getStudent();

        List<LessonProgress> progresses = lessonProgressRepository.findByEnrollmentIdAndCompletedTrue(enrollment.getId());
        Set<Long> completedIds = progresses.stream().map(p -> p.getLesson().getId()).collect(Collectors.toSet());

        List<LearningActivityResponse> recentActivities = learningActivityRepository
                .findByStudentIdAndCourseIdOrderByTimestampDesc(studentId, courseId).stream()
                .limit(20)
                .map(LearningActivityResponse::from)
                .collect(Collectors.toList());

        StudentProgressDetailResponse dto = new StudentProgressDetailResponse();
        dto.setStudentId(student.getId());
        dto.setStudentName(student.getFullName());
        dto.setStudentUsername(student.getUsername());
        dto.setStudentEmail(student.getEmail());
        dto.setCourseId(course.getId());
        dto.setCourseTitle(course.getTitle());
        dto.setEnrolledAt(enrollment.getEnrolledAt());
        dto.setProgressPercentage(enrollment.getProgressPercentage());
        dto.setCompletedLessonsCount(enrollment.getCompletedLessonsCount());
        dto.setTotalLessonsCount(enrollment.getTotalLessonsCount());
        dto.setCompleted(Boolean.TRUE.equals(enrollment.getCompleted()));
        dto.setCompletedAt(enrollment.getCompletedAt());
        dto.setCompletedLessonIds(completedIds);
        dto.setRecentActivities(recentActivities);

        return dto;
    }
}
