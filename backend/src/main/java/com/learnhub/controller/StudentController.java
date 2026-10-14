package com.learnhub.controller;

import com.learnhub.dto.ApiResponse;
import com.learnhub.dto.EnrollmentResponse;
import com.learnhub.dto.StudentLearningCourseResponse;
import com.learnhub.security.UserPrincipal;
import com.learnhub.service.StudentLearningService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

/**
 * REST Controller for Student operations: course enrollment, sequential lesson learning,
 * and progress tracking.
 */
@RestController
@RequestMapping("/api/student")
@PreAuthorize("hasRole('STUDENT')")
public class StudentController {

    private final StudentLearningService studentLearningService;

    public StudentController(StudentLearningService studentLearningService) {
        this.studentLearningService = studentLearningService;
    }

    /**
     * Lists courses the authenticated student is currently enrolled in.
     */
    @GetMapping("/enrollments")
    public ResponseEntity<ApiResponse<List<EnrollmentResponse>>> getMyEnrollments(
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<EnrollmentResponse> enrollments = studentLearningService.getMyEnrollments(currentUser);
        return ResponseEntity.ok(ApiResponse.success("Enrollments retrieved successfully", enrollments));
    }

    /**
     * Enrolls the authenticated student into a published course.
     */
    @PostMapping("/courses/{courseId}/enroll")
    public ResponseEntity<ApiResponse<EnrollmentResponse>> enroll(
            @PathVariable Long courseId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        EnrollmentResponse response = studentLearningService.enroll(courseId, currentUser);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.success("Enrolled in course successfully", response));
    }

    /**
     * Checks if current student is enrolled in a specific course.
     */
    @GetMapping("/courses/{courseId}/is-enrolled")
    public ResponseEntity<ApiResponse<Map<String, Boolean>>> isEnrolled(
            @PathVariable Long courseId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        boolean enrolled = studentLearningService.isEnrolled(courseId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Enrollment status checked", Map.of("enrolled", enrolled)));
    }

    /**
     * Retrieves full learning curriculum, lesson content, and completion status for an enrolled course.
     */
    @GetMapping("/courses/{courseId}/learn")
    public ResponseEntity<ApiResponse<StudentLearningCourseResponse>> getCourseLearningContent(
            @PathVariable Long courseId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        StudentLearningCourseResponse response = studentLearningService.getCourseLearningContent(courseId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Learning content loaded successfully", response));
    }

    /**
     * Marks a lesson as completed, recalculating progress percentage.
     */
    @PostMapping("/lessons/{lessonId}/complete")
    public ResponseEntity<ApiResponse<EnrollmentResponse>> markLessonComplete(
            @PathVariable Long lessonId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        EnrollmentResponse response = studentLearningService.markLessonComplete(lessonId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Lesson marked as complete", response));
    }

    /**
     * Marks a lesson as incomplete, recalculating progress percentage.
     */
    @PostMapping("/lessons/{lessonId}/uncomplete")
    public ResponseEntity<ApiResponse<EnrollmentResponse>> markLessonIncomplete(
            @PathVariable Long lessonId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        EnrollmentResponse response = studentLearningService.markLessonIncomplete(lessonId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Lesson marked as incomplete", response));
    }

    /**
     * Records lesson opened activity and updates last accessed timestamp.
     */
    @PostMapping("/lessons/{lessonId}/opened")
    public ResponseEntity<ApiResponse<Void>> recordLessonOpened(
            @PathVariable Long lessonId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        studentLearningService.recordLessonOpened(lessonId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Lesson opened activity logged", null));
    }
}
