import { useState, useEffect, useCallback } from 'react';
import { healthService } from '../services/api';

/**
 * Custom React hook for checking and tracking backend health connectivity.
 */
export function useHealthCheck() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [lastChecked, setLastChecked] = useState(null);

  const performCheck = useCallback(async () => {
    setLoading(true);
    const res = await healthService.checkHealth();
    setResult(res);
    setLoading(false);
    setLastChecked(new Date().toLocaleTimeString());
  }, []);

  useEffect(() => {
    let active = true;
    healthService.checkHealth().then(res => {
      if (active) {
        setResult(res);
        setLoading(false);
        setLastChecked(new Date().toLocaleTimeString());
      }
    });
    return () => {
      active = false;
    };
  }, []);

  return {
    result,
    loading,
    lastChecked,
    refresh: performCheck,
  };
}
