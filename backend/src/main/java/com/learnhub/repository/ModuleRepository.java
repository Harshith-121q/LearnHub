package com.learnhub.repository;

import com.learnhub.entity.Module;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Spring Data JPA Repository for Course Modules.
 */
@Repository
public interface ModuleRepository extends JpaRepository<Module, Long> {

    List<Module> findByCourseIdOrderBySequenceOrderAsc(Long courseId);

    Optional<Module> findByCourseIdAndSequenceOrder(Long courseId, Integer sequenceOrder);

    long countByCourseId(Long courseId);

    @Query("SELECT COALESCE(MAX(m.sequenceOrder), 0) FROM Module m WHERE m.course.id = :courseId")
    Integer findMaxSequenceOrderByCourseId(@Param("courseId") Long courseId);
}
