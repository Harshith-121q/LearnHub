package com.learnhub.entity;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OrderBy;
import jakarta.persistence.Table;

import jakarta.persistence.ManyToMany;
import jakarta.persistence.JoinTable;
import jakarta.persistence.UniqueConstraint;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Course entity representing a complete course on LearnHub.
 */
@Entity
@Table(name = "courses")
public class Course extends BaseEntity {

    @Column(name = "title", nullable = false, length = 150)
    private String title;

    @Column(name = "description", columnDefinition = "TEXT")
    private String description;

    @Column(name = "category", nullable = false, length = 100)
    private String category;

    @Enumerated(EnumType.STRING)
    @Column(name = "difficulty_level", nullable = false, length = 30)
    private DifficultyLevel difficultyLevel = DifficultyLevel.BEGINNER;

    @Column(name = "learning_objectives", columnDefinition = "TEXT")
    private String learningObjectives;

    @Column(name = "prerequisites", columnDefinition = "TEXT")
    private String prerequisites;

    @Column(name = "estimated_duration")
    private Integer estimatedDuration = 60; // in minutes

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "instructor_id", nullable = true)
    private User instructor;

    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
            name = "course_instructors",
            joinColumns = @JoinColumn(name = "course_id"),
            inverseJoinColumns = @JoinColumn(name = "instructor_id"),
            uniqueConstraints = @UniqueConstraint(columnNames = {"course_id", "instructor_id"})
    )
    private Set<User> assignedInstructors = new HashSet<>();

    @Enumerated(EnumType.STRING)
    @Column(name = "status", nullable = false, length = 30)
    private CourseStatus status = CourseStatus.DRAFT;

    @OneToMany(mappedBy = "course", cascade = CascadeType.ALL, orphanRemoval = true)
    @OrderBy("sequenceOrder ASC")
    private List<Module> modules = new ArrayList<>();

    public Course() {
    }

    public Course(String title, String description, String category, DifficultyLevel difficultyLevel,
                  String learningObjectives, String prerequisites, Integer estimatedDuration, User instructor) {
        this.title = title;
        this.description = description;
        this.category = category;
        this.difficultyLevel = difficultyLevel != null ? difficultyLevel : DifficultyLevel.BEGINNER;
        this.learningObjectives = learningObjectives;
        this.prerequisites = prerequisites;
        this.estimatedDuration = estimatedDuration;
        this.instructor = instructor;
        this.status = CourseStatus.DRAFT;
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

    public User getInstructor() {
        return instructor;
    }

    public void setInstructor(User instructor) {
        this.instructor = instructor;
    }

    public CourseStatus getStatus() {
        return status;
    }

    public void setStatus(CourseStatus status) {
        this.status = status;
    }

    public List<Module> getModules() {
        return modules;
    }

    public void setModules(List<Module> modules) {
        this.modules = modules;
    }

    public Set<User> getAssignedInstructors() {
        return assignedInstructors;
    }

    public void setAssignedInstructors(Set<User> assignedInstructors) {
        this.assignedInstructors = assignedInstructors;
    }

    public void addInstructor(User instructor) {
        if (instructor != null) {
            this.assignedInstructors.add(instructor);
            if (this.instructor == null) {
                this.instructor = instructor;
            }
        }
    }

    public void removeInstructor(User instructor) {
        if (instructor != null) {
            this.assignedInstructors.remove(instructor);
            if (this.instructor != null && this.instructor.getId().equals(instructor.getId())) {
                this.instructor = this.assignedInstructors.isEmpty() ? null : this.assignedInstructors.iterator().next();
            }
        }
    }

    public boolean hasInstructor(Long instructorId) {
        if (instructorId == null) return false;
        if (this.instructor != null && instructorId.equals(this.instructor.getId())) return true;
        return this.assignedInstructors.stream().anyMatch(u -> instructorId.equals(u.getId()));
    }

    public void addModule(Module module) {
        modules.add(module);
        module.setCourse(this);
    }

    public void removeModule(Module module) {
        modules.remove(module);
        module.setCourse(null);
    }
}
