package com.learnhub.dto;

import java.time.LocalDateTime;

/**
 * Representation of an enrolled student and their course progress for instructor monitoring.
 */
public class EnrolledStudentResponse {

    private Long studentId;
    private String studentName;
    private String studentUsername;
    private String studentEmail;
    private LocalDateTime enrolledAt;
    private int completedLessonsCount;
    private int totalLessonsCount;
    private double progressPercentage;
    private boolean completed;
    private LocalDateTime lastActivityDate;
    private String lastActivityDescription;

    public EnrolledStudentResponse() {
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

    public LocalDateTime getEnrolledAt() {
        return enrolledAt;
    }

    public void setEnrolledAt(LocalDateTime enrolledAt) {
        this.enrolledAt = enrolledAt;
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

    public double getProgressPercentage() {
        return progressPercentage;
    }

    public void setProgressPercentage(double progressPercentage) {
        this.progressPercentage = progressPercentage;
    }

    public boolean isCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }

    public LocalDateTime getLastActivityDate() {
        return lastActivityDate;
    }

    public void setLastActivityDate(LocalDateTime lastActivityDate) {
        this.lastActivityDate = lastActivityDate;
    }

    public String getLastActivityDescription() {
        return lastActivityDescription;
    }

    public void setLastActivityDescription(String lastActivityDescription) {
        this.lastActivityDescription = lastActivityDescription;
    }
}
