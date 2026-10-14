import { API_ENDPOINTS } from '../utils/constants';

/**
 * Helper to make authenticated or public API calls.
 */
async function fetchApi(url, options = {}) {
  const token = localStorage.getItem('learnhub_jwt_token');
  const headers = {
    'Accept': 'application/json',
    ...(options.headers || {}),
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  if (options.body && typeof options.body === 'object' && !(options.body instanceof FormData)) {
    headers['Content-Type'] = 'application/json';
    options.body = JSON.stringify(options.body);
  }

  try {
    const response = await fetch(url, { ...options, headers });
    const json = await response.json().catch(() => ({}));

    if (!response.ok) {
      const errorMsg = json.data && typeof json.data === 'object'
        ? Object.values(json.data).join(', ')
        : (json.message || `Request failed with status ${response.status}`);
      return { success: false, error: errorMsg, statusCode: response.status };
    }

    return { success: true, data: json.data, message: json.message };
  } catch (error) {
    return { success: false, error: error.message || 'Network error occurred' };
  }
}

/**
 * Health Check Service
 */
export const healthService = {
  async checkHealth() {
    const startTime = performance.now();
    try {
      const response = await fetch(API_ENDPOINTS.HEALTH, {
        method: 'GET',
        headers: { 'Accept': 'application/json' },
      });
      const latencyMs = Math.round(performance.now() - startTime);
      if (!response.ok) throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      const data = await response.json();
      return { success: true, statusCode: response.status, latencyMs, data };
    } catch (error) {
      const latencyMs = Math.round(performance.now() - startTime);
      return { success: false, statusCode: 0, latencyMs, error: error.message || 'Unable to connect to backend' };
    }
  },

  async getHealthStatus() {
    try {
      const response = await fetch(API_ENDPOINTS.HEALTH_STATUS, {
        method: 'GET',
        headers: { 'Accept': 'application/json' },
      });
      const json = await response.json();
      return { statusCode: response.status, ...json };
    } catch (error) {
      return { success: false, statusCode: 0, message: error.message || 'Failed to fetch status details', data: null };
    }
  },
};

/**
 * Authentication Service
 */
export const authService = {
  async login(usernameOrEmail, password) {
    return fetchApi(API_ENDPOINTS.AUTH_LOGIN, {
      method: 'POST',
      body: { usernameOrEmail, password },
    });
  },

  async register(registrationData) {
    return fetchApi(API_ENDPOINTS.AUTH_REGISTER, {
      method: 'POST',
      body: registrationData,
    });
  },

  async getCurrentUser(token) {
    const headers = token ? { 'Authorization': `Bearer ${token}` } : {};
    return fetchApi(API_ENDPOINTS.AUTH_ME, {
      method: 'GET',
      headers,
    });
  },

  async getRoles() {
    const res = await fetchApi(API_ENDPOINTS.AUTH_ROLES);
    return res.success ? res.data : ['ROLE_STUDENT', 'ROLE_INSTRUCTOR'];
  },
};

/**
 * Public Courses Service
 */
export const courseService = {
  async getPublishedCourses({ search, category, difficulty, page = 0, size = 12, sort = 'createdAt,desc' } = {}) {
    const params = new URLSearchParams();
    if (search) params.append('search', search);
    if (category) params.append('category', category);
    if (difficulty) params.append('difficulty', difficulty);
    params.append('page', page);
    params.append('size', size);
    params.append('sort', sort);

    return fetchApi(`${API_ENDPOINTS.COURSES}?${params.toString()}`);
  },

  async getCourseById(id) {
    return fetchApi(API_ENDPOINTS.COURSE_BY_ID(id));
  },
};

/**
 * Administrator Service
 */
export const adminService = {
  async getStats() {
    return fetchApi(API_ENDPOINTS.ADMIN_STATS);
  },

  async getAllCourses() {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSES);
  },

  async createCourse(courseData) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSES, {
      method: 'POST',
      body: courseData,
    });
  },

  async updateCourse(id, courseData) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_BY_ID(id), {
      method: 'PUT',
      body: courseData,
    });
  },

  async deleteCourse(id) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_BY_ID(id), {
      method: 'DELETE',
    });
  },

  async publishCourse(id) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_PUBLISH(id), {
      method: 'PUT',
    });
  },

  async unpublishCourse(id) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_UNPUBLISH(id), {
      method: 'PUT',
    });
  },

  async archiveCourse(id) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_ARCHIVE(id), {
      method: 'PUT',
    });
  },

  async getInstructors() {
    return fetchApi(API_ENDPOINTS.ADMIN_INSTRUCTORS);
  },

  async assignInstructor(courseId, instructorId) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_ASSIGN_INSTRUCTOR(courseId), {
      method: 'POST',
      body: { instructorId },
    });
  },

  async removeInstructor(courseId, instructorId) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_REMOVE_INSTRUCTOR(courseId, instructorId), {
      method: 'DELETE',
    });
  },

  // Modules
  async addModule(courseId, moduleData) {
    return fetchApi(API_ENDPOINTS.ADMIN_COURSE_ADD_MODULE(courseId), {
      method: 'POST',
      body: moduleData,
    });
  },

  async updateModule(moduleId, moduleData) {
    return fetchApi(API_ENDPOINTS.ADMIN_MODULE_UPDATE(moduleId), {
      method: 'PUT',
      body: moduleData,
    });
  },

  async deleteModule(moduleId) {
    return fetchApi(API_ENDPOINTS.ADMIN_MODULE_DELETE(moduleId), {
      method: 'DELETE',
    });
  },

  async reorderModules(courseId, orderedIds) {
    return fetchApi(API_ENDPOINTS.ADMIN_MODULES_REORDER(courseId), {
      method: 'PUT',
      body: { orderedIds },
    });
  },

  // Lessons
  async addLesson(moduleId, lessonData) {
    return fetchApi(API_ENDPOINTS.ADMIN_MODULE_ADD_LESSON(moduleId), {
      method: 'POST',
      body: lessonData,
    });
  },

  async updateLesson(lessonId, lessonData) {
    return fetchApi(API_ENDPOINTS.ADMIN_LESSON_UPDATE(lessonId), {
      method: 'PUT',
      body: lessonData,
    });
  },

  async deleteLesson(lessonId) {
    return fetchApi(API_ENDPOINTS.ADMIN_LESSON_DELETE(lessonId), {
      method: 'DELETE',
    });
  },

  async reorderLessons(moduleId, orderedIds) {
    return fetchApi(API_ENDPOINTS.ADMIN_LESSONS_REORDER(moduleId), {
      method: 'PUT',
      body: { orderedIds },
    });
  },
};

