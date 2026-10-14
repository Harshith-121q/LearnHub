package com.learnhub.service;

import com.learnhub.dto.EnrollmentResponse;
import com.learnhub.dto.ModuleResponse;
import com.learnhub.dto.StudentLearningCourseResponse;
import com.learnhub.entity.ActivityType;
import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.Enrollment;
import com.learnhub.entity.LearningActivity;
import com.learnhub.entity.Lesson;
import com.learnhub.entity.LessonProgress;
import com.learnhub.entity.Module;
import com.learnhub.entity.User;
import com.learnhub.exception.BadRequestException;
import com.learnhub.exception.ResourceNotFoundException;
import com.learnhub.repository.CourseRepository;
import com.learnhub.repository.EnrollmentRepository;
import com.learnhub.repository.LearningActivityRepository;
import com.learnhub.repository.LessonProgressRepository;
import com.learnhub.repository.LessonRepository;
import com.learnhub.repository.UserRepository;
import com.learnhub.security.UserPrincipal;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Service managing student course enrollment, step-by-step lesson navigation, and persistent progress tracking.
 */
@Service
@Transactional
public class StudentLearningService {

    private final EnrollmentRepository enrollmentRepository;
    private final LessonProgressRepository lessonProgressRepository;
    private final LearningActivityRepository learningActivityRepository;
    private final CourseRepository courseRepository;
    private final LessonRepository lessonRepository;
    private final UserRepository userRepository;

    public StudentLearningService(EnrollmentRepository enrollmentRepository,
                                  LessonProgressRepository lessonProgressRepository,
                                  LearningActivityRepository learningActivityRepository,
                                  CourseRepository courseRepository,
                                  LessonRepository lessonRepository,
                                  UserRepository userRepository) {
        this.enrollmentRepository = enrollmentRepository;
        this.lessonProgressRepository = lessonProgressRepository;
        this.learningActivityRepository = learningActivityRepository;
        this.courseRepository = courseRepository;
        this.lessonRepository = lessonRepository;
        this.userRepository = userRepository;
    }

    private User getAuthenticatedStudent(UserPrincipal currentUser) {
        if (currentUser == null) {
            throw new AccessDeniedException("Authentication required to access student workspace");
        }
        return userRepository.findById(currentUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("User", "id", currentUser.getId()));
    }

    /**
     * Enrolls the student in a published course with duplicate protection.
     */
    public EnrollmentResponse enroll(Long courseId, UserPrincipal currentUser) {
        User student = getAuthenticatedStudent(currentUser);

        Course course = courseRepository.findById(courseId)
                .orElseThrow(() -> new ResourceNotFoundException("Course", "id", courseId));

        if (course.getStatus() != CourseStatus.PUBLISHED) {
            throw new BadRequestException("Only published courses are open for enrollment");
        }

        if (enrollmentRepository.existsByStudentIdAndCourseId(student.getId(), course.getId())) {
            throw new BadRequestException("You are already enrolled in this course");
        }

        Enrollment enrollment = new Enrollment(student, course);
        long totalLessons = lessonRepository.countTotalLessonsByCourseId(course.getId());
        enrollment.setTotalLessonsCount((int) totalLessons);
        enrollment.setCompletedLessonsCount(0);
        enrollment.setProgressPercentage(0.0);

        Enrollment saved = enrollmentRepository.save(enrollment);

        // Record activity
        learningActivityRepository.save(new LearningActivity(
                student,
                course,
                null,
                ActivityType.COURSE_ENROLLED,
                "Enrolled in course " + course.getTitle()
        ));

        return EnrollmentResponse.from(saved);
    }

    /**
     * Lists courses the student is currently enrolled in.
     */
    @Transactional(readOnly = true)
    public List<EnrollmentResponse> getMyEnrollments(UserPrincipal currentUser) {
        User student = getAuthenticatedStudent(currentUser);
        return enrollmentRepository.findByStudentIdOrderByEnrolledAtDesc(student.getId()).stream()
                .map(EnrollmentResponse::from)
                .collect(Collectors.toList());
    }

    /**
     * Checks if the student is enrolled in a specific course.
     */
    @Transactional(readOnly = true)
    public boolean isEnrolled(Long courseId, UserPrincipal currentUser) {
        if (currentUser == null) return false;
        return enrollmentRepository.existsByStudentIdAndCourseId(currentUser.getId(), courseId);
    }

    /**
     * Retrieves the complete learning course structure, ordered modules/lessons, and progress map for an enrolled student.
     */
    @Transactional(readOnly = true)
    public StudentLearningCourseResponse getCourseLearningContent(Long courseId, UserPrincipal currentUser) {
        User student = getAuthenticatedStudent(currentUser);

        Enrollment enrollment = enrollmentRepository.findByStudentIdAndCourseId(student.getId(), courseId)
                .orElseThrow(() -> new AccessDeniedException("You must be enrolled in this course to access its learning content"));

        Course course = enrollment.getCourse();

        // Get completed lesson IDs
        List<LessonProgress> progresses = lessonProgressRepository.findByEnrollmentIdAndCompletedTrue(enrollment.getId());
        Set<Long> completedIds = progresses.stream()
                .map(p -> p.getLesson().getId())
                .collect(Collectors.toSet());

        // Build modules in sequence order
        List<ModuleResponse> moduleResponses = course.getModules().stream()
                .sorted(Comparator.comparing(Module::getSequenceOrder))
                .map(ModuleResponse::from)
                .collect(Collectors.toList());

        // Find next incomplete lesson for resumption
        Long resumeLessonId = null;
        outer:
        for (ModuleResponse m : moduleResponses) {
            for (var l : m.getLessons()) {
                if (!completedIds.contains(l.getId())) {
                    resumeLessonId = l.getId();
                    break outer;
                }
            }
        }

        // If all completed or none incomplete, default to first lesson
        if (resumeLessonId == null && !moduleResponses.isEmpty()) {
            var firstMod = moduleResponses.get(0);
            if (!firstMod.getLessons().isEmpty()) {
                resumeLessonId = firstMod.getLessons().get(0).getId();
            }
        }

        StudentLearningCourseResponse res = new StudentLearningCourseResponse();
        res.setEnrollmentId(enrollment.getId());
        res.setCourseId(course.getId());
        res.setTitle(course.getTitle());
        res.setDescription(course.getDescription());
        res.setCategory(course.getCategory());
        res.setDifficultyLevel(course.getDifficultyLevel());
        res.setEstimatedDuration(course.getEstimatedDuration());
        res.setModules(moduleResponses);
        res.setCompletedLessonIds(completedIds);
        res.setProgressPercentage(enrollment.getProgressPercentage());
        res.setCompletedLessonsCount(enrollment.getCompletedLessonsCount());
        res.setTotalLessonsCount(enrollment.getTotalLessonsCount());
        res.setIsCompleted(enrollment.getCompleted());
        res.setResumeLessonId(resumeLessonId);

        return res;
    }

