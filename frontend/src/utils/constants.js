/**
 * Application Constants and Configuration
 */

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8080/api';
export const APP_NAME = import.meta.env.VITE_APP_NAME || 'LearnHub';
export const APP_VERSION = import.meta.env.VITE_APP_VERSION || '0.0.1';

export const API_ENDPOINTS = {
  HEALTH: `${API_BASE_URL}/health`,
  HEALTH_STATUS: `${API_BASE_URL}/health/status`,
};
