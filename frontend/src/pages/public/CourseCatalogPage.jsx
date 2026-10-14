import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { courseService, studentService } from '../../services/api';
import { useAuth } from '../../context/useAuth';

export default function CourseCatalogPage({ onOpenAuth }) {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [enrolledCourseIds, setEnrolledCourseIds] = useState(new Set());
  const [enrollingId, setEnrollingId] = useState(null);
  const [message, setMessage] = useState(null);

  const { isAuthenticated, user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    loadCourses();
  }, [category, difficulty]);

  useEffect(() => {
    if (isAuthenticated && user?.role === 'ROLE_STUDENT') {
      studentService.getMyEnrollments().then((res) => {
        if (res.success && res.data) {
          const ids = new Set(res.data.map((e) => e.courseId));
          setEnrolledCourseIds(ids);
        }
      });
    }
  }, [isAuthenticated, user]);

  const loadCourses = async () => {
    setLoading(true);
    const res = await courseService.getPublishedCourses({
      search: search.trim() || undefined,
      category: category || undefined,
      difficulty: difficulty || undefined,
    });
    if (res.success && res.data) {
      setCourses(res.data.content || []);
    }
    setLoading(false);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    loadCourses();
  };

  const handleEnroll = async (courseId) => {
    if (!isAuthenticated) {
      onOpenAuth('login');
      return;
    }

    if (user.role !== 'ROLE_STUDENT') {
      setMessage({ type: 'error', text: 'Only registered Student accounts can enroll in courses.' });
      setTimeout(() => setMessage(null), 4000);
      return;
    }

    setEnrollingId(courseId);
    const res = await studentService.enroll(courseId);
    setEnrollingId(null);

    if (res.success) {
      setEnrolledCourseIds((prev) => new Set([...prev, courseId]));
      setMessage({ type: 'success', text: 'Successfully enrolled! Redirecting to your learning workspace...' });
      setTimeout(() => {
        navigate(`/student/courses/${courseId}/learn`);
      }, 1000);
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to enroll in course' });
      setTimeout(() => setMessage(null), 4000);
    }
  };

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Header */}
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <span className="section-badge">Mastery Curriculum</span>
        <h1 className="hero-title" style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>
          Explore Verified <span className="gold-text">Technical Tracks</span>
        </h1>
        <p className="hero-subtitle" style={{ maxWidth: 680, margin: '0 auto' }}>
          Choose from structured, production-grade courses in Java and Python designed to take you from foundational concepts to advanced architectural mastery.
        </p>
      </div>

      {/* Notification Toast */}
      {message && (
        <div
          className={`auth-alert ${message.type === 'success' ? 'success-alert' : 'error-alert'}`}
          style={{ maxWidth: 700, margin: '0 auto 2rem' }}
        >
          <span>{message.type === 'success' ? '✅' : '⚠️'}</span>
          <span>{message.text}</span>
        </div>
      )}

      {/* Filter and Search Bar */}
      <div
        className="admin-card"
        style={{
          padding: '1.5rem',
          marginBottom: '2.5rem',
          display: 'flex',
          flexWrap: 'wrap',
          gap: '1rem',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        <form onSubmit={handleSearchSubmit} style={{ display: 'flex', gap: '0.75rem', flex: '1 1 300px' }}>
          <input
            type="text"
            className="form-input"
            placeholder="Search topics, keywords, courses..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{ margin: 0 }}
          />
          <button type="submit" className="cta-btn cta-btn-secondary" style={{ padding: '0 1.25rem', whiteSpace: 'nowrap' }}>
            🔍 Search
          </button>
        </form>

        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <select
            className="form-input"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            style={{ width: 'auto', margin: 0, padding: '0.6rem 1rem' }}
          >
            <option value="">All Categories</option>
            <option value="Java">Java</option>
            <option value="Python">Python</option>
            <option value="Web Development">Web Development</option>
          </select>

          <select
            className="form-input"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)}
            style={{ width: 'auto', margin: 0, padding: '0.6rem 1rem' }}
          >
            <option value="">All Difficulties</option>
            <option value="BEGINNER">Beginner</option>
            <option value="INTERMEDIATE">Intermediate</option>
            <option value="ADVANCED">Advanced</option>
          </select>
        </div>
      </div>

      {/* Course Grid */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '4rem 0' }}>
          <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
          <p style={{ color: 'var(--text-muted)' }}>Loading verified tracks...</p>
        </div>
      ) : courses.length === 0 ? (
        <div className="admin-card" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>🔍</span>
          <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
            No courses found
          </h3>
          <p style={{ color: 'var(--text-muted)' }}>
            Try adjusting your search criteria or resetting the category filter.
          </p>
        </div>
      ) : (
        <div className="courses-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: '2rem' }}>
          {courses.map((course) => {
            const isEnrolled = enrolledCourseIds.has(course.id);
            return (
              <div
                key={course.id}
                className="luxury-card course-card"
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  overflow: 'hidden',
                  background: 'var(--surface-color)',
                  border: '1px solid var(--border-color)',
                  borderRadius: '12px',
                }}
              >
                <div style={{ height: 180, overflow: 'hidden', position: 'relative', background: 'rgba(197, 155, 39, 0.08)' }}>
                  <img
                    src={course.category?.toLowerCase().includes('python') ? '/course-java.jpg' : '/course-java.jpg'}
                    alt={course.title}
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                  />
                  <div
                    style={{
                      position: 'absolute',
                      top: '1rem',
                      right: '1rem',
                      background: 'rgba(11, 19, 43, 0.85)',
                      backdropFilter: 'blur(8px)',
                      padding: '0.25rem 0.75rem',
                      borderRadius: '20px',
                      fontSize: '0.75rem',
                      border: '1px solid rgba(197, 155, 39, 0.3)',
                      color: 'var(--gold-primary)',
                      fontWeight: 600,
                    }}
                  >
                    {course.difficultyLevel}
                  </div>
                </div>

                <div style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column', flexGrow: 1 }}>
                  <div style={{ fontSize: '0.75rem', color: 'var(--gold-primary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '0.5rem' }}>
                    {course.category}
                  </div>
                  <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--text-primary)', marginBottom: '0.75rem', lineHeight: 1.4 }}>
                    {course.title}
                  </h3>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6, marginBottom: '1.25rem', flexGrow: 1 }}>
                    {course.description?.length > 130 ? `${course.description.substring(0, 130)}...` : course.description}
                  </p>

                  <div
                    style={{
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      paddingTop: '1rem',
                      borderTop: '1px solid var(--border-color)',
                      marginBottom: '1.25rem',
                      fontSize: '0.8rem',
                      color: 'var(--text-muted)',
                    }}
                  >
                    <span>⏱️ {course.estimatedDuration || 60} mins</span>
                    <span>📖 {course.moduleCount || 0} Modules</span>
                    <span>👥 {course.enrolledCount || 0} Learners</span>
                  </div>

                  <div style={{ display: 'grid', gridTemplateColumns: isEnrolled ? '1fr' : '1fr 1fr', gap: '0.75rem' }}>
                    <button
                      onClick={() => navigate(`/courses/${course.id}`)}
                      className="cta-btn cta-btn-secondary"
                      style={{ padding: '0.6rem 0.5rem', fontSize: '0.875rem', textAlign: 'center' }}
                    >
                      View Syllabus
                    </button>

                    {isEnrolled ? (
                      <button
                        onClick={() => navigate(`/student/courses/${course.id}/learn`)}
                        className="cta-btn cta-btn-primary"
                        style={{ padding: '0.6rem 0.5rem', fontSize: '0.875rem', textAlign: 'center' }}
                      >
                        ▶️ Resume Track
                      </button>
                    ) : (
                      <button
                        onClick={() => handleEnroll(course.id)}
                        disabled={enrollingId === course.id}
                        className="cta-btn cta-btn-primary"
                        style={{ padding: '0.6rem 0.5rem', fontSize: '0.875rem', textAlign: 'center' }}
                      >
                        {enrollingId === course.id ? 'Enrolling...' : 'Enroll Free'}
                      </button>
                    )}
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
