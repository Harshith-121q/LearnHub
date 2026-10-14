package com.learnhub.repository;

import com.learnhub.entity.LearningActivity;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Spring Data JPA Repository for LearningActivity audit and tracking events.
 */
@Repository
public interface LearningActivityRepository extends JpaRepository<LearningActivity, Long> {

    List<LearningActivity> findByStudentIdOrderByTimestampDesc(Long studentId, Pageable pageable);

    List<LearningActivity> findByCourseIdOrderByTimestampDesc(Long courseId, Pageable pageable);

    List<LearningActivity> findByStudentIdAndCourseIdOrderByTimestampDesc(Long studentId, Long courseId);

    Optional<LearningActivity> findFirstByStudentIdAndCourseIdOrderByTimestampDesc(Long studentId, Long courseId);

    Optional<LearningActivity> findFirstByStudentIdOrderByTimestampDesc(Long studentId);
}
