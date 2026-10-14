import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import ProtectedRoute from './ProtectedRoute';

// Public pages
import LandingPage from '../pages/LandingPage';
import CourseCatalogPage from '../pages/public/CourseCatalogPage';
import CourseDetailPage from '../pages/public/CourseDetailPage';

// Admin pages
import AdminDashboardPage from '../pages/admin/AdminDashboardPage';
import AdminCoursesPage from '../pages/admin/AdminCoursesPage';
import CourseCurriculumEditorPage from '../pages/admin/CourseCurriculumEditorPage';
import InstructorAssignmentPage from '../pages/admin/InstructorAssignmentPage';

// Instructor pages
import InstructorDashboardPage from '../pages/instructor/InstructorDashboardPage';
import AssignedCourseDetailPage from '../pages/instructor/AssignedCourseDetailPage';
import EnrolledStudentsPage from '../pages/instructor/EnrolledStudentsPage';
import StudentProgressPage from '../pages/instructor/StudentProgressPage';

// Student pages
import StudentDashboardPage from '../pages/student/StudentDashboardPage';
import LearningPage from '../pages/student/LearningPage';

/**
 * AppRoutes component centralizing all route declarations and role protections.
 */
export default function AppRoutes({ onOpenAuth }) {
  return (
    <Routes>
      {/* Public Pages */}
      <Route path="/" element={<LandingPage onOpenAuth={onOpenAuth} />} />
      <Route path="/courses" element={<CourseCatalogPage onOpenAuth={onOpenAuth} />} />
      <Route path="/courses/:id" element={<CourseDetailPage onOpenAuth={onOpenAuth} />} />

      {/* Admin Protected Routes */}
      <Route
        path="/admin/dashboard"
        element={
          <ProtectedRoute allowedRole="ROLE_ADMIN">
            <AdminDashboardPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/admin/courses"
        element={
          <ProtectedRoute allowedRole="ROLE_ADMIN">
            <AdminCoursesPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/admin/courses/:id/curriculum"
        element={
          <ProtectedRoute allowedRole="ROLE_ADMIN">
            <CourseCurriculumEditorPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/admin/instructors"
        element={
          <ProtectedRoute allowedRole="ROLE_ADMIN">
            <InstructorAssignmentPage />
          </ProtectedRoute>
        }
      />

      {/* Instructor Protected Routes */}
      <Route
        path="/instructor/dashboard"
        element={
          <ProtectedRoute allowedRole="ROLE_INSTRUCTOR">
            <InstructorDashboardPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/instructor/courses/:id"
        element={
          <ProtectedRoute allowedRole="ROLE_INSTRUCTOR">
            <AssignedCourseDetailPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/instructor/courses/:id/students"
        element={
          <ProtectedRoute allowedRole="ROLE_INSTRUCTOR">
            <EnrolledStudentsPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/instructor/courses/:id/students/:studentId"
        element={
          <ProtectedRoute allowedRole="ROLE_INSTRUCTOR">
            <StudentProgressPage />
          </ProtectedRoute>
        }
      />

      {/* Student Protected Routes */}
      <Route
        path="/student/dashboard"
        element={
          <ProtectedRoute allowedRole="ROLE_STUDENT">
            <StudentDashboardPage />
          </ProtectedRoute>
        }
      />
      <Route
        path="/student/courses/:id/learn"
        element={
          <ProtectedRoute allowedRole="ROLE_STUDENT">
            <LearningPage />
          </ProtectedRoute>
        }
      />

      {/* Catch-all fallback */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