/**
 * Student Learning Service
 */
export const studentService = {
  async getMyEnrollments() {
    return fetchApi(API_ENDPOINTS.STUDENT_ENROLLMENTS);
  },

  async enroll(courseId) {
    return fetchApi(API_ENDPOINTS.STUDENT_ENROLL(courseId), {
      method: 'POST',
    });
  },

  async isEnrolled(courseId) {
    const res = await fetchApi(API_ENDPOINTS.STUDENT_IS_ENROLLED(courseId));
    return res.success ? res.data?.enrolled : false;
  },

  async getLearningContent(courseId) {
    return fetchApi(API_ENDPOINTS.STUDENT_LEARN(courseId));
  },

  async markLessonComplete(lessonId) {
    return fetchApi(API_ENDPOINTS.STUDENT_LESSON_COMPLETE(lessonId), {
      method: 'POST',
    });
  },

  async markLessonIncomplete(lessonId) {
    return fetchApi(API_ENDPOINTS.STUDENT_LESSON_UNCOMPLETE(lessonId), {
      method: 'POST',
    });
  },

  async recordLessonOpened(lessonId) {
    return fetchApi(API_ENDPOINTS.STUDENT_LESSON_OPENED(lessonId), {
      method: 'POST',
    });
  },
};

/**
 * Instructor Portal Service
 */
export const instructorService = {
  async getAssignedCourses() {
    return fetchApi(API_ENDPOINTS.INSTRUCTOR_COURSES);
  },

  async getAssignedCourseContent(courseId) {
    return fetchApi(API_ENDPOINTS.INSTRUCTOR_COURSE_BY_ID(courseId));
  },

  async getEnrolledStudents(courseId, filter = 'all') {
    return fetchApi(`${API_ENDPOINTS.INSTRUCTOR_COURSE_STUDENTS(courseId)}?filter=${filter}`);
  },

  async getStudentProgress(courseId, studentId) {
    return fetchApi(API_ENDPOINTS.INSTRUCTOR_STUDENT_PROGRESS(courseId, studentId));
  },
};
