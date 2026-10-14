package com.learnhub.dto;

import com.learnhub.entity.Lesson;

import java.time.LocalDateTime;

/**
 * Detailed representation of a Lesson for responses.
 */
public class LessonResponse {

    private Long id;
    private String title;
    private String content;
    private String codeExample;
    private String videoUrl;
    private Integer sequenceOrder;
    private Integer estimatedDuration;
    private Long moduleId;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    public LessonResponse() {
    }

    public static LessonResponse from(Lesson lesson) {
        LessonResponse res = new LessonResponse();
        res.setId(lesson.getId());
        res.setTitle(lesson.getTitle());
        res.setContent(lesson.getContent());
        res.setCodeExample(lesson.getCodeExample());
        res.setVideoUrl(lesson.getVideoUrl());
        res.setSequenceOrder(lesson.getSequenceOrder());
        res.setEstimatedDuration(lesson.getEstimatedDuration());
        if (lesson.getModule() != null) {
            res.setModuleId(lesson.getModule().getId());
        }
        res.setCreatedAt(lesson.getCreatedAt());
        res.setUpdatedAt(lesson.getUpdatedAt());
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

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getCodeExample() {
        return codeExample;
    }

    public void setCodeExample(String codeExample) {
        this.codeExample = codeExample;
    }

    public String getVideoUrl() {
        return videoUrl;
    }

    public void setVideoUrl(String videoUrl) {
        this.videoUrl = videoUrl;
    }

    public Integer getSequenceOrder() {
        return sequenceOrder;
    }

    public void setSequenceOrder(Integer sequenceOrder) {
        this.sequenceOrder = sequenceOrder;
    }

    public Integer getEstimatedDuration() {
        return estimatedDuration;
    }

    public void setEstimatedDuration(Integer estimatedDuration) {
        this.estimatedDuration = estimatedDuration;
    }

    public Integer getDurationMinutes() {
        return estimatedDuration;
    }

    public void setDurationMinutes(Integer durationMinutes) {
        this.estimatedDuration = durationMinutes;
    }

    public Long getModuleId() {
        return moduleId;
    }

    public void setModuleId(Long moduleId) {
        this.moduleId = moduleId;
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
