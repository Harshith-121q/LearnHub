import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useTheme } from '../context/useTheme';
import { useAuth } from '../context/useAuth';
import UserProfileBadge from '../components/UserProfileBadge';
import AuthModal from '../components/AuthModal';
import { APP_NAME } from '../utils/constants';

const CURRENT_YEAR = new Date().getFullYear();

/**
 * Main layout providing top navigation bar, luxury styling, and footer.
 */
export default function MainLayout({ children }) {
  const { theme, toggleTheme } = useTheme();
  const { isAuthenticated, user } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [authModalTab, setAuthModalTab] = useState('login');

  const handleOpenAuth = (tab = 'login') => {
    setAuthModalTab(tab);
    setAuthModalOpen(true);
  };

  const scrollToSection = (id) => {
    if (location.pathname !== '/') {
      navigate('/');
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
      return;
    }
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const role = user?.role;

  return (
    <div className="app-container" data-theme={theme}>
      {/* Prosperum-style Luxury Navigation Header */}
      <header className="app-header prosperum-header">
        <div className="header-inner">
          <div className="brand-logo" id="brand-logo" onClick={() => navigate('/')} style={{ cursor: 'pointer' }}>
            <div className="logo-symbol-gold">LH</div>
            <div className="brand-text">
              <span className="brand-title-luxury">{APP_NAME}</span>
            </div>
          </div>

          {/* Central Nav Links */}
          <nav className="header-nav-links">
            <button
              onClick={() => navigate('/')}
              className={`nav-link-btn ${location.pathname === '/' ? 'active' : ''}`}
            >
              Home
            </button>
            <button
              onClick={() => navigate('/courses')}
              className={`nav-link-btn ${location.pathname.startsWith('/courses') ? 'active' : ''}`}
            >
              Browse Tracks
            </button>

            {role === 'ROLE_ADMIN' && (
              <button
                onClick={() => navigate('/admin/dashboard')}
                className={`nav-link-btn ${location.pathname.startsWith('/admin') ? 'active' : ''}`}
                style={{ color: 'var(--gold-primary)', fontWeight: 600 }}
              >
                👑 Admin Portal
              </button>
            )}

            {role === 'ROLE_INSTRUCTOR' && (
              <button
                onClick={() => navigate('/instructor/dashboard')}
                className={`nav-link-btn ${location.pathname.startsWith('/instructor') ? 'active' : ''}`}
                style={{ color: 'var(--gold-primary)', fontWeight: 600 }}
              >
                👨‍🏫 Faculty Portal
              </button>
            )}

            {role === 'ROLE_STUDENT' && (
              <button
                onClick={() => navigate('/student/dashboard')}
                className={`nav-link-btn ${location.pathname.startsWith('/student') ? 'active' : ''}`}
                style={{ color: 'var(--gold-primary)', fontWeight: 600 }}
              >
                🎓 My Learning
              </button>
            )}
          </nav>

          <div className="header-actions">
            {!isAuthenticated && (
              <button
                onClick={() => handleOpenAuth('register')}
                className="btn-gold-header"
                id="btn-header-cta"
              >
                Start Learning
              </button>
            )}

            <UserProfileBadge onOpenAuth={handleOpenAuth} />

            <button
              onClick={toggleTheme}
              className="theme-toggle-btn"
              id="theme-toggle-btn"
              aria-label="Toggle Dark/Light Mode"
              title={`Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`}
            >
              {theme === 'dark' ? '☀️' : '🌙'}
            </button>
          </div>
        </div>
      </header>

      {/* Main Page Content */}
      <main className="main-content">
        {React.cloneElement(children, {
          onOpenAuth: handleOpenAuth,
        })}
      </main>

      {/* Auth Modal (Sign In / Register) */}
      <AuthModal
        isOpen={authModalOpen}
        onClose={() => setAuthModalOpen(false)}
        defaultTab={authModalTab}
      />

      {/* Luxury Footer matching Prosperum styling */}
      <footer className="app-footer prosperum-footer">
        <div className="footer-inner">
          <div className="footer-top-row">
            <div className="footer-brand-col">
              <div className="logo-symbol-gold">LH</div>
              <h3 className="footer-brand-title">LEARNHUB</h3>
              <p className="footer-tagline">
                Enterprise programming platform delivering verified, structured step-by-step curricula in Java and Python with persistent progress tracking.
              </p>
            </div>

            <div className="footer-links-grid">
              <div className="footer-col">
                <span className="footer-col-title">Curriculum</span>
                <button onClick={() => scrollToSection('solutions-section')} className="footer-link">Java Programming</button>
                <button onClick={() => scrollToSection('solutions-section')} className="footer-link">Python Programming</button>
                <button onClick={() => scrollToSection('solutions-section')} className="footer-link">Full-Stack Architecture</button>
              </div>

              <div className="footer-col">
                <span className="footer-col-title">Platform</span>
                <button onClick={() => scrollToSection('how-we-work-section')} className="footer-link">How We Work</button>
                <button onClick={() => handleOpenAuth('login')} className="footer-link">Student Login</button>
                <button onClick={() => handleOpenAuth('register')} className="footer-link">Create Account</button>
              </div>

              <div className="footer-col">
                <span className="footer-col-title">Roles</span>
                <span className="footer-text-muted">Administrator</span>
                <span className="footer-text-muted">Assigned Instructor</span>
                <span className="footer-text-muted">Enrolled Student</span>
              </div>
            </div>
          </div>

          <div className="footer-bottom-divider"></div>

          <div className="footer-bottom-row">
            <p className="footer-copy">
              &copy; {CURRENT_YEAR} <strong>LearnHub</strong>. All rights reserved.
            </p>
            <div className="footer-tech-tags">
              <span className="gold-bullet">&bull;</span>
              <span>Java 17 &bull; Spring Boot 3 &bull; React &bull; MySQL</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
