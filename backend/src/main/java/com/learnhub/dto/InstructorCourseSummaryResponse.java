package com.learnhub.dto;

import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;

/**
 * Summary metrics of an assigned course for instructor dashboard.
 */
public class InstructorCourseSummaryResponse {

    private Long id;
    private String title;
    private String description;
    private String category;
    private DifficultyLevel difficultyLevel;
    private CourseStatus status;
    private long totalEnrolledStudents;
    private long studentsStarted;
    private long studentsCompleted;
    private double averageCompletionPercentage;
    private int totalModules;
    private long totalLessons;

    public InstructorCourseSummaryResponse() {
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

    public CourseStatus getStatus() {
        return status;
    }

    public void setStatus(CourseStatus status) {
        this.status = status;
    }

    public long getTotalEnrolledStudents() {
        return totalEnrolledStudents;
    }

    public void setTotalEnrolledStudents(long totalEnrolledStudents) {
        this.totalEnrolledStudents = totalEnrolledStudents;
    }

    public long getStudentsStarted() {
        return studentsStarted;
    }

    public void setStudentsStarted(long studentsStarted) {
        this.studentsStarted = studentsStarted;
    }

    public long getStudentsCompleted() {
        return studentsCompleted;
    }

    public void setStudentsCompleted(long studentsCompleted) {
        this.studentsCompleted = studentsCompleted;
    }

    public double getAverageCompletionPercentage() {
        return averageCompletionPercentage;
    }

    public void setAverageCompletionPercentage(double averageCompletionPercentage) {
        this.averageCompletionPercentage = averageCompletionPercentage;
    }

    public int getTotalModules() {
        return totalModules;
    }

    public void setTotalModules(int totalModules) {
        this.totalModules = totalModules;
    }

    public long getTotalLessons() {
        return totalLessons;
    }

    public void setTotalLessons(long totalLessons) {
        this.totalLessons = totalLessons;
    }
}
