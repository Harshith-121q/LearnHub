package com.learnhub.config;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;
import com.learnhub.entity.Enrollment;
import com.learnhub.entity.Lesson;
import com.learnhub.entity.Module;
import com.learnhub.entity.User;
import com.learnhub.repository.CourseRepository;
import com.learnhub.repository.EnrollmentRepository;
import com.learnhub.repository.LessonRepository;
import com.learnhub.repository.ModuleRepository;
import com.learnhub.repository.UserRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.io.InputStream;
import java.util.List;
import java.util.Optional;

/**
 * Idempotent seeder that imports complete, high-quality educational curricula
 * for Java Programming and Python Programming.
 * Preserves Admin edits and prevents duplicate records upon re-execution.
 */
@Component
public class CurriculumSeeder {

    private static final Logger log = LoggerFactory.getLogger(CurriculumSeeder.class);

    private final CourseRepository courseRepository;
    private final ModuleRepository moduleRepository;
    private final LessonRepository lessonRepository;
    private final EnrollmentRepository enrollmentRepository;
    private final UserRepository userRepository;
    private final ObjectMapper objectMapper;

    public CurriculumSeeder(CourseRepository courseRepository,
                            ModuleRepository moduleRepository,
                            LessonRepository lessonRepository,
                            EnrollmentRepository enrollmentRepository,
                            UserRepository userRepository,
                            ObjectMapper objectMapper) {
        this.courseRepository = courseRepository;
        this.moduleRepository = moduleRepository;
        this.lessonRepository = lessonRepository;
        this.enrollmentRepository = enrollmentRepository;
        this.userRepository = userRepository;
        this.objectMapper = objectMapper;
    }

    /**
     * Seeds both Java Programming Masterclass and Python Programming Masterclass idempotently.
     */
    @Transactional
    public void seedAllCurricula() {
        log.info("Starting idempotent curriculum import for Java and Python tracks...");
        
        User instructor = userRepository.findByUsername("instructor_sarah")
                .orElseGet(() -> userRepository.findAll().stream()
                        .filter(u -> "ROLE_INSTRUCTOR".equals(u.getRole().name()))
                        .findFirst()
                        .orElse(null));

        seedCourseFromResource("curriculum/java-curriculum.json", "Java Programming", instructor);
        seedCourseFromResource("curriculum/python-curriculum.json", "Python Programming", instructor);

        log.info("Curriculum import completed successfully.");
    }

