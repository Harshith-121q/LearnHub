package com.learnhub.dto;

import com.learnhub.entity.Module;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Detailed representation of a Module including lessons.
 */
public class ModuleResponse {

    private Long id;
    private String title;
    private String description;
    private Integer sequenceOrder;
    private Long courseId;
    private List<LessonResponse> lessons = new ArrayList<>();
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    public ModuleResponse() {
    }

    public static ModuleResponse from(Module module) {
        ModuleResponse res = new ModuleResponse();
        res.setId(module.getId());
        res.setTitle(module.getTitle());
        res.setDescription(module.getDescription());
        res.setSequenceOrder(module.getSequenceOrder());
        if (module.getCourse() != null) {
            res.setCourseId(module.getCourse().getId());
        }
        if (module.getLessons() != null) {
            res.setLessons(module.getLessons().stream()
                    .map(LessonResponse::from)
                    .collect(Collectors.toList()));
        }
        res.setCreatedAt(module.getCreatedAt());
        res.setUpdatedAt(module.getUpdatedAt());
        return res;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Integer getSequenceOrder() {
        return sequenceOrder;
    }

    public void setSequenceOrder(Integer sequenceOrder) {
        this.sequenceOrder = sequenceOrder;
    }

    public Long getCourseId() {
        return courseId;
    }

    public void setCourseId(Long courseId) {
        this.courseId = courseId;
    }

    public List<LessonResponse> getLessons() {
        return lessons;
    }

    public void setLessons(List<LessonResponse> lessons) {
        this.lessons = lessons;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
