package com.learnhub.repository;

import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * Spring Data JPA Repository for Course entities.
 */
@Repository
public interface CourseRepository extends JpaRepository<Course, Long> {

    List<Course> findAllByOrderByCreatedAtDesc();

    List<Course> findByStatusOrderByCreatedAtDesc(CourseStatus status);

    @Query("SELECT DISTINCT c FROM Course c LEFT JOIN c.assignedInstructors ai " +
           "WHERE (c.instructor IS NOT NULL AND c.instructor.id = :instructorId) OR ai.id = :instructorId " +
           "ORDER BY c.createdAt DESC")
    List<Course> findAssignedCoursesForInstructor(@Param("instructorId") Long instructorId);

    List<Course> findByInstructorIdOrderByCreatedAtDesc(Long instructorId);

    long countByStatus(CourseStatus status);

    @Query("SELECT c FROM Course c WHERE c.status = 'PUBLISHED' " +
           "AND (:category IS NULL OR LOWER(c.category) = LOWER(:category)) " +
           "AND (:difficulty IS NULL OR c.difficultyLevel = :difficulty) " +
           "AND (:query IS NULL OR LOWER(c.title) LIKE LOWER(CONCAT('%', :query, '%')) " +
           "     OR LOWER(c.description) LIKE LOWER(CONCAT('%', :query, '%')))")
    Page<Course> searchPublishedCourses(
            @Param("query") String query,
            @Param("category") String category,
            @Param("difficulty") DifficultyLevel difficulty,
            Pageable pageable
    );
}
