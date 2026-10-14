package com.learnhub.dto;

import com.learnhub.entity.DifficultyLevel;
import com.learnhub.entity.Enrollment;

import java.time.LocalDateTime;

/**
 * Representation of a student course enrollment.
 */
public class EnrollmentResponse {

    private Long id;
    private Long courseId;
    private String courseTitle;
    private String courseCategory;
    private DifficultyLevel difficultyLevel;
    private Integer estimatedDuration;
    private LocalDateTime enrolledAt;
    private Double progressPercentage;
    private Integer completedLessonsCount;
    private Integer totalLessonsCount;
    private Boolean completed;
    private LocalDateTime completedAt;
    private LocalDateTime lastAccessedAt;

    public EnrollmentResponse() {
    }

    public static EnrollmentResponse from(Enrollment enrollment) {
        EnrollmentResponse res = new EnrollmentResponse();
        res.setId(enrollment.getId());
        if (enrollment.getCourse() != null) {
            res.setCourseId(enrollment.getCourse().getId());
            res.setCourseTitle(enrollment.getCourse().getTitle());
            res.setCourseCategory(enrollment.getCourse().getCategory());
            res.setDifficultyLevel(enrollment.getCourse().getDifficultyLevel());
            res.setEstimatedDuration(enrollment.getCourse().getEstimatedDuration());
        }
        res.setEnrolledAt(enrollment.getEnrolledAt());
        res.setProgressPercentage(enrollment.getProgressPercentage());
        res.setCompletedLessonsCount(enrollment.getCompletedLessonsCount());
        res.setTotalLessonsCount(enrollment.getTotalLessonsCount());
        res.setCompleted(enrollment.getCompleted());
        res.setCompletedAt(enrollment.getCompletedAt());
        res.setLastAccessedAt(enrollment.getLastAccessedAt());
        return res;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getCourseId() {
        return courseId;
    }

    public void setCourseId(Long courseId) {
        this.courseId = courseId;
    }

    public String getCourseTitle() {
        return courseTitle;
    }

    public void setCourseTitle(String courseTitle) {
        this.courseTitle = courseTitle;
    }

    public String getCourseCategory() {
        return courseCategory;
    }

    public void setCourseCategory(String courseCategory) {
        this.courseCategory = courseCategory;
    }

    public DifficultyLevel getDifficultyLevel() {
        return difficultyLevel;
    }

    public void setDifficultyLevel(DifficultyLevel difficultyLevel) {
        this.difficultyLevel = difficultyLevel;
    }

    public Integer getEstimatedDuration() {
        return estimatedDuration;
    }

    public void setEstimatedDuration(Integer estimatedDuration) {
        this.estimatedDuration = estimatedDuration;
    }

    public LocalDateTime getEnrolledAt() {
        return enrolledAt;
    }

    public void setEnrolledAt(LocalDateTime enrolledAt) {
        this.enrolledAt = enrolledAt;
    }

    public Double getProgressPercentage() {
        return progressPercentage;
    }

    public void setProgressPercentage(Double progressPercentage) {
        this.progressPercentage = progressPercentage;
    }

    public Integer getCompletedLessonsCount() {
        return completedLessonsCount;
    }

    public void setCompletedLessonsCount(Integer completedLessonsCount) {
        this.completedLessonsCount = completedLessonsCount;
    }

    public Integer getTotalLessonsCount() {
        return totalLessonsCount;
    }

    public void setTotalLessonsCount(Integer totalLessonsCount) {
        this.totalLessonsCount = totalLessonsCount;
    }

    public Boolean getCompleted() {
        return completed;
    }

    public void setCompleted(Boolean completed) {
        this.completed = completed;
    }

    public LocalDateTime getCompletedAt() {
        return completedAt;
    }

    public void setCompletedAt(LocalDateTime completedAt) {
        this.completedAt = completedAt;
    }

    public LocalDateTime getLastAccessedAt() {
        return lastAccessedAt;
    }

    public void setLastAccessedAt(LocalDateTime lastAccessedAt) {
        this.lastAccessedAt = lastAccessedAt;
    }
}
