package com.learnhub.service;

import com.learnhub.dto.DatabaseStatus;
import com.learnhub.dto.DetailedHealthResponse;
import com.learnhub.dto.HealthCheckResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;
import java.time.LocalDateTime;

/**
 * Service providing system and database health status information.
 */
@Service
public class HealthService {

    private static final Logger log = LoggerFactory.getLogger(HealthService.class);

    private final DataSource dataSource;

    @Autowired
    public HealthService(@Autowired(required = false) DataSource dataSource) {
        this.dataSource = dataSource;
    }

    /**
     * Basic application health status for /api/health endpoint.
     */
    public HealthCheckResponse getHealthStatus() {
        return new HealthCheckResponse(
                "UP",
                "LearnHub Skill Learning & Assessment Platform backend is running successfully.",
                "learnhub-backend",
                "0.0.1-SNAPSHOT",
                LocalDateTime.now()
        );
    }

    /**
     * Checks database connectivity using a short timeout validation.
     * Sanitizes all output to ensure no credentials or sensitive URLs leak.
     */
    public DatabaseStatus checkDatabaseConnection() {
        if (dataSource == null) {
            return DatabaseStatus.down("Database DataSource is not configured in application context.");
        }

        try (Connection connection = dataSource.getConnection()) {
            boolean isValid = connection.isValid(2);
            if (isValid) {
                String databaseName = connection.getMetaData().getDatabaseProductName();
                String databaseVersion = connection.getMetaData().getDatabaseProductVersion();
                return DatabaseStatus.up(databaseName, databaseVersion);
            } else {
                return DatabaseStatus.down("Database connection validation timed out or failed.");
            }
        } catch (SQLException e) {
            // Log generic error internally without printing raw passwords or sensitive credentials
            log.warn("Database connectivity check failed: {}", e.getMessage());
            return DatabaseStatus.down("Unable to establish database connection. Verify MySQL service, database name, and credentials.");
        } catch (Exception e) {
            log.warn("Unexpected error during database check: {}", e.getMessage());
            return DatabaseStatus.down("Database connection check encountered an unexpected error.");
        }
    }

    /**
     * Detailed health check reporting application and database status separately.
     */
    public DetailedHealthResponse getDetailedHealthStatus() {
        HealthCheckResponse appStatus = getHealthStatus();
        DatabaseStatus dbStatus = checkDatabaseConnection();

        boolean isDbHealthy = "UP".equalsIgnoreCase(dbStatus.getStatus());
        String overallStatus = isDbHealthy ? "UP" : "DEGRADED";

        return new DetailedHealthResponse(overallStatus, appStatus, dbStatus);
    }
}
