package com.learnhub.exception;

/**
 * Exception thrown when a client request contains invalid or conflicting business arguments.
 */
public class BadRequestException extends RuntimeException {

    public BadRequestException(String message) {
        super(message);
    }
}