    /**
     * Marks an individual lesson as completed and updates aggregate enrollment progress.
     */
    public EnrollmentResponse markLessonComplete(Long lessonId, UserPrincipal currentUser) {
        User student = getAuthenticatedStudent(currentUser);

        Lesson lesson = lessonRepository.findById(lessonId)
                .orElseThrow(() -> new ResourceNotFoundException("Lesson", "id", lessonId));

        Course course = lesson.getModule().getCourse();

        Enrollment enrollment = enrollmentRepository.findByStudentIdAndCourseId(student.getId(), course.getId())
                .orElseThrow(() -> new AccessDeniedException("You are not enrolled in the course for this lesson"));

        LessonProgress progress = lessonProgressRepository.findByEnrollmentIdAndLessonId(enrollment.getId(), lesson.getId())
                .orElseGet(() -> new LessonProgress(enrollment, lesson, false));

        progress.setCompleted(true);
        lessonProgressRepository.save(progress);

        // Recalculate progress
        long completedCount = lessonProgressRepository.countByEnrollmentIdAndCompletedTrue(enrollment.getId());
        long totalLessons = lessonRepository.countTotalLessonsByCourseId(course.getId());

        enrollment.recalculateProgress((int) completedCount, (int) totalLessons);
        Enrollment savedEnrollment = enrollmentRepository.save(enrollment);

        // Record activity
        learningActivityRepository.save(new LearningActivity(
                student,
                course,
                lesson,
                ActivityType.LESSON_COMPLETED,
                "Completed lesson '" + lesson.getTitle() + "'"
        ));

        if (Boolean.TRUE.equals(savedEnrollment.getCompleted())) {
            learningActivityRepository.save(new LearningActivity(
                    student,
                    course,
                    null,
                    ActivityType.COURSE_COMPLETED,
                    "Finished all modules and achieved 100% completion in " + course.getTitle()
            ));
        }

        return EnrollmentResponse.from(savedEnrollment);
    }

    /**
     * Marks an individual lesson as incomplete and recalculates course progress.
     */
    public EnrollmentResponse markLessonIncomplete(Long lessonId, UserPrincipal currentUser) {
        User student = getAuthenticatedStudent(currentUser);

        Lesson lesson = lessonRepository.findById(lessonId)
                .orElseThrow(() -> new ResourceNotFoundException("Lesson", "id", lessonId));

        Course course = lesson.getModule().getCourse();

        Enrollment enrollment = enrollmentRepository.findByStudentIdAndCourseId(student.getId(), course.getId())
                .orElseThrow(() -> new AccessDeniedException("You are not enrolled in the course for this lesson"));

        LessonProgress progress = lessonProgressRepository.findByEnrollmentIdAndLessonId(enrollment.getId(), lesson.getId())
                .orElseGet(() -> new LessonProgress(enrollment, lesson, false));

        progress.setCompleted(false);
        lessonProgressRepository.save(progress);

        long completedCount = lessonProgressRepository.countByEnrollmentIdAndCompletedTrue(enrollment.getId());
        long totalLessons = lessonRepository.countTotalLessonsByCourseId(course.getId());

        enrollment.recalculateProgress((int) completedCount, (int) totalLessons);
        Enrollment savedEnrollment = enrollmentRepository.save(enrollment);

        learningActivityRepository.save(new LearningActivity(
                student,
                course,
                lesson,
                ActivityType.LESSON_UNCOMPLETED,
                "Marked lesson '" + lesson.getTitle() + "' as incomplete"
        ));

        return EnrollmentResponse.from(savedEnrollment);
    }

    /**
     * Records lesson opened activity and updates last accessed timestamp.
     */
    public void recordLessonOpened(Long lessonId, UserPrincipal currentUser) {
        User student = getAuthenticatedStudent(currentUser);

        Lesson lesson = lessonRepository.findById(lessonId)
                .orElseThrow(() -> new ResourceNotFoundException("Lesson", "id", lessonId));

        Course course = lesson.getModule().getCourse();

        Enrollment enrollment = enrollmentRepository.findByStudentIdAndCourseId(student.getId(), course.getId())
                .orElse(null);

        if (enrollment != null) {
            enrollment.setLastAccessedAt(java.time.LocalDateTime.now());
            enrollmentRepository.save(enrollment);

            learningActivityRepository.save(new LearningActivity(
                    student,
                    course,
                    lesson,
                    ActivityType.LESSON_OPENED,
                    "Opened lesson '" + lesson.getTitle() + "'"
            ));
        }
    }
}
