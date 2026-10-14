package com.learnhub.dto;

import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;

import java.time.LocalDateTime;
import java.util.List;

/**
 * Lightweight summary representation of Course for lists and catalogs.
 */
public class CourseSummaryResponse {

    private Long id;
    private String title;
    private String description;
    private String category;
    private DifficultyLevel difficultyLevel;
    private Integer estimatedDuration;
    private CourseStatus status;
    private Long instructorId;
    private String instructorName;
    private String instructorUsername;
    private int moduleCount;
    private int lessonCount;
    private List<UserSummaryResponse> assignedInstructors = new java.util.ArrayList<>();
    private Long enrolledCount = 0L;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    public CourseSummaryResponse() {
    }

    public static CourseSummaryResponse from(Course course) {
        CourseSummaryResponse res = new CourseSummaryResponse();
        res.setId(course.getId());
        res.setTitle(course.getTitle());
        res.setDescription(course.getDescription());
        res.setCategory(course.getCategory());
        res.setDifficultyLevel(course.getDifficultyLevel());
        res.setEstimatedDuration(course.getEstimatedDuration());
        res.setStatus(course.getStatus());

        if (course.getInstructor() != null) {
            res.setInstructorId(course.getInstructor().getId());
            res.setInstructorName(course.getInstructor().getFullName());
            res.setInstructorUsername(course.getInstructor().getUsername());
        }

        if (course.getAssignedInstructors() != null && !course.getAssignedInstructors().isEmpty()) {
            res.setAssignedInstructors(course.getAssignedInstructors().stream()
                    .map(UserSummaryResponse::fromEntity)
                    .collect(java.util.stream.Collectors.toList()));
        }

        if (course.getModules() != null) {
            res.setModuleCount(course.getModules().size());
            int totalLessons = course.getModules().stream()
                    .mapToInt(m -> m.getLessons() != null ? m.getLessons().size() : 0)
                    .sum();
            res.setLessonCount(totalLessons);
        }

        res.setCreatedAt(course.getCreatedAt());
        res.setUpdatedAt(course.getUpdatedAt());
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

    public CourseStatus getStatus() {
        return status;
    }

    public void setStatus(CourseStatus status) {
        this.status = status;
    }

    public Long getInstructorId() {
        return instructorId;
    }

    public void setInstructorId(Long instructorId) {
        this.instructorId = instructorId;
    }

    public String getInstructorName() {
        return instructorName;
    }

    public void setInstructorName(String instructorName) {
        this.instructorName = instructorName;
    }

    public String getInstructorUsername() {
        return instructorUsername;
    }

    public void setInstructorUsername(String instructorUsername) {
        this.instructorUsername = instructorUsername;
    }

    public int getModuleCount() {
        return moduleCount;
    }

    public void setModuleCount(int moduleCount) {
        this.moduleCount = moduleCount;
    }

    public int getLessonCount() {
        return lessonCount;
    }

    public void setLessonCount(int lessonCount) {
        this.lessonCount = lessonCount;
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

    public List<UserSummaryResponse> getAssignedInstructors() {
        return assignedInstructors;
    }

    public void setAssignedInstructors(List<UserSummaryResponse> assignedInstructors) {
        this.assignedInstructors = assignedInstructors;
    }

    public Long getEnrolledCount() {
        return enrolledCount;
    }

    public void setEnrolledCount(Long enrolledCount) {
        this.enrolledCount = enrolledCount;
    }
}
