package com.learnhub.dto;

import java.time.LocalDateTime;

/**
 * Data Transfer Object reporting application server and database health states separately.
 */
public class DetailedHealthResponse {

    private String status; // "UP" when both healthy, "DEGRADED" when database is unavailable
    private HealthCheckResponse application;
    private DatabaseStatus database;
    private LocalDateTime timestamp;

    public DetailedHealthResponse() {
        this.timestamp = LocalDateTime.now();
    }

    public DetailedHealthResponse(String status, HealthCheckResponse application, DatabaseStatus database) {
        this.status = status;
        this.application = application;
        this.database = database;
        this.timestamp = LocalDateTime.now();
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public HealthCheckResponse getApplication() {
        return application;
    }

    public void setApplication(HealthCheckResponse application) {
        this.application = application;
    }

    public DatabaseStatus getDatabase() {
        return database;
    }

    public void setDatabase(DatabaseStatus database) {
        this.database = database;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
