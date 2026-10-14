package com.learnhub.dto;

import com.learnhub.entity.Course;
import com.learnhub.entity.CourseStatus;
import com.learnhub.entity.DifficultyLevel;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Full details of a course including modules, lessons, and review metadata.
 */
public class CourseDetailResponse {

    private Long id;
    private String title;
    private String description;
    private String category;
    private DifficultyLevel difficultyLevel;
    private String learningObjectives;
    private String prerequisites;
    private Integer estimatedDuration;
    private CourseStatus status;
    private Long instructorId;
    private String instructorName;
    private String instructorUsername;
    private List<ModuleResponse> modules = new ArrayList<>();
    private List<UserSummaryResponse> assignedInstructors = new ArrayList<>();
    private Long enrolledCount = 0L;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    public CourseDetailResponse() {
    }

    public static CourseDetailResponse from(Course course) {
        CourseDetailResponse res = new CourseDetailResponse();
        res.setId(course.getId());
        res.setTitle(course.getTitle());
        res.setDescription(course.getDescription());
        res.setCategory(course.getCategory());
        res.setDifficultyLevel(course.getDifficultyLevel());
        res.setLearningObjectives(course.getLearningObjectives());
        res.setPrerequisites(course.getPrerequisites());
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
                    .collect(Collectors.toList()));
        }

        if (course.getModules() != null) {
            res.setModules(course.getModules().stream()
                    .map(ModuleResponse::from)
                    .collect(Collectors.toList()));
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

    public String getLearningObjectives() {
        return learningObjectives;
    }

    public void setLearningObjectives(String learningObjectives) {
        this.learningObjectives = learningObjectives;
    }

    public String getPrerequisites() {
        return prerequisites;
    }

    public void setPrerequisites(String prerequisites) {
        this.prerequisites = prerequisites;
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

    public List<ModuleResponse> getModules() {
        return modules;
    }

    public void setModules(List<ModuleResponse> modules) {
        this.modules = modules;
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
