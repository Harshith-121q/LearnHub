package com.learnhub.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

/**
 * Lesson entity representing instructional content within a Module.
 * Contains explanatory content, programming code examples, video/resource links, and duration.
 */
@Entity
@Table(name = "lessons")
public class Lesson extends BaseEntity {

    @Column(name = "title", nullable = false, length = 150)
    private String title;

    @Column(name = "content", columnDefinition = "LONGTEXT", nullable = false)
    private String content;

    @Column(name = "code_example", columnDefinition = "LONGTEXT")
    private String codeExample;

    @Column(name = "video_url", length = 500)
    private String videoUrl;

    @Column(name = "sequence_order", nullable = false)
    private Integer sequenceOrder = 1;

    @Column(name = "estimated_duration")
    private Integer estimatedDuration = 15; // in minutes

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "module_id", nullable = false)
    private Module module;

    public Lesson() {
    }

    public Lesson(String title, String content, Integer sequenceOrder, Integer estimatedDuration, Module module) {
        this.title = title;
        this.content = content;
        this.sequenceOrder = sequenceOrder;
        this.estimatedDuration = estimatedDuration;
        this.module = module;
    }

    public Lesson(String title, String content, String videoUrl, Integer estimatedDuration, Integer sequenceOrder, Module module) {
        this.title = title;
        this.content = content;
        this.videoUrl = videoUrl;
        this.estimatedDuration = estimatedDuration;
        this.sequenceOrder = sequenceOrder;
        this.module = module;
    }

    public Lesson(String title, String content, String codeExample, String videoUrl, Integer estimatedDuration, Integer sequenceOrder, Module module) {
        this.title = title;
        this.content = content;
        this.codeExample = codeExample;
        this.videoUrl = videoUrl;
        this.estimatedDuration = estimatedDuration;
        this.sequenceOrder = sequenceOrder;
        this.module = module;
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

    public Module getModule() {
        return module;
    }

    public void setModule(Module module) {
        this.module = module;
    }
}
