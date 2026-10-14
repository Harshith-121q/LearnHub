package com.learnhub.dto;

import jakarta.validation.constraints.NotNull;

/**
 * Request body for assigning an instructor to a course.
 */
public class InstructorAssignmentRequest {

    @NotNull(message = "Instructor ID is required")
    private Long instructorId;

    public InstructorAssignmentRequest() {
    }

    public InstructorAssignmentRequest(Long instructorId) {
        this.instructorId = instructorId;
    }

    public Long getInstructorId() {
        return instructorId;
    }

    public void setInstructorId(Long instructorId) {
        this.instructorId = instructorId;
    }
}
