import { API_ENDPOINTS } from '../utils/constants';

/**
 * Service to communicate with the Spring Boot backend REST APIs.
 */
export const healthService = {
  /**
   * Fetches backend health check info from /api/health
   */
  async checkHealth() {
    const startTime = performance.now();
    try {
      const response = await fetch(API_ENDPOINTS.HEALTH, {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
        },
      });

      const latencyMs = Math.round(performance.now() - startTime);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();
      return {
        success: true,
        statusCode: response.status,
        latencyMs,
        data,
      };
    } catch (error) {
      const latencyMs = Math.round(performance.now() - startTime);
      return {
        success: false,
        statusCode: 0,
        latencyMs,
        error: error.message || 'Unable to connect to backend service',
      };
    }
  },

  /**
   * Fetches detailed application & database health status from /api/health/status
   */
  async getHealthStatus() {
    try {
      const response = await fetch(API_ENDPOINTS.HEALTH_STATUS, {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
        },
      });

      const json = await response.json();
      return {
        statusCode: response.status,
        ...json,
      };
    } catch (error) {
      return {
        success: false,
        statusCode: 0,
        message: error.message || 'Failed to fetch status details',
        data: null,
      };
    }
  },
};
