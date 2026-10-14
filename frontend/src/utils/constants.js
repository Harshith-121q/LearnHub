/**
 * Application Constants and Configuration
 */

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';
export const APP_NAME = import.meta.env.VITE_APP_NAME || 'LearnHub';
export const APP_VERSION = import.meta.env.VITE_APP_VERSION || '0.0.1';

export const API_ENDPOINTS = {
  HEALTH: `${API_BASE_URL}/health`,
  HEALTH_STATUS: `${API_BASE_URL}/health/status`,
  AUTH_LOGIN: `${API_BASE_URL}/auth/login`,
  AUTH_REGISTER: `${API_BASE_URL}/auth/register`,
  AUTH_ME: `${API_BASE_URL}/auth/me`,
  AUTH_ROLES: `${API_BASE_URL}/auth/roles`,

  // Public courses
  COURSES: `${API_BASE_URL}/courses`,
  COURSE_BY_ID: (id) => `${API_BASE_URL}/courses/${id}`,

  // Admin
  ADMIN_STATS: `${API_BASE_URL}/admin/stats`,
  ADMIN_COURSES: `${API_BASE_URL}/admin/courses`,
  ADMIN_COURSE_BY_ID: (id) => `${API_BASE_URL}/admin/courses/${id}`,
  ADMIN_COURSE_PUBLISH: (id) => `${API_BASE_URL}/admin/courses/${id}/publish`,
  ADMIN_COURSE_UNPUBLISH: (id) => `${API_BASE_URL}/admin/courses/${id}/unpublish`,
  ADMIN_COURSE_ARCHIVE: (id) => `${API_BASE_URL}/admin/courses/${id}/archive`,
  ADMIN_INSTRUCTORS: `${API_BASE_URL}/admin/instructors`,
  ADMIN_COURSE_ASSIGN_INSTRUCTOR: (id) => `${API_BASE_URL}/admin/courses/${id}/instructors`,
  ADMIN_COURSE_REMOVE_INSTRUCTOR: (courseId, instructorId) => `${API_BASE_URL}/admin/courses/${courseId}/instructors/${instructorId}`,
  ADMIN_COURSE_ADD_MODULE: (courseId) => `${API_BASE_URL}/admin/courses/${courseId}/modules`,
  ADMIN_MODULE_UPDATE: (moduleId) => `${API_BASE_URL}/admin/modules/${moduleId}`,
  ADMIN_MODULE_DELETE: (moduleId) => `${API_BASE_URL}/admin/modules/${moduleId}`,
  ADMIN_MODULES_REORDER: (courseId) => `${API_BASE_URL}/admin/courses/${courseId}/modules/reorder`,
  ADMIN_MODULE_ADD_LESSON: (moduleId) => `${API_BASE_URL}/admin/modules/${moduleId}/lessons`,
  ADMIN_LESSON_UPDATE: (lessonId) => `${API_BASE_URL}/admin/lessons/${lessonId}`,
  ADMIN_LESSON_DELETE: (lessonId) => `${API_BASE_URL}/admin/lessons/${lessonId}`,
  ADMIN_LESSONS_REORDER: (moduleId) => `${API_BASE_URL}/admin/modules/${moduleId}/lessons/reorder`,

  // Student
  STUDENT_ENROLLMENTS: `${API_BASE_URL}/student/enrollments`,
  STUDENT_ENROLL: (courseId) => `${API_BASE_URL}/student/courses/${courseId}/enroll`,
  STUDENT_IS_ENROLLED: (courseId) => `${API_BASE_URL}/student/courses/${courseId}/is-enrolled`,
  STUDENT_LEARN: (courseId) => `${API_BASE_URL}/student/courses/${courseId}/learn`,
  STUDENT_LESSON_COMPLETE: (lessonId) => `${API_BASE_URL}/student/lessons/${lessonId}/complete`,
  STUDENT_LESSON_UNCOMPLETE: (lessonId) => `${API_BASE_URL}/student/lessons/${lessonId}/uncomplete`,
  STUDENT_LESSON_OPENED: (lessonId) => `${API_BASE_URL}/student/lessons/${lessonId}/opened`,

  // Instructor
  INSTRUCTOR_COURSES: `${API_BASE_URL}/instructor/courses`,
  INSTRUCTOR_COURSE_BY_ID: (id) => `${API_BASE_URL}/instructor/courses/${id}`,
  INSTRUCTOR_COURSE_STUDENTS: (id) => `${API_BASE_URL}/instructor/courses/${id}/students`,
  INSTRUCTOR_STUDENT_PROGRESS: (courseId, studentId) => `${API_BASE_URL}/instructor/courses/${courseId}/students/${studentId}`,
};

export const ROLES = {
  STUDENT: 'ROLE_STUDENT',
  INSTRUCTOR: 'ROLE_INSTRUCTOR',
  ADMIN: 'ROLE_ADMIN',
};

export const ROLE_LABELS = {
  ROLE_STUDENT: 'Student',
  ROLE_INSTRUCTOR: 'Instructor',
  ROLE_ADMIN: 'Administrator',
};
