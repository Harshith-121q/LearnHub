package com.learnhub.controller;

import com.learnhub.dto.AdminStatsResponse;
import com.learnhub.dto.ApiResponse;
import com.learnhub.dto.CourseDetailResponse;
import com.learnhub.dto.CourseSummaryResponse;
import com.learnhub.dto.CreateCourseRequest;
import com.learnhub.dto.CreateLessonRequest;
import com.learnhub.dto.CreateModuleRequest;
import com.learnhub.dto.InstructorAssignmentRequest;
import com.learnhub.dto.LessonResponse;
import com.learnhub.dto.ModuleResponse;
import com.learnhub.dto.ReorderListRequest;
import com.learnhub.dto.UpdateCourseRequest;
import com.learnhub.dto.UpdateLessonRequest;
import com.learnhub.dto.UpdateModuleRequest;
import com.learnhub.dto.UserSummaryResponse;
import com.learnhub.security.UserPrincipal;
import com.learnhub.service.AdminService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * REST Controller for Administrator operations: course authoring, curriculum structure, and instructor assignments.
 */
@RestController
@RequestMapping("/api/admin")
@PreAuthorize("hasRole('ADMIN')")
public class AdminController {

    private final AdminService adminService;

    public AdminController(AdminService adminService) {
        this.adminService = adminService;
    }

    @GetMapping("/stats")
    public ResponseEntity<ApiResponse<AdminStatsResponse>> getStats(
            @AuthenticationPrincipal UserPrincipal currentUser) {
        AdminStatsResponse stats = adminService.getStats(currentUser);
        return ResponseEntity.ok(ApiResponse.success("Admin stats retrieved successfully", stats));
    }

    @GetMapping("/courses")
    public ResponseEntity<ApiResponse<List<CourseSummaryResponse>>> getAllCourses(
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<CourseSummaryResponse> courses = adminService.getAllCourses(currentUser);
        return ResponseEntity.ok(ApiResponse.success("All courses retrieved", courses));
    }

    @PostMapping("/courses")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> createCourse(
            @Valid @RequestBody CreateCourseRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.createCourse(request, currentUser);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.success("Course created successfully as draft", course));
    }

    @PutMapping("/courses/{id}")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> updateCourse(
            @PathVariable Long id,
            @Valid @RequestBody UpdateCourseRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.updateCourse(id, request, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course updated successfully", course));
    }

    @DeleteMapping("/courses/{id}")
    public ResponseEntity<ApiResponse<Void>> deleteCourse(
            @PathVariable Long id,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        adminService.deleteCourse(id, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course deleted successfully", null));
    }

    @PutMapping("/courses/{id}/publish")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> publishCourse(
            @PathVariable Long id,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.publishCourse(id, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course published successfully", course));
    }

    @PutMapping("/courses/{id}/unpublish")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> unpublishCourse(
            @PathVariable Long id,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.unpublishCourse(id, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course unpublished back to draft", course));
    }

    @PutMapping("/courses/{id}/archive")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> archiveCourse(
            @PathVariable Long id,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.archiveCourse(id, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course archived successfully", course));
    }

    @GetMapping("/instructors")
    public ResponseEntity<ApiResponse<List<UserSummaryResponse>>> getAvailableInstructors(
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<UserSummaryResponse> instructors = adminService.getAvailableInstructors(currentUser);
        return ResponseEntity.ok(ApiResponse.success("Instructors retrieved", instructors));
    }

    @PostMapping("/courses/{id}/instructors")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> assignInstructor(
            @PathVariable Long id,
            @Valid @RequestBody InstructorAssignmentRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.assignInstructor(id, request.getInstructorId(), currentUser);
        return ResponseEntity.ok(ApiResponse.success("Instructor assigned to course", course));
    }

    @DeleteMapping("/courses/{id}/instructors/{instructorId}")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> removeInstructor(
            @PathVariable Long id,
            @PathVariable Long instructorId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        CourseDetailResponse course = adminService.removeInstructor(id, instructorId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Instructor removed from course", course));
    }

    // Module endpoints
    @PostMapping("/courses/{id}/modules")
    public ResponseEntity<ApiResponse<ModuleResponse>> addModule(
            @PathVariable Long id,
            @Valid @RequestBody CreateModuleRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        ModuleResponse module = adminService.addModule(id, request, currentUser);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.success("Module added to course", module));
    }

    @PutMapping("/modules/{moduleId}")
    public ResponseEntity<ApiResponse<ModuleResponse>> updateModule(
            @PathVariable Long moduleId,
            @Valid @RequestBody UpdateModuleRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        ModuleResponse module = adminService.updateModule(moduleId, request, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Module updated", module));
    }

    @DeleteMapping("/modules/{moduleId}")
    public ResponseEntity<ApiResponse<Void>> deleteModule(
            @PathVariable Long moduleId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        adminService.deleteModule(moduleId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Module deleted", null));
    }

    @PutMapping("/courses/{id}/modules/reorder")
    public ResponseEntity<ApiResponse<List<ModuleResponse>>> reorderModules(
            @PathVariable Long id,
            @RequestBody ReorderListRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<ModuleResponse> modules = adminService.reorderModules(id, request.getOrderedIds(), currentUser);
        return ResponseEntity.ok(ApiResponse.success("Modules reordered", modules));
    }

    // Lesson endpoints
    @PostMapping("/modules/{moduleId}/lessons")
    public ResponseEntity<ApiResponse<LessonResponse>> addLesson(
            @PathVariable Long moduleId,
            @Valid @RequestBody CreateLessonRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        LessonResponse lesson = adminService.addLesson(moduleId, request, currentUser);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.success("Lesson added", lesson));
    }

    @PutMapping("/lessons/{lessonId}")
    public ResponseEntity<ApiResponse<LessonResponse>> updateLesson(
            @PathVariable Long lessonId,
            @Valid @RequestBody UpdateLessonRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        LessonResponse lesson = adminService.updateLesson(lessonId, request, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Lesson updated", lesson));
    }

    @DeleteMapping("/lessons/{lessonId}")
    public ResponseEntity<ApiResponse<Void>> deleteLesson(
            @PathVariable Long lessonId,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        adminService.deleteLesson(lessonId, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Lesson deleted", null));
    }

    @PutMapping("/modules/{moduleId}/lessons/reorder")
    public ResponseEntity<ApiResponse<List<LessonResponse>>> reorderLessons(
            @PathVariable Long moduleId,
            @RequestBody ReorderListRequest request,
            @AuthenticationPrincipal UserPrincipal currentUser) {
        List<LessonResponse> lessons = adminService.reorderLessons(moduleId, request.getOrderedIds(), currentUser);
        return ResponseEntity.ok(ApiResponse.success("Lessons reordered", lessons));
    }
}
