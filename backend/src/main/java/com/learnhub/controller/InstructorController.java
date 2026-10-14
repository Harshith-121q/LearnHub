package com.learnhub.controller;

import com.learnhub.dto.ApiResponse;
import com.learnhub.dto.CourseDetailResponse;
import com.learnhub.dto.EnrolledStudentResponse;
import com.learnhub.dto.InstructorCourseSummaryResponse;
import com.learnhub.dto.StudentProgressDetailResponse;
import com.learnhub.security.UserPrincipal;
import com.learnhub.service.InstructorService;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * REST Controller for Instructor operations: viewing assigned courses, tracking student completions,
 * and reviewing learning activities. (Read-only access, no course editing or publishing).
 */
@RestController
@RequestMapping("/api/instructor")
@PreAuthorize("hasRole('INSTRUCTOR')")
public class InstructorController {

    private final InstructorService instructorService;

    public InstructorController(InstructorService instructorService) {
        this.instructorService = instructorService;
    }

    /**
     * Lists courses assigned to the authenticated instructor with completion & student metrics.
     */
    @GetMapping("/courses")
    public ResponseEntity<ApiResponse<List<InstructorCourseSummaryResponse>>> getAssignedCourses(
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<InstructorCourseSummaryResponse> courses = instructorService.getAssignedCourses(currentUser);
        return ResponseEntity.ok(ApiResponse.success("Assigned courses retrieved successfully", courses));
    }

    /**
     * Retrieves course curriculum details for an assigned course.
     */
    @GetMapping("/courses/{id}")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> getAssignedCourseContent(
            @PathVariable Long id,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = instructorService.getAssignedCourseContent(id, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course details retrieved successfully", course));
    }

    /**
     * Lists enrolled students with progress percentages and optional filtering (all, in-progress, completed).
     */
    @GetMapping("/courses/{id}/students")
    public ResponseEntity<ApiResponse<List<EnrolledStudentResponse>>> getEnrolledStudents(
            @PathVariable Long id,
            @RequestParam(required = false, defaultValue = "all") String filter,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<EnrolledStudentResponse> students = instructorService.getEnrolledStudents(id, filter, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Enrolled students retrieved successfully", students));
    }

    /**
     * Retrieves progress details and activity history for an individual student in an assigned course.
     */
    @GetMapping("/courses/{id}/students/{studentId}")
    public ResponseEntity<ApiResponse<StudentProgressDetailResponse>> getStudentProgressDetail(
            @PathVariable Long id,
            @PathVariable Long studentId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        StudentProgressDetailResponse progress = instructorService.getStudentProgressDetail(id, studentId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Student progress details retrieved successfully", progress));
    }
}
