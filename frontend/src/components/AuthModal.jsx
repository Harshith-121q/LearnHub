import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/useAuth';
import { ROLES, ROLE_LABELS } from '../utils/constants';

export default function AuthModal({ isOpen, onClose, defaultTab = 'login' }) {
  const { login, register } = useAuth();
  const navigate = useNavigate();
  const [tab, setTab] = useState(defaultTab);
  const [prevDefaultTab, setPrevDefaultTab] = useState(defaultTab);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMsg, setSuccessMsg] = useState(null);

  if (defaultTab !== prevDefaultTab) {
    setPrevDefaultTab(defaultTab);
    setTab(defaultTab);
    setError(null);
    setSuccessMsg(null);
  }

  // Login form state
  const [loginData, setLoginData] = useState({
    usernameOrEmail: '',
    password: '',
  });

  // Register form state
  const [registerData, setRegisterData] = useState({
    fullName: '',
    username: '',
    email: '',
    password: '',
    role: ROLES.STUDENT,
  });

  // Close on Escape key
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape' && isOpen) onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handleRoleRedirect = (role) => {
    if (role === 'ROLE_ADMIN') {
      navigate('/admin/dashboard');
    } else if (role === 'ROLE_INSTRUCTOR') {
      navigate('/instructor/dashboard');
    } else {
      navigate('/student/dashboard');
    }
  };

  const handleLoginSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    if (!loginData.usernameOrEmail.trim() || !loginData.password) {
      setError('Please provide your username or email and password');
      setLoading(false);
      return;
    }

    const result = await login(loginData.usernameOrEmail, loginData.password);
    setLoading(false);

    if (result.success) {
      onClose();
      handleRoleRedirect(result.user?.role);
    } else {
      setError(result.error);
    }
  };

  const handleRegisterSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    if (!registerData.fullName.trim() || !registerData.username.trim() || !registerData.email.trim() || !registerData.password) {
      setError('Please complete all required fields');
      setLoading(false);
      return;
    }

    if (registerData.password.length < 6) {
      setError('Password must be at least 6 characters long');
      setLoading(false);
      return;
    }

    const result = await register(registerData);
    setLoading(false);

    if (result.success) {
      setSuccessMsg('Account created successfully! Redirecting to your workspace...');
      setTimeout(() => {
        onClose();
        handleRoleRedirect(result.user?.role);
      }, 700);
    } else {
      setError(result.error);
    }
  };

  const handleDemoFill = (roleType) => {
    if (roleType === 'ADMIN') {
      setLoginData({
        usernameOrEmail: 'admin',
        password: 'Admin@123',
      });
    } else if (roleType === 'INSTRUCTOR') {
      setLoginData({
        usernameOrEmail: 'instructor_sarah',
        password: 'Password123',
      });
    } else {
      setLoginData({
        usernameOrEmail: 'student_alex',
        password: 'Password123',
      });
    }
    setError(null);
  };

  return (
    <div className="modal-backdrop" onClick={onClose} id="auth-modal-backdrop">
      <div
        className="modal-container"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        id="auth-modal-dialog"
      >
        <button
          className="modal-close-btn"
          onClick={onClose}
          aria-label="Close modal"
          id="btn-close-auth-modal"
        >
          &times;
        </button>

        {/* Modal Header & Tabs */}
        <div className="modal-header">
          <div className="modal-logo-badge">LH</div>
          <h2 className="modal-title">
            {tab === 'login' ? 'Sign in to LearnHub' : 'Join LearnHub Platform'}
          </h2>
          <p className="modal-subtitle">
            {tab === 'login'
              ? 'Access courses, assessments, and track your learning progress.'
              : 'Create an account to start mastering new technical skills.'}
          </p>

          <div className="modal-tabs" role="tablist">
            <button
              className={`tab-btn ${tab === 'login' ? 'active' : ''}`}
              onClick={() => { setTab('login'); setError(null); }}
              type="button"
              id="tab-login"
            >
              Sign In
            </button>
            <button
              className={`tab-btn ${tab === 'register' ? 'active' : ''}`}
              onClick={() => { setTab('register'); setError(null); }}
              type="button"
              id="tab-register"
            >
              Create Account
            </button>
          </div>
        </div>

        {/* Error / Success Feedback */}
        {error && (
          <div className="auth-alert error-alert" id="auth-error-alert">
            <span className="alert-icon">⚠️</span>
            <span>{error}</span>
          </div>
        )}

        {successMsg && (
          <div className="auth-alert success-alert" id="auth-success-alert">
            <span className="alert-icon">✅</span>
            <span>{successMsg}</span>
          </div>
        )}

        {/* Login Form */}
        {tab === 'login' && (
          <form onSubmit={handleLoginSubmit} className="auth-form" id="login-form">
            <div className="form-group">
              <label htmlFor="login-username" className="form-label">Username or Email</label>
              <input
                type="text"
                id="login-username"
                className="form-input"
                placeholder="e.g. harshith or user@example.com"
                value={loginData.usernameOrEmail}
                onChange={(e) => setLoginData({ ...loginData, usernameOrEmail: e.target.value })}
                required
                autoComplete="username"
              />
            </div>

            <div className="form-group">
              <div className="label-with-action">
                <label htmlFor="login-password" className="form-label">Password</label>
                <button
                  type="button"
                  className="text-link-btn"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? 'Hide' : 'Show'}
                </button>
              </div>
              <input
                type={showPassword ? 'text' : 'password'}
                id="login-password"
                className="form-input"
                placeholder="Enter your password"
                value={loginData.password}
                onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
                required
                autoComplete="current-password"
              />
            </div>

            <button
              type="submit"
              className="submit-auth-btn"
              disabled={loading}
              id="btn-submit-login"
            >
              {loading ? 'Authenticating...' : 'Sign In with JWT'}
            </button>

            {/* Demo Quick-Fill Section */}
            <div className="demo-fill-section">
              <span className="demo-fill-label">Quick Test Autofill:</span>
              <div className="demo-fill-chips">
                <button
                  type="button"
                  className="demo-chip"
                  onClick={() => handleDemoFill('STUDENT')}
                >
                  🎓 Demo Student
                </button>
                <button
                  type="button"
                  className="demo-chip"
                  onClick={() => handleDemoFill('INSTRUCTOR')}
                >
                  👨‍🏫 Demo Instructor
                </button>
                <button
                  type="button"
                  className="demo-chip"
                  onClick={() => handleDemoFill('ADMIN')}
                >
                  👑 Demo Admin
                </button>
              </div>
            </div>
          </form>
        )}

        {/* Register Form */}
        {tab === 'register' && (
          <form onSubmit={handleRegisterSubmit} className="auth-form" id="register-form">
            <div className="form-group">
              <label htmlFor="reg-fullname" className="form-label">Full Name</label>
              <input
                type="text"
                id="reg-fullname"
                className="form-input"
                placeholder="e.g. Harshith Kumar"
                value={registerData.fullName}
                onChange={(e) => setRegisterData({ ...registerData, fullName: e.target.value })}
                required
              />
            </div>

            <div className="form-row-2">
              <div className="form-group">
                <label htmlFor="reg-username" className="form-label">Username</label>
                <input
                  type="text"
                  id="reg-username"
                  className="form-input"
                  placeholder="e.g. harshith"
                  value={registerData.username}
                  onChange={(e) => setRegisterData({ ...registerData, username: e.target.value })}
                  required
                  autoComplete="username"
                />
              </div>

              <div className="form-group">
                <label htmlFor="reg-email" className="form-label">Email Address</label>
                <input
                  type="email"
                  id="reg-email"
                  className="form-input"
                  placeholder="you@domain.com"
                  value={registerData.email}
                  onChange={(e) => setRegisterData({ ...registerData, email: e.target.value })}
                  required
                  autoComplete="email"
                />
              </div>
            </div>

            <div className="form-group">
              <div className="label-with-action">
                <label htmlFor="reg-password" className="form-label">Password</label>
                <button
                  type="button"
                  className="text-link-btn"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? 'Hide' : 'Show'}
                </button>
              </div>
              <input
                type={showPassword ? 'text' : 'password'}
                id="reg-password"
                className="form-input"
                placeholder="At least 6 characters"
                value={registerData.password}
                onChange={(e) => setRegisterData({ ...registerData, password: e.target.value })}
                required
                autoComplete="new-password"
              />
            </div>

            {/* Role Selection */}
            <div className="form-group">
              <label className="form-label">Select Learning Role</label>
              <div className="role-selector-grid">
                <button
                  type="button"
                  className={`role-option-card ${registerData.role === ROLES.STUDENT ? 'selected' : ''}`}
                  onClick={() => setRegisterData({ ...registerData, role: ROLES.STUDENT })}
                >
                  <span className="role-icon">🎓</span>
                  <div className="role-info">
                    <span className="role-name">{ROLE_LABELS.ROLE_STUDENT}</span>
                    <span className="role-desc">Enroll in courses &amp; take skill tests</span>
                  </div>
                </button>

                <button
                  type="button"
                  className={`role-option-card ${registerData.role === ROLES.INSTRUCTOR ? 'selected' : ''}`}
                  onClick={() => setRegisterData({ ...registerData, role: ROLES.INSTRUCTOR })}
                >
                  <span className="role-icon">👨‍🏫</span>
                  <div className="role-info">
                    <span className="role-name">{ROLE_LABELS.ROLE_INSTRUCTOR}</span>
                    <span className="role-desc">Publish lessons &amp; author assessments</span>
                  </div>
                </button>
              </div>
            </div>

            <button
              type="submit"
              className="submit-auth-btn"
              disabled={loading}
              id="btn-submit-register"
            >
              {loading ? 'Creating Account...' : 'Complete Registration'}
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
