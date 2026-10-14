package com.learnhub.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

/**
 * Payload for updating an existing lesson.
 */
public class UpdateLessonRequest {

    @NotBlank(message = "Lesson title is required")
    @Size(max = 150, message = "Lesson title cannot exceed 150 characters")
    private String title;

    @NotBlank(message = "Lesson content is required")
    private String content;

    private String codeExample;

    private String videoUrl;

    private Integer sequenceOrder;

    @Min(value = 1, message = "Estimated duration must be at least 1 minute")
    private Integer estimatedDuration;

    public UpdateLessonRequest() {
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
}
