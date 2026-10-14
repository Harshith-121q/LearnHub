import React, { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/useAuth';
import { ROLE_LABELS } from '../utils/constants';

export default function UserProfileBadge({ onOpenAuth }) {
  const { user, isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownRef = useRef(null);

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
        setDropdownOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  if (!isAuthenticated || !user) {
    return (
      <div className="auth-nav-buttons" id="guest-nav-actions">
        <button
          className="nav-btn nav-btn-outline"
          onClick={() => onOpenAuth('login')}
          id="btn-nav-signin"
        >
          Sign In
        </button>
        <button
          className="nav-btn nav-btn-primary"
          onClick={() => onOpenAuth('register')}
          id="btn-nav-register"
        >
          Get Started
        </button>
      </div>
    );
  }

  const initials = user.fullName
    ? user.fullName
        .split(' ')
        .map(n => n[0])
        .slice(0, 2)
        .join('')
        .toUpperCase()
    : user.username.slice(0, 2).toUpperCase();

  const roleLabel = ROLE_LABELS[user.role] || user.role;

  return (
    <div className="user-profile-wrapper" ref={dropdownRef} id="user-profile-menu">
      <button
        className="user-profile-trigger"
        onClick={() => setDropdownOpen(!dropdownOpen)}
        aria-expanded={dropdownOpen}
        id="btn-profile-dropdown"
      >
        <div className="user-avatar-circle">{initials}</div>
        <div className="user-info-text">
          <span className="user-display-name">{user.fullName || user.username}</span>
          <span className="user-role-badge">{roleLabel}</span>
        </div>
        <span className="chevron-arrow">{dropdownOpen ? '▲' : '▼'}</span>
      </button>

      {dropdownOpen && (
        <div className="profile-dropdown-menu" id="profile-dropdown-content">
          <div className="dropdown-user-header">
            <p className="dropdown-user-name">{user.fullName}</p>
            <p className="dropdown-user-handle">@{user.username}</p>
            <p className="dropdown-user-email">{user.email}</p>
            <span className="dropdown-role-chip">{roleLabel}</span>
          </div>

          <div className="dropdown-divider"></div>

          <div className="dropdown-items-group">
            <button
              className="dropdown-action-btn"
              onClick={() => {
                setDropdownOpen(false);
                if (user.role === 'ROLE_ADMIN') navigate('/admin/dashboard');
                else if (user.role === 'ROLE_INSTRUCTOR') navigate('/instructor/dashboard');
                else navigate('/student/dashboard');
              }}
              style={{
                width: '100%',
                padding: '0.65rem 1rem',
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem',
                background: 'rgba(197, 155, 39, 0.12)',
                border: '1px solid rgba(197, 155, 39, 0.25)',
                borderRadius: '6px',
                color: 'var(--gold-primary)',
                fontWeight: 600,
                fontSize: '0.85rem',
                cursor: 'pointer',
                marginBottom: '0.5rem',
              }}
              id="btn-profile-go-dashboard"
            >
              <span>{user.role === 'ROLE_ADMIN' ? '👑' : user.role === 'ROLE_INSTRUCTOR' ? '👨‍🏫' : '🎓'}</span>
              <span>Open {roleLabel} Portal &rarr;</span>
            </button>

            <div className="dropdown-meta-item">
              <span className="meta-item-label">Status</span>
              <span className="meta-item-value text-success">● Active Session</span>
            </div>
            <div className="dropdown-meta-item">
              <span className="meta-item-label">Auth Method</span>
              <span className="meta-item-value">Spring Security JWT</span>
            </div>
          </div>

          <div className="dropdown-divider"></div>

          <button
            className="dropdown-action-btn logout-btn"
            onClick={() => {
              setDropdownOpen(false);
              logout();
            }}
            id="btn-logout"
          >
            <span>🚪</span>
            <span>Sign Out</span>
          </button>
        </div>
      )}
    </div>
  );
}
