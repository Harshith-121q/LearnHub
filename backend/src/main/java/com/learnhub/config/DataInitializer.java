package com.learnhub.config;

import com.learnhub.entity.ActivityType;
import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;
import com.learnhub.entity.Enrollment;
import com.learnhub.entity.LearningActivity;
import com.learnhub.entity.Lesson;
import com.learnhub.entity.LessonProgress;
import com.learnhub.entity.Module;
import com.learnhub.entity.Role;
import com.learnhub.entity.User;
import com.learnhub.repository.CourseRepository;
import com.learnhub.repository.EnrollmentRepository;
import com.learnhub.repository.LearningActivityRepository;
import com.learnhub.repository.LessonProgressRepository;
import com.learnhub.repository.LessonRepository;
import com.learnhub.repository.ModuleRepository;
import com.learnhub.repository.UserRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

/**
 * Initializes baseline administrative, instructor, and student accounts along with structured Java &amp; Python courses.
 */
@Component
public class DataInitializer implements CommandLineRunner {

    private static final Logger log = LoggerFactory.getLogger(DataInitializer.class);

    private final UserRepository userRepository;
    private final CourseRepository courseRepository;
    private final ModuleRepository moduleRepository;
    private final LessonRepository lessonRepository;
    private final EnrollmentRepository enrollmentRepository;
    private final LessonProgressRepository lessonProgressRepository;
    private final LearningActivityRepository learningActivityRepository;
    private final PasswordEncoder passwordEncoder;
    private final CurriculumSeeder curriculumSeeder;

    public DataInitializer(UserRepository userRepository,
                           CourseRepository courseRepository,
                           ModuleRepository moduleRepository,
                           LessonRepository lessonRepository,
                           EnrollmentRepository enrollmentRepository,
                           LessonProgressRepository lessonProgressRepository,
                           LearningActivityRepository learningActivityRepository,
                           PasswordEncoder passwordEncoder,
                           CurriculumSeeder curriculumSeeder) {
        this.userRepository = userRepository;
        this.courseRepository = courseRepository;
        this.moduleRepository = moduleRepository;
        this.lessonRepository = lessonRepository;
        this.enrollmentRepository = enrollmentRepository;
        this.lessonProgressRepository = lessonProgressRepository;
        this.learningActivityRepository = learningActivityRepository;
        this.passwordEncoder = passwordEncoder;
        this.curriculumSeeder = curriculumSeeder;
    }

    @Override
    @Transactional
    public void run(String... args) {
        log.info("Initializing LearnHub baseline users and curricula...");

        // 1. Seed Core Accounts
        User admin = userRepository.findByUsername("admin").orElseGet(() -> {
            User u = new User(
                    "admin",
                    "admin@learnhub.com",
                    passwordEncoder.encode("Admin@123"),
                    "System Administrator",
                    Role.ROLE_ADMIN
            );
            u.setBio("Platform root administrator overseeing curriculum and instructor assignments.");
            return userRepository.save(u);
        });

        User instructor = userRepository.findByUsername("instructor_sarah").orElseGet(() -> {
            User u = new User(
                    "instructor_sarah",
                    "sarah@learnhub.com",
                    passwordEncoder.encode("Password123"),
                    "Sarah Connor",
                    Role.ROLE_INSTRUCTOR
            );
            u.setBio("Senior Software Engineer & Lead Programming Instructor.");
            return userRepository.save(u);
        });

        User student = userRepository.findByUsername("student_alex").orElseGet(() -> {
            User u = new User(
                    "student_alex",
                    "alex@learnhub.com",
                    passwordEncoder.encode("Password123"),
                    "Alex Morgan",
                    Role.ROLE_STUDENT
            );
            u.setBio("Full-stack engineering student mastering Java and Python.");
            return userRepository.save(u);
        });

        // 2. Seed Complete Java and Python Curricula via Idempotent Seeder
        curriculumSeeder.seedAllCurricula();

        // 3. Seed an active enrollment for student_alex in Java Programming Masterclass if not present
        Course javaCourse = courseRepository.findAll().stream()
                .filter(c -> c.getTitle() != null && c.getTitle().toLowerCase().contains("java programming"))
                .findFirst()
                .orElse(null);

        if (javaCourse != null && !enrollmentRepository.existsByStudentIdAndCourseId(student.getId(), javaCourse.getId())) {
            Enrollment enrollment = new Enrollment(student, javaCourse);
            long totalLessons = lessonRepository.countTotalLessonsByCourseId(javaCourse.getId());
            enrollment.setTotalLessonsCount((int) totalLessons);

            // Mark first 2 lessons completed as demonstration of persistent progress
            var lessons = lessonRepository.findAll().stream()
                    .filter(l -> l.getModule().getCourse().getId().equals(javaCourse.getId()))
                    .sorted((a, b) -> a.getId().compareTo(b.getId()))
                    .limit(2)
                    .toList();

            Enrollment savedEnrollment = enrollmentRepository.save(enrollment);

            for (Lesson l : lessons) {
                LessonProgress lp = new LessonProgress(savedEnrollment, l, true);
                lessonProgressRepository.save(lp);
                learningActivityRepository.save(new LearningActivity(
                        student,
                        javaCourse,
                        l,
                        ActivityType.LESSON_COMPLETED,
                        "Completed lesson '" + l.getTitle() + "'"
                ));
            }

            savedEnrollment.recalculateProgress(lessons.size(), (int) totalLessons);
            enrollmentRepository.save(savedEnrollment);
        }

        log.info("LearnHub baseline data initialized successfully.");
    }
}
