package com.learnhub.controller;

import com.learnhub.dto.ApiResponse;
import com.learnhub.dto.CourseDetailResponse;
import com.learnhub.dto.CourseSummaryResponse;
import com.learnhub.dto.PageResponse;
import com.learnhub.entity.DifficultyLevel;
import com.learnhub.security.UserPrincipal;
import com.learnhub.service.CourseService;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * REST Controller for public course catalog discovery and course outline inspection.
 */
@RestController
@RequestMapping("/api/courses")
public class CourseController {

    private final CourseService courseService;

    public CourseController(CourseService courseService) {
        this.courseService = courseService;
    }

    /**
     * Searches published courses with optional filtering and pagination.
     */
    @GetMapping
    public ResponseEntity<ApiResponse<PageResponse<CourseSummaryResponse>>> getPublishedCourses(
            @RequestParam(required = false) String search,
            @RequestParam(required = false) String category,
            @RequestParam(required = false) DifficultyLevel difficulty,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "12") int size,
            @RequestParam(defaultValue = "createdAt,desc") String sort) {

        String[] sortParams = sort.split(",");
        String property = sortParams[0];
        Sort.Direction direction = sortParams.length > 1 && sortParams[1].equalsIgnoreCase("asc")
                ? Sort.Direction.ASC : Sort.Direction.DESC;

        Pageable pageable = PageRequest.of(page, size, Sort.by(direction, property));
        PageResponse<CourseSummaryResponse> response = courseService.searchPublishedCourses(search, category, difficulty, pageable);

        return ResponseEntity.ok(ApiResponse.success("Published courses retrieved successfully", response));
    }

    /**
     * Retrieves course details by ID. Published courses are accessible publicly.
     */
    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<CourseDetailResponse>> getCourseById(
            @PathVariable Long id,
            @AuthenticationPrincipal UserPrincipal currentUser) {

        CourseDetailResponse course = courseService.getCourseById(id, currentUser);
        return ResponseEntity.ok(ApiResponse.success("Course details retrieved successfully", course));
    }
}
