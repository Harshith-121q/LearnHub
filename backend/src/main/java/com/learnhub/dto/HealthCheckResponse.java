package com.learnhub.dto;

import java.time.LocalDateTime;

/**
 * Data Transfer Object for health check endpoint response.
 */
public class HealthCheckResponse {

    private String status;
    private String message;
    private String service;
    private String version;
    private LocalDateTime timestamp;

    public HealthCheckResponse() {
    }

    public HealthCheckResponse(String status, String message, String service, String version, LocalDateTime timestamp) {
        this.status = status;
        this.message = message;
        this.service = service;
        this.version = version;
        this.timestamp = timestamp;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
