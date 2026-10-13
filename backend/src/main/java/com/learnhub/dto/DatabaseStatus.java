package com.learnhub.dto;

/**
 * Data Transfer Object representing database connectivity and health state.
 * Never includes credentials, connection strings, or sensitive information.
 */
public class DatabaseStatus {

    private String status;
    private String message;
    private String database;
    private String version;

    public DatabaseStatus() {
    }

    public DatabaseStatus(String status, String message) {
        this.status = status;
        this.message = message;
    }

    public DatabaseStatus(String status, String message, String database, String version) {
        this.status = status;
        this.message = message;
        this.database = database;
        this.version = version;
    }

    public static DatabaseStatus up(String database, String version) {
        return new DatabaseStatus("UP", "Database connection successful", database, version);
    }

    public static DatabaseStatus down(String message) {
        return new DatabaseStatus("DOWN", message, null, null);
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

    public String getDatabase() {
        return database;
    }

    public void setDatabase(String database) {
        this.database = database;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
}
