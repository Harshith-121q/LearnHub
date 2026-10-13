package com.learnhub.controller;

import com.learnhub.dto.DatabaseStatus;
import com.learnhub.dto.DetailedHealthResponse;
import com.learnhub.dto.HealthCheckResponse;
import com.learnhub.service.HealthService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import java.time.LocalDateTime;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Unit tests for HealthController verifying /api/health and /api/health/status.
 * Uses standalone MockMvc to test HTTP contracts independently of local MySQL instances.
 */
class HealthControllerTest {

    private MockMvc mockMvc;
    private StubHealthService stubHealthService;

    static class StubHealthService extends HealthService {
        private DetailedHealthResponse detailedResponse;

        public StubHealthService() {
            super(null);
        }

        public void setDetailedResponse(DetailedHealthResponse detailedResponse) {
            this.detailedResponse = detailedResponse;
        }

        @Override
        public HealthCheckResponse getHealthStatus() {
            return new HealthCheckResponse(
                    "UP",
                    "LearnHub backend is running",
                    "learnhub-backend",
                    "0.0.1-SNAPSHOT",
                    LocalDateTime.now()
            );
        }

        @Override
        public DetailedHealthResponse getDetailedHealthStatus() {
            return detailedResponse;
        }
    }

    @BeforeEach
    void setUp() {
        stubHealthService = new StubHealthService();
        mockMvc = MockMvcBuilders.standaloneSetup(new HealthController(stubHealthService)).build();
    }

    @Test
    @DisplayName("GET /api/health returns HTTP 200 and application health status")
    void testBasicHealthEndpointReturns200() throws Exception {
        mockMvc.perform(get("/api/health").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.status").value("UP"))
                .andExpect(jsonPath("$.service").value("learnhub-backend"));
    }

    @Test
    @DisplayName("GET /api/health/status returns HTTP 200 when database is healthy")
    void testDetailedHealthEndpointReturns200WhenDbUp() throws Exception {
        HealthCheckResponse appStatus = new HealthCheckResponse("UP", "OK", "learnhub-backend", "0.0.1", LocalDateTime.now());
        DatabaseStatus dbStatus = DatabaseStatus.up("MySQL", "8.0.44");
        DetailedHealthResponse detailed = new DetailedHealthResponse("UP", appStatus, dbStatus);

        stubHealthService.setDetailedResponse(detailed);

        mockMvc.perform(get("/api/health/status").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.success").value(true))
                .andExpect(jsonPath("$.data.status").value("UP"))
                .andExpect(jsonPath("$.data.application.status").value("UP"))
                .andExpect(jsonPath("$.data.database.status").value("UP"))
                .andExpect(jsonPath("$.data.database.database").value("MySQL"));
    }

    @Test
    @DisplayName("GET /api/health/status returns HTTP 503 when database is unavailable without leaking secrets")
    void testDetailedHealthEndpointReturns503WhenDbDown() throws Exception {
        HealthCheckResponse appStatus = new HealthCheckResponse("UP", "OK", "learnhub-backend", "0.0.1", LocalDateTime.now());
        DatabaseStatus dbStatus = DatabaseStatus.down("Unable to establish database connection.");
        DetailedHealthResponse detailed = new DetailedHealthResponse("DEGRADED", appStatus, dbStatus);

        stubHealthService.setDetailedResponse(detailed);

        mockMvc.perform(get("/api/health/status").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isServiceUnavailable())
                .andExpect(jsonPath("$.success").value(false))
                .andExpect(jsonPath("$.data.status").value("DEGRADED"))
                .andExpect(jsonPath("$.data.application.status").value("UP"))
                .andExpect(jsonPath("$.data.database.status").value("DOWN"))
                .andExpect(jsonPath("$.data.database.password").doesNotExist())
                .andExpect(jsonPath("$.data.database.url").doesNotExist());
    }
}
