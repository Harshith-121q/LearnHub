import React, { useEffect, useState } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';
import { useAuth } from '../context/useAuth';
import { ROLE_LABELS } from '../utils/constants';

/**
 * Route guard enforcing strict role boundaries.
 * Unauthorized attempts display a warning and redirect to the user's appropriate role dashboard.
 */
export default function ProtectedRoute({ allowedRole, children }) {
  const { user, isAuthenticated, loading } = useAuth();
  const navigate = useNavigate();
  const [countdown, setCountdown] = useState(3);

  const getAuthorizedDashboard = (role) => {
    if (role === 'ROLE_ADMIN') return '/admin/dashboard';
    if (role === 'ROLE_INSTRUCTOR') return '/instructor/dashboard';
    return '/student/dashboard';
  };

  useEffect(() => {
    if (!loading && isAuthenticated && user && user.role !== allowedRole) {
      const timer = setInterval(() => {
        setCountdown((prev) => {
          if (prev <= 1) {
            clearInterval(timer);
            navigate(getAuthorizedDashboard(user.role), { replace: true });
            return 0;
          }
          return prev - 1;
        });
      }, 1000);

      return () => clearInterval(timer);
    }
  }, [loading, isAuthenticated, user, allowedRole, navigate]);

  if (loading) {
    return (
      <div className="section-container" style={{ padding: '6rem 2rem', textAlign: 'center' }}>
        <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
        <p style={{ color: 'var(--text-muted)' }}>Validating credentials and authorization...</p>
      </div>
    );
  }

  if (!isAuthenticated || !user) {
    return <Navigate to="/" replace state={{ openAuth: true }} />;
  }

  if (user.role !== allowedRole) {
    const userRoleName = ROLE_LABELS[user.role] || user.role;
    const requiredRoleName = ROLE_LABELS[allowedRole] || allowedRole;
    const targetDashboard = getAuthorizedDashboard(user.role);

    return (
      <div className="section-container" style={{ padding: '4rem 2rem' }}>
        <div
          className="admin-card"
          style={{
            maxWidth: 640,
            margin: '0 auto',
            border: '1px solid rgba(239, 68, 68, 0.4)',
            background: 'linear-gradient(135deg, rgba(239, 68, 68, 0.08) 0%, rgba(11, 19, 43, 0.95) 100%)',
            textAlign: 'center',
            padding: '3rem 2rem',
          }}
        >
          <div style={{ fontSize: '3rem', marginBottom: '1rem' }}>🛡️</div>
          <h2 style={{ fontFamily: 'var(--font-serif)', color: '#f87171', marginBottom: '0.75rem' }}>
            Access Restricted
          </h2>
          <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: '1.5rem' }}>
            You are logged in as <strong>{userRoleName}</strong>. This section is strictly reserved for{' '}
            <strong>{requiredRoleName}</strong> accounts.
          </p>
          <div
            style={{
              padding: '0.75rem 1.25rem',
              background: 'rgba(239, 68, 68, 0.15)',
              borderRadius: '8px',
              color: '#fca5a5',
              fontSize: '0.875rem',
              marginBottom: '2rem',
              display: 'inline-block',
            }}
          >
            ⚠️ Redirecting to your authorized dashboard in <strong>{countdown}s</strong>...
          </div>
          <div>
            <button
              onClick={() => navigate(targetDashboard, { replace: true })}
              className="cta-btn cta-btn-primary"
              id="btn-return-authorized-dashboard"
            >
              Go to {userRoleName} Dashboard Now &rarr;
            </button>
          </div>
        </div>
      </div>
    );
  }

  return children;
}
