package com.learnhub.repository;

import com.learnhub.entity.Enrollment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Spring Data JPA Repository for Enrollment entities.
 */
@Repository
public interface EnrollmentRepository extends JpaRepository<Enrollment, Long> {

    List<Enrollment> findByStudentIdOrderByEnrolledAtDesc(Long studentId);

    List<Enrollment> findByCourseIdOrderByEnrolledAtDesc(Long courseId);

    Optional<Enrollment> findByStudentIdAndCourseId(Long studentId, Long courseId);

    boolean existsByStudentIdAndCourseId(Long studentId, Long courseId);

    long countByCourseId(Long courseId);

    long countByCourseIdAndCompletedTrue(Long courseId);

    long countByCourseIdAndCompletedLessonsCountGreaterThan(Long courseId, Integer count);

    @Query("SELECT COUNT(DISTINCT e.student.id) FROM Enrollment e")
    long countDistinctStudents();

    @Query("SELECT AVG(e.progressPercentage) FROM Enrollment e WHERE e.course.id = :courseId")
    Double getAverageProgressByCourseId(@Param("courseId") Long courseId);
}
