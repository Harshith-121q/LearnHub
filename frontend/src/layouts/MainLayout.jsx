import React from 'react';
import { useTheme } from '../context/ThemeContext';
import StatusBadge from '../components/StatusBadge';
import { useHealthCheck } from '../hooks/useHealthCheck';
import { APP_NAME } from '../utils/constants';

/**
 * Main layout providing top navigation bar and footer.
 */
export default function MainLayout({ children }) {
  const { theme, toggleTheme } = useTheme();
  const { result, loading, refresh } = useHealthCheck();

  return (
    <div className="app-container" data-theme={theme}>
      {/* Navigation Header */}
      <header className="app-header">
        <div className="header-inner">
          <div className="brand-logo" id="brand-logo">
            <div className="logo-symbol">LH</div>
            <div className="brand-text">
              <span className="brand-title">{APP_NAME}</span>
              <span className="brand-tag">Platform</span>
            </div>
          </div>

          <div className="header-actions">
            <StatusBadge loading={loading} result={result} onRetry={refresh} />
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
        {React.cloneElement(children, { healthResult: result, healthLoading: loading, onRefreshHealth: refresh })}
      </main>

      {/* Footer */}
      <footer className="app-footer">
        <div className="footer-inner">
          <p className="footer-text">
            &copy; {new Date().getFullYear()} <strong>LearnHub</strong> &mdash; Skill Learning &amp; Assessment Platform. All rights reserved.
          </p>
          <div className="footer-meta">
            <span className="meta-tag">Java Full Stack</span>
            <span className="meta-separator">&bull;</span>
            <span className="meta-tag">Spring Boot 3</span>
            <span className="meta-separator">&bull;</span>
            <span className="meta-tag">React + Vite</span>
          </div>
        </div>
      </footer>
    </div>
  );
}