    @Transactional
    public void seedCourseFromResource(String resourcePath, String courseSearchKey, User instructor) {
        try {
            ClassPathResource resource = new ClassPathResource(resourcePath);
            if (!resource.exists()) {
                log.warn("Curriculum resource file not found: {}", resourcePath);
                return;
            }

            try (InputStream is = resource.getInputStream()) {
                JsonNode root = objectMapper.readTree(is);
                String title = root.path("title").asText();
                String description = root.path("description").asText();
                String category = root.path("category").asText("Programming Languages");
                String difficultyStr = root.path("difficultyLevel").asText("BEGINNER");
                String learningObjectives = root.path("learningObjectives").asText();
                String prerequisites = root.path("prerequisites").asText();
                int estimatedDuration = root.path("estimatedDuration").asInt(3000);

                DifficultyLevel difficulty = DifficultyLevel.BEGINNER;
                try {
                    difficulty = DifficultyLevel.valueOf(difficultyStr);
                } catch (Exception ignored) {
                }

                // 1. Idempotently Find or Create Course
                DifficultyLevel finalDifficulty = difficulty;
                Course course = courseRepository.findAll().stream()
                        .filter(c -> c.getTitle() != null &&
                                (c.getTitle().equalsIgnoreCase(title) ||
                                 c.getTitle().toLowerCase().contains(courseSearchKey.toLowerCase())))
                        .findFirst()
                        .orElseGet(() -> {
                            Course c = new Course(
                                    title,
                                    description,
                                    category,
                                    finalDifficulty,
                                    learningObjectives,
                                    prerequisites,
                                    estimatedDuration,
                                    instructor
                            );
                            c.setStatus(CourseStatus.PUBLISHED);
                            if (instructor != null) {
                                c.addInstructor(instructor);
                            }
                            log.info("Creating new Course entity: '{}'", title);
                            return courseRepository.save(c);
                        });

                // Update course attributes to ensure published status and canonical title
                course.setTitle(title);
                course.setDescription(description);
                course.setCategory(category);
                course.setStatus(CourseStatus.PUBLISHED);
                course.setEstimatedDuration(estimatedDuration);
                if (instructor != null) {
                    course.setInstructor(instructor);
                    course.addInstructor(instructor);
                }
                final Course finalCourse = courseRepository.save(course);

                // 2. Iterate and Seed Modules
                JsonNode modulesNode = root.path("modules");
                if (modulesNode.isArray()) {
                    for (int mIdx = 0; mIdx < modulesNode.size(); mIdx++) {
                        JsonNode modNode = modulesNode.get(mIdx);
                        String modTitle = modNode.path("title").asText();
                        String modDesc = modNode.path("description").asText();
                        int modSeq = modNode.path("sequenceOrder").asInt(mIdx + 1);

                        // Find or create module idempotently
                        Module module = moduleRepository.findByCourseIdAndSequenceOrder(finalCourse.getId(), modSeq)
                                .orElseGet(() -> moduleRepository.findByCourseIdOrderBySequenceOrderAsc(finalCourse.getId()).stream()
                                        .filter(m -> m.getTitle().equalsIgnoreCase(modTitle))
                                        .findFirst()
                                        .orElseGet(() -> {
                                            Module m = new Module(modTitle, modDesc, modSeq, null);
                                            m.setCourse(finalCourse);
                                            return moduleRepository.save(m);
                                        }));

                        // Update module title and description if it was a basic stub
                        if (module.getTitle() == null || !module.getTitle().equals(modTitle)) {
                            module.setTitle(modTitle);
                        }
                        if (module.getDescription() == null || module.getDescription().isBlank()) {
                            module.setDescription(modDesc);
                        }
                        module.setSequenceOrder(modSeq);
                        module = moduleRepository.save(module);

                        // 3. Iterate and Seed Lessons
                        JsonNode lessonsNode = modNode.path("lessons");
                        if (lessonsNode.isArray()) {
                            for (int lIdx = 0; lIdx < lessonsNode.size(); lIdx++) {
                                JsonNode lesNode = lessonsNode.get(lIdx);
                                String lesTitle = lesNode.path("title").asText();
                                String content = lesNode.path("content").asText();
                                String codeExample = lesNode.path("codeExample").asText("");
                                int duration = lesNode.path("estimatedDuration").asInt(20);
                                int lesSeq = lesNode.path("sequenceOrder").asInt(lIdx + 1);

                                Optional<Lesson> existingLessonOpt = lessonRepository.findByModuleIdAndSequenceOrder(module.getId(), lesSeq);
                                if (existingLessonOpt.isEmpty()) {
                                    existingLessonOpt = lessonRepository.findByModuleIdOrderBySequenceOrderAsc(module.getId()).stream()
                                            .filter(l -> l.getTitle().equalsIgnoreCase(lesTitle))
                                            .findFirst();
                                }

                                if (existingLessonOpt.isPresent()) {
                                    Lesson existing = existingLessonOpt.get();
                                    // Idempotency: Do NOT overwrite content that an Admin has substantively edited
                                    boolean hasCustomAdminContent = existing.getContent() != null &&
                                            existing.getContent().length() > 500 &&
                                            existing.getContent().contains("### 🎯 Learning Objectives");

                                    if (!hasCustomAdminContent) {
                                        existing.setTitle(lesTitle);
                                        existing.setContent(content);
                                        existing.setCodeExample(codeExample);
                                        existing.setEstimatedDuration(duration);
                                        existing.setSequenceOrder(lesSeq);
                                        existing.setVideoUrl(null); // No invented URLs
                                        lessonRepository.save(existing);
                                    }
                                } else {
                                    Lesson newLesson = new Lesson(
                                            lesTitle,
                                            content,
                                            codeExample,
                                            null, // No invented video URLs
                                            duration,
                                            lesSeq,
                                            module
                                    );
                                    lessonRepository.save(newLesson);
                                }
                            }
                        }
                    }
                }

                // 4. Synchronize Enrollment total lesson counts
                long totalLessons = lessonRepository.countTotalLessonsByCourseId(finalCourse.getId());
                log.info("Course '{}' (ID: {}) now contains {} total lessons across {} modules.",
                        finalCourse.getTitle(), finalCourse.getId(), totalLessons, moduleRepository.countByCourseId(finalCourse.getId()));

                List<Enrollment> enrollments = enrollmentRepository.findByCourseIdOrderByEnrolledAtDesc(finalCourse.getId());
                for (Enrollment enr : enrollments) {
                    enr.setTotalLessonsCount((int) totalLessons);
                    int completed = enr.getCompletedLessonsCount() != null ? enr.getCompletedLessonsCount() : 0;
                    enr.recalculateProgress(completed, (int) totalLessons);
                    enrollmentRepository.save(enr);
                }
            }
        } catch (Exception e) {
            log.error("Error seeding curriculum from {}: {}", resourcePath, e.getMessage(), e);
        }
    }
}
