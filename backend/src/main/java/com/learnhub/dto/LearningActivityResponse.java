package com.learnhub.dto;

import com.learnhub.entity.ActivityType;
import com.learnhub.entity.LearningActivity;

import java.time.LocalDateTime;

/**
 * Representation of a single learning event.
 */
public class LearningActivityResponse {

    private Long id;
    private Long courseId;
    private String courseTitle;
    private Long lessonId;
    private String lessonTitle;
    private ActivityType activityType;
    private String description;
    private LocalDateTime timestamp;

    public LearningActivityResponse() {
    }

    public static LearningActivityResponse from(LearningActivity activity) {
        LearningActivityResponse res = new LearningActivityResponse();
        res.setId(activity.getId());
        if (activity.getCourse() != null) {
            res.setCourseId(activity.getCourse().getId());
            res.setCourseTitle(activity.getCourse().getTitle());
        }
        if (activity.getLesson() != null) {
            res.setLessonId(activity.getLesson().getId());
            res.setLessonTitle(activity.getLesson().getTitle());
        }
        res.setActivityType(activity.getActivityType());
        res.setDescription(activity.getDescription());
        res.setTimestamp(activity.getTimestamp());
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

    public Long getLessonId() {
        return lessonId;
    }

    public void setLessonId(Long lessonId) {
        this.lessonId = lessonId;
    }

    public String getLessonTitle() {
        return lessonTitle;
    }

    public void setLessonTitle(String lessonTitle) {
        this.lessonTitle = lessonTitle;
    }

    public ActivityType getActivityType() {
        return activityType;
    }

    public void setActivityType(ActivityType activityType) {
        this.activityType = activityType;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
