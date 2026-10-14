package com.learnhub.repository;

import com.learnhub.entity.LessonProgress;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Spring Data JPA Repository for LessonProgress entities.
 */
@Repository
public interface LessonProgressRepository extends JpaRepository<LessonProgress, Long> {

    List<LessonProgress> findByEnrollmentId(Long enrollmentId);

    List<LessonProgress> findByEnrollmentIdAndCompletedTrue(Long enrollmentId);

    Optional<LessonProgress> findByEnrollmentIdAndLessonId(Long enrollmentId, Long lessonId);

    long countByEnrollmentIdAndCompletedTrue(Long enrollmentId);

    boolean existsByEnrollmentIdAndLessonIdAndCompletedTrue(Long enrollmentId, Long lessonId);
}
