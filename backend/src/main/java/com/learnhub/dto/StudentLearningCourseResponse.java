package com.learnhub.dto;

import com.learnhub.entity.DifficultyLevel;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Full learning curriculum data package returned for an enrolled student.
 */
public class StudentLearningCourseResponse {

    private Long enrollmentId;
    private Long courseId;
    private String title;
    private String description;
    private String category;
    private DifficultyLevel difficultyLevel;
    private Integer estimatedDuration;
    private List<ModuleResponse> modules = new ArrayList<>();
    private Set<Long> completedLessonIds = new HashSet<>();
    private Double progressPercentage;
    private Integer completedLessonsCount;
    private Integer totalLessonsCount;
    private Boolean isCompleted;
    private Long resumeLessonId;

    public StudentLearningCourseResponse() {
    }

    public Long getEnrollmentId() {
        return enrollmentId;
    }

    public void setEnrollmentId(Long enrollmentId) {
        this.enrollmentId = enrollmentId;
    }

    public Long getCourseId() {
        return courseId;
    }

    public void setCourseId(Long courseId) {
        this.courseId = courseId;
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

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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

    public List<ModuleResponse> getModules() {
        return modules;
    }

    public void setModules(List<ModuleResponse> modules) {
        this.modules = modules;
    }

    public Set<Long> getCompletedLessonIds() {
        return completedLessonIds;
    }

    public void setCompletedLessonIds(Set<Long> completedLessonIds) {
        this.completedLessonIds = completedLessonIds;
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

    public Boolean getIsCompleted() {
        return isCompleted;
    }

    public void setIsCompleted(Boolean isCompleted) {
        this.isCompleted = isCompleted;
    }

    public Long getResumeLessonId() {
        return resumeLessonId;
    }

    public void setResumeLessonId(Long resumeLessonId) {
        this.resumeLessonId = resumeLessonId;
    }
}
