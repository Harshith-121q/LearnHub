import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { AuthContext } from './authContextValue';
import { authService } from '../services/api';

const TOKEN_KEY = 'learnhub_jwt_token';
const USER_KEY = 'learnhub_user_profile';

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => localStorage.getItem(TOKEN_KEY) || null);
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem(USER_KEY);
    if (!saved) return null;
    try {
      return JSON.parse(saved);
    } catch {
      return null;
    }
  });
  const [loading, setLoading] = useState(() => Boolean(localStorage.getItem(TOKEN_KEY)));

  // Validate session on mount if token exists
  useEffect(() => {
    let active = true;
    const initialToken = localStorage.getItem(TOKEN_KEY);

    if (!initialToken) {
      return;
    }

    authService.getCurrentUser(initialToken).then(res => {
      if (!active) return;
      if (res.success && res.data) {
        setUser(res.data);
        localStorage.setItem(USER_KEY, JSON.stringify(res.data));
      } else {
        // Invalid or expired token
        localStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(USER_KEY);
        setToken(null);
        setUser(null);
      }
      setLoading(false);
    });

    return () => {
      active = false;
    };
  }, []);

  const login = useCallback(async (usernameOrEmail, password) => {
    const res = await authService.login(usernameOrEmail, password);
    if (res.success && res.data) {
      const { token: receivedToken, user: userProfile } = res.data;
      setToken(receivedToken);
      setUser(userProfile);
      localStorage.setItem(TOKEN_KEY, receivedToken);
      localStorage.setItem(USER_KEY, JSON.stringify(userProfile));
      return { success: true, user: userProfile };
    }
    return { success: false, error: res.error || 'Login failed' };
  }, []);

  const register = useCallback(async (registrationData) => {
    const res = await authService.register(registrationData);
    if (res.success && res.data) {
      const { token: receivedToken, user: userProfile } = res.data;
      setToken(receivedToken);
      setUser(userProfile);
      localStorage.setItem(TOKEN_KEY, receivedToken);
      localStorage.setItem(USER_KEY, JSON.stringify(userProfile));
      return { success: true, user: userProfile };
    }
    return { success: false, error: res.error || 'Registration failed' };
  }, []);

  const logout = useCallback(() => {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
    setToken(null);
    setUser(null);
  }, []);

  const value = useMemo(() => ({
    user,
    token,
    isAuthenticated: Boolean(user && token),
    loading,
    login,
    register,
    logout,
  }), [user, token, loading, login, register, logout]);

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}
