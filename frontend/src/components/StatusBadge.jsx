import React from 'react';

/**
 * StatusBadge component showing live backend connectivity status.
 */
export default function StatusBadge({ loading, result, onRetry }) {
  if (loading) {
    return (
      <div className="status-badge status-loading" id="status-badge-loading">
        <span className="pulse-dot dot-amber"></span>
        <span className="badge-text">Checking Backend API...</span>
      </div>
    );
  }

  if (result && result.success) {
    return (
      <div className="status-badge status-online" id="status-badge-online">
        <span className="pulse-dot dot-emerald"></span>
        <span className="badge-text">Backend Online</span>
        <span className="badge-latency">{result.latencyMs}ms</span>
      </div>
    );
  }

  return (
    <div className="status-badge status-offline" id="status-badge-offline">
      <span className="pulse-dot dot-rose"></span>
      <span className="badge-text">Backend Offline</span>
      {onRetry && (
        <button
          onClick={onRetry}
          className="badge-retry-btn"
          id="btn-retry-health"
          title="Retry Connection"
        >
          Retry
        </button>
      )}
    </div>
  );
}
