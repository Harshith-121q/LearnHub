import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/useAuth';
import { ROLE_LABELS } from '../utils/constants';

export default function UserDashboardBanner({ onOpenAuth }) {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  if (!isAuthenticated || !user) {
    return (
      <div className="auth-hero-cta-card" id="auth-guest-cta">
        <div className="cta-content">
          <div className="cta-icon-badge">🎓</div>
          <div>
            <h3 className="cta-title">Begin Your Structured Learning Journey</h3>
            <p className="cta-desc">
              Enroll in complete Java and Python programming courses, follow structured step-by-step modules, and monitor your persistent progress.
            </p>
          </div>
        </div>
        <div className="cta-actions">
          <button
            className="cta-btn cta-btn-primary"
            onClick={() => onOpenAuth('register')}
            id="btn-hero-register"
          >
            Create Student Account
          </button>
          <button
            className="cta-btn cta-btn-secondary"
            onClick={() => onOpenAuth('login')}
            id="btn-hero-login"
          >
            Sign In to Platform
          </button>
        </div>
      </div>
    );
  }

  const roleLabel = ROLE_LABELS[user.role] || user.role;
  const isAdmin = user.role === 'ROLE_ADMIN';
  const isInstructor = user.role === 'ROLE_INSTRUCTOR';

  const handlePortalNavigate = () => {
    if (isAdmin) navigate('/admin/dashboard');
    else if (isInstructor) navigate('/instructor/dashboard');
    else navigate('/student/dashboard');
  };

  return (
    <div className="auth-dashboard-banner" id="user-dashboard-banner">
      <div className="banner-top-row">
        <div className="user-greeting">
          <div className="greeting-avatar">
            {user.fullName ? user.fullName[0].toUpperCase() : 'U'}
          </div>
          <div>
            <div className="greeting-pill">
              <span className="live-dot"></span>
              <span>Active Workspace &bull; {roleLabel}</span>
            </div>
            <h2 className="greeting-name">
              Welcome back, <span className="gold-text">{user.fullName}</span>!
            </h2>
            <p className="greeting-sub">
              Logged in as <strong>@{user.username}</strong> &bull; {user.email}
            </p>
          </div>
        </div>

        <div className="banner-status-badge">
          <button
            onClick={handlePortalNavigate}
            className="cta-btn cta-btn-primary"
            style={{ padding: '0.5rem 1.25rem', fontSize: '0.875rem' }}
            id="btn-banner-dashboard"
          >
            {isAdmin ? '👑 Admin Portal' : isInstructor ? '👨‍🏫 Instructor Portal' : '🎓 My Learning Portal'} &rarr;
          </button>
          <button
            onClick={logout}
            className="banner-logout-btn"
            id="btn-banner-logout"
          >
            Sign Out
          </button>
        </div>
      </div>

      {/* Role-Specific Action Cards Grid */}
      <div className="dashboard-actions-grid">
        {isAdmin && (
          <>
            <div className="action-card" onClick={() => navigate('/admin/courses')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">🛠️</div>
              <div className="action-info">
                <h4 className="action-title">Course Management</h4>
                <p className="action-desc">Create, publish, edit, and organize Java &amp; Python courses</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
            <div className="action-card" onClick={() => navigate('/admin/courses')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">📖</div>
              <div className="action-info">
                <h4 className="action-title">Modules &amp; Lessons</h4>
                <p className="action-desc">Add code examples, explanations, and structure topics</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
            <div className="action-card" onClick={() => navigate('/admin/instructors')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">👥</div>
              <div className="action-info">
                <h4 className="action-title">Instructor Assignments</h4>
                <p className="action-desc">Assign qualified instructors to oversee course participation</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
          </>
        )}

        {isInstructor && (
          <>
            <div className="action-card" onClick={() => navigate('/instructor/dashboard')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">📚</div>
              <div className="action-info">
                <h4 className="action-title">Assigned Courses</h4>
                <p className="action-desc">Access complete curriculum of courses assigned to you</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
            <div className="action-card" onClick={() => navigate('/instructor/dashboard')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">👥</div>
              <div className="action-info">
                <h4 className="action-title">Enrolled Students</h4>
                <p className="action-desc">Monitor student enrollment and cohort activity</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
            <div className="action-card" onClick={() => navigate('/instructor/dashboard')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">📊</div>
              <div className="action-info">
                <h4 className="action-title">Participation Metrics</h4>
                <p className="action-desc">Track class engagement across assigned modules</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
          </>
        )}

        {!isAdmin && !isInstructor && (
          <>
            <div className="action-card" onClick={() => navigate('/student/dashboard')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">📚</div>
              <div className="action-info">
                <h4 className="action-title">My Enrolled Courses</h4>
                <p className="action-desc">Access your ongoing Java and Python courses</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
            <div className="action-card" onClick={() => navigate('/student/dashboard')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">▶️</div>
              <div className="action-info">
                <h4 className="action-title">Resume Learning</h4>
                <p className="action-desc">Continue from your latest completed lesson</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
            <div className="action-card" onClick={() => navigate('/student/dashboard')} style={{ cursor: 'pointer' }}>
              <div className="action-icon">📈</div>
              <div className="action-info">
                <h4 className="action-title">Learning Progress</h4>
                <p className="action-desc">Review your verified completion percentage</p>
              </div>
              <button className="action-arrow-btn">&rarr;</button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
