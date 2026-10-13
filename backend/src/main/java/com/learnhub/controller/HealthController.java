package com.learnhub.controller;

import com.learnhub.dto.ApiResponse;
import com.learnhub.dto.DetailedHealthResponse;
import com.learnhub.dto.HealthCheckResponse;
import com.learnhub.service.HealthService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Controller for health check and system status verification.
 */
@RestController
@RequestMapping("/api/health")
public class HealthController {

    private final HealthService healthService;

    public HealthController(HealthService healthService) {
        this.healthService = healthService;
    }

    /**
     * Preserved basic health-check endpoint returning HTTP 200.
     */
    @GetMapping
    public ResponseEntity<HealthCheckResponse> checkHealth() {
        return ResponseEntity.ok(healthService.getHealthStatus());
    }

    /**
     * Detailed status endpoint reporting application and database health separately.
     * Returns HTTP 200 when database is healthy; HTTP 503 when database is unavailable.
     */
    @GetMapping("/status")
    public ResponseEntity<ApiResponse<DetailedHealthResponse>> getStatusDetails() {
        DetailedHealthResponse detailedHealth = healthService.getDetailedHealthStatus();

        boolean isDbHealthy = detailedHealth.getDatabase() != null &&
                "UP".equalsIgnoreCase(detailedHealth.getDatabase().getStatus());

        if (isDbHealthy) {
            return ResponseEntity.ok(ApiResponse.success(
                    "Service and database are operational",
                    detailedHealth
            ));
        } else {
            return ResponseEntity
                    .status(HttpStatus.SERVICE_UNAVAILABLE)
                    .body(new ApiResponse<>(
                            false,
                            "Service is running but database is currently unavailable",
                            detailedHealth
                    ));
        }
    }
}
