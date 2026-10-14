import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { courseService, studentService } from '../../services/api';
import { useAuth } from '../../context/useAuth';

export default function CourseDetailPage({ onOpenAuth }) {
  const { id } = useParams();
  const navigate = useNavigate();
  const { isAuthenticated, user } = useAuth();

  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isEnrolled, setIsEnrolled] = useState(false);
  const [enrolling, setEnrolling] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadCourse();
  }, [id]);

  useEffect(() => {
    if (isAuthenticated && user?.role === 'ROLE_STUDENT' && id) {
      studentService.isEnrolled(id).then((enrolled) => {
        setIsEnrolled(enrolled);
      });
    }
  }, [isAuthenticated, user, id]);

  const loadCourse = async () => {
    setLoading(true);
    const res = await courseService.getCourseById(id);
    if (res.success && res.data) {
      setCourse(res.data);
    } else {
      setError(res.error || 'Failed to load course details');
    }
    setLoading(false);
  };

  const handleEnroll = async () => {
    if (!isAuthenticated) {
      onOpenAuth('login');
      return;
    }

    if (user.role !== 'ROLE_STUDENT') {
      setError('Only registered Student accounts can enroll in courses.');
      setTimeout(() => setError(null), 4000);
      return;
    }

    setEnrolling(true);
    const res = await studentService.enroll(id);
    setEnrolling(false);

    if (res.success) {
      setIsEnrolled(true);
      navigate(`/student/courses/${id}/learn`);
    } else {
      setError(res.error || 'Enrollment failed');
      setTimeout(() => setError(null), 4000);
    }
  };

  if (loading) {
    return (
      <div className="section-container" style={{ padding: '6rem 2rem', textAlign: 'center' }}>
        <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
        <p style={{ color: 'var(--text-muted)' }}>Loading course syllabus...</p>
      </div>
    );
  }

  if (error || !course) {
    return (
      <div className="section-container" style={{ padding: '4rem 2rem', textAlign: 'center' }}>
        <div className="admin-card" style={{ maxWidth: 600, margin: '0 auto', padding: '3rem 2rem' }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>⚠️</span>
          <h2 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '1rem' }}>
            {error || 'Course Not Found'}
          </h2>
          <Link to="/courses" className="cta-btn cta-btn-primary">
            &larr; Back to Course Catalog
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Breadcrumb */}
      <div style={{ marginBottom: '1.5rem', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
        <Link to="/" style={{ color: 'var(--text-secondary)' }}>Home</Link>
        <span style={{ margin: '0 0.5rem' }}>/</span>
        <Link to="/courses" style={{ color: 'var(--text-secondary)' }}>Courses</Link>
        <span style={{ margin: '0 0.5rem' }}>/</span>
        <span style={{ color: 'var(--gold-primary)' }}>{course.title}</span>
      </div>

      {/* Hero Banner */}
      <div
        className="admin-card"
        style={{
          padding: '2.5rem',
          marginBottom: '3rem',
          background: 'linear-gradient(135deg, rgba(11, 19, 43, 0.95) 0%, rgba(197, 155, 39, 0.08) 100%)',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '2.5rem',
          alignItems: 'center',
        }}
      >
        <div>
          <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center', marginBottom: '1rem' }}>
            <span
              style={{
                background: 'rgba(197, 155, 39, 0.15)',
                color: 'var(--gold-primary)',
                padding: '0.25rem 0.75rem',
                borderRadius: '20px',
                fontSize: '0.8rem',
                fontWeight: 600,
                border: '1px solid rgba(197, 155, 39, 0.3)',
              }}
            >
              {course.category}
            </span>
            <span
              style={{
                background: 'rgba(255, 255, 255, 0.05)',
                color: 'var(--text-secondary)',
                padding: '0.25rem 0.75rem',
                borderRadius: '20px',
                fontSize: '0.8rem',
              }}
            >
              {course.difficultyLevel} Level
            </span>
          </div>

          <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2.25rem', color: 'var(--text-primary)', marginBottom: '1rem', lineHeight: 1.3 }}>
            {course.title}
          </h1>

          <p style={{ color: 'var(--text-secondary)', lineHeight: 1.7, marginBottom: '1.5rem', fontSize: '1rem' }}>
            {course.description}
          </p>

          <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap', marginBottom: '2rem', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
            <div>⏱️ <strong>{course.estimatedDuration}</strong> Total Minutes</div>
            <div>📖 <strong>{course.modules?.length || 0}</strong> Modules</div>
            <div>
              👨‍🏫 Lead Instructor:{' '}
              <strong style={{ color: 'var(--gold-primary)' }}>
                {course.instructorName || 'LearnHub Faculty'}
              </strong>
            </div>
          </div>

          <div>
            {isEnrolled ? (
              <button
                onClick={() => navigate(`/student/courses/${course.id}/learn`)}
                className="cta-btn cta-btn-primary"
                style={{ padding: '0.85rem 2rem', fontSize: '1rem' }}
                id="btn-resume-from-detail"
              >
                ▶️ Resume Course Workspace
              </button>
            ) : (
              <button
                onClick={handleEnroll}
                disabled={enrolling}
                className="cta-btn cta-btn-primary"
                style={{ padding: '0.85rem 2rem', fontSize: '1rem' }}
                id="btn-enroll-from-detail"
              >
                {enrolling ? 'Enrolling...' : 'Enroll in Track Free &rarr;'}
              </button>
            )}
          </div>
        </div>

        <div style={{ borderRadius: '12px', overflow: 'hidden', border: '1px solid var(--border-color)', height: 260 }}>
          <img
            src={course.category?.toLowerCase().includes('python') ? '/course-java.jpg' : '/course-java.jpg'}
            alt={course.title}
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        </div>
      </div>

      {/* Curriculum Outline */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '2rem' }}>
        {/* Left Column: Learning Objectives & Prerequisites */}
        <div>
          {course.learningObjectives && (
            <div className="admin-card" style={{ padding: '1.75rem', marginBottom: '1.5rem' }}>
              <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--gold-primary)', fontSize: '1.15rem', marginBottom: '1rem' }}>
                🎯 What You Will Master
              </h3>
              <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, fontSize: '0.9rem', whiteSpace: 'pre-line' }}>
                {course.learningObjectives}
              </p>
            </div>
          )}

          {course.prerequisites && (
            <div className="admin-card" style={{ padding: '1.75rem', marginBottom: '1.5rem' }}>
              <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', fontSize: '1.15rem', marginBottom: '1rem' }}>
                📋 Recommended Prerequisites
              </h3>
              <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, fontSize: '0.9rem', whiteSpace: 'pre-line' }}>
                {course.prerequisites}
              </p>
            </div>
          )}

          {course.assignedInstructors && course.assignedInstructors.length > 0 && (
            <div className="admin-card" style={{ padding: '1.75rem' }}>
              <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', fontSize: '1.15rem', marginBottom: '1rem' }}>
                👨‍🏫 Assigned Course Instructors
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                {course.assignedInstructors.map((inst) => (
                  <div key={inst.id} style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                    <div className="greeting-avatar" style={{ width: 32, height: 32, fontSize: '0.85rem' }}>
                      {inst.fullName ? inst.fullName[0] : 'I'}
                    </div>
                    <div>
                      <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.9rem' }}>{inst.fullName}</div>
                      <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>@{inst.username}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Right Column: Structured Curriculum Accordion */}
        <div>
          <div className="admin-card" style={{ padding: '1.75rem' }}>
            <h2 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', fontSize: '1.35rem', marginBottom: '1.25rem' }}>
              Curriculum &amp; Sequential Modules
            </h2>

            {course.modules?.length === 0 ? (
              <p style={{ color: 'var(--text-muted)' }}>Curriculum is currently being finalized.</p>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                {course.modules?.map((module, idx) => (
                  <div
                    key={module.id}
                    style={{
                      border: '1px solid var(--border-color)',
                      borderRadius: '8px',
                      padding: '1.25rem',
                      background: 'rgba(255, 255, 255, 0.02)',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                      <h4 style={{ color: 'var(--gold-primary)', fontSize: '1rem', margin: 0 }}>
                        {module.title}
                      </h4>
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                        {module.lessons?.length || 0} Lessons
                      </span>
                    </div>

                    {module.description && (
                      <p style={{ color: 'var(--text-secondary)', fontSize: '0.825rem', marginBottom: '0.75rem', lineHeight: 1.5 }}>
                        {module.description}
                      </p>
                    )}

                    <div style={{ paddingLeft: '0.5rem', display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
                      {module.lessons?.map((lesson, lIdx) => (
                        <div
                          key={lesson.id}
                          style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            fontSize: '0.85rem',
                            color: 'var(--text-secondary)',
                            padding: '0.4rem 0.6rem',
                            borderRadius: '4px',
                            background: 'rgba(0, 0, 0, 0.2)',
                          }}
                        >
                          <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                            <span style={{ color: 'var(--text-muted)' }}>{lIdx + 1}.</span>
                            <span>{lesson.title}</span>
                          </span>
                          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                            {lesson.estimatedDuration || 15} min
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
