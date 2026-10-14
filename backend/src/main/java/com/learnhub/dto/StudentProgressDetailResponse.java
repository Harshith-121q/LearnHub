package com.learnhub.dto;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Detailed student progress report on an assigned course, for instructor inspection.
 */
public class StudentProgressDetailResponse {

    private Long studentId;
    private String studentName;
    private String studentUsername;
    private String studentEmail;
    private Long courseId;
    private String courseTitle;
    private LocalDateTime enrolledAt;
    private double progressPercentage;
    private int completedLessonsCount;
    private int totalLessonsCount;
    private boolean completed;
    private LocalDateTime completedAt;
    private Set<Long> completedLessonIds = new HashSet<>();
    private List<LearningActivityResponse> recentActivities = new ArrayList<>();

    public StudentProgressDetailResponse() {
    }

    public Long getStudentId() {
        return studentId;
    }

    public void setStudentId(Long studentId) {
        this.studentId = studentId;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public String getStudentUsername() {
        return studentUsername;
    }

    public void setStudentUsername(String studentUsername) {
        this.studentUsername = studentUsername;
    }

    public String getStudentEmail() {
        return studentEmail;
    }

    public void setStudentEmail(String studentEmail) {
        this.studentEmail = studentEmail;
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

    public LocalDateTime getEnrolledAt() {
        return enrolledAt;
    }

    public void setEnrolledAt(LocalDateTime enrolledAt) {
        this.enrolledAt = enrolledAt;
    }

    public double getProgressPercentage() {
        return progressPercentage;
    }

    public void setProgressPercentage(double progressPercentage) {
        this.progressPercentage = progressPercentage;
    }

    public int getCompletedLessonsCount() {
        return completedLessonsCount;
    }

    public void setCompletedLessonsCount(int completedLessonsCount) {
        this.completedLessonsCount = completedLessonsCount;
    }

    public int getTotalLessonsCount() {
        return totalLessonsCount;
    }

    public void setTotalLessonsCount(int totalLessonsCount) {
        this.totalLessonsCount = totalLessonsCount;
    }

    public boolean isCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }

    public LocalDateTime getCompletedAt() {
        return completedAt;
    }

    public void setCompletedAt(LocalDateTime completedAt) {
        this.completedAt = completedAt;
    }

    public Set<Long> getCompletedLessonIds() {
        return completedLessonIds;
    }

    public void setCompletedLessonIds(Set<Long> completedLessonIds) {
        this.completedLessonIds = completedLessonIds;
    }

    public List<LearningActivityResponse> getRecentActivities() {
        return recentActivities;
    }

    public void setRecentActivities(List<LearningActivityResponse> recentActivities) {
        this.recentActivities = recentActivities;
    }
}
