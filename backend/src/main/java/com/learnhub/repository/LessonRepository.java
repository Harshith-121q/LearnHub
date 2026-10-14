package com.learnhub.repository;

import com.learnhub.entity.Lesson;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Spring Data JPA Repository for Lessons.
 */
@Repository
public interface LessonRepository extends JpaRepository<Lesson, Long> {

    List<Lesson> findByModuleIdOrderBySequenceOrderAsc(Long moduleId);

    Optional<Lesson> findByModuleIdAndSequenceOrder(Long moduleId, Integer sequenceOrder);

    long countByModuleId(Long moduleId);

    @Query("SELECT COALESCE(MAX(l.sequenceOrder), 0) FROM Lesson l WHERE l.module.id = :moduleId")
    Integer findMaxSequenceOrderByModuleId(@Param("moduleId") Long moduleId);

    @Query("SELECT COUNT(l) FROM Lesson l WHERE l.module.course.id = :courseId")
    long countTotalLessonsByCourseId(@Param("courseId") Long courseId);
}
