import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { instructorService } from '../../services/api';

export default function AssignedCourseDetailPage() {
  const { id: courseId } = useParams();
  const navigate = useNavigate();

  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadCourseDetails();
  }, [courseId]);

  const loadCourseDetails = async () => {
    setLoading(true);
    const res = await instructorService.getAssignedCourseContent(courseId);
    if (res.success && res.data) {
      setCourse(res.data);
    } else {
      setError(res.error || 'Failed to load assigned course content');
    }
    setLoading(false);
  };

  if (loading) {
    return (
      <div className="section-container" style={{ padding: '6rem 2rem', textAlign: 'center' }}>
        <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
        <p style={{ color: 'var(--text-muted)' }}>Loading assigned course syllabus...</p>
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
          <Link to="/instructor/dashboard" className="cta-btn cta-btn-primary">
            &larr; Back to Instructor Dashboard
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Breadcrumb & Navigation */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          <Link to="/instructor/dashboard" style={{ color: 'var(--text-secondary)' }}>Instructor Portal</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <span style={{ color: 'var(--gold-primary)' }}>{course.title}</span>
        </div>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button
            onClick={() => navigate(`/instructor/courses/${courseId}/students`)}
            className="cta-btn cta-btn-primary"
            style={{ padding: '0.6rem 1.25rem', fontSize: '0.875rem' }}
          >
            👥 View Enrolled Students ({course.enrolledCount || 0}) &rarr;
          </button>
        </div>
      </div>

      {/* Role Notice Alert */}
      <div
        style={{
          background: 'rgba(197, 155, 39, 0.08)',
          border: '1px solid rgba(197, 155, 39, 0.3)',
          borderRadius: '8px',
          padding: '1rem 1.5rem',
          marginBottom: '2.5rem',
          display: 'flex',
          alignItems: 'center',
          gap: '1rem',
          color: 'var(--text-secondary)',
          fontSize: '0.9rem',
        }}
      >
        <span style={{ fontSize: '1.25rem' }}>ℹ️</span>
        <div>
          <strong style={{ color: 'var(--gold-primary)' }}>Read-Only Faculty Inspection Mode:</strong> You are an assigned instructor for this course. Curriculums and modules are managed and authored by Administrator accounts.
        </div>
      </div>

      {/* Header Info Card */}
      <div className="admin-card" style={{ padding: '2rem', marginBottom: '2.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem', marginBottom: '1rem' }}>
          <div>
            <div style={{ fontSize: '0.8rem', color: 'var(--gold-primary)', fontWeight: 600, textTransform: 'uppercase', marginBottom: '0.5rem' }}>
              {course.category} &bull; {course.difficultyLevel} Level
            </div>
            <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2rem', color: 'var(--text-primary)', margin: 0 }}>
              {course.title}
            </h1>
          </div>

          <span
            style={{
              padding: '0.35rem 0.85rem',
              borderRadius: '20px',
              fontSize: '0.8rem',
              fontWeight: 600,
              background: course.status === 'PUBLISHED' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(239, 68, 68, 0.15)',
              color: course.status === 'PUBLISHED' ? '#34d399' : '#f87171',
            }}
          >
            Status: {course.status}
          </span>
        </div>

        <p style={{ color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: '1.5rem' }}>
          {course.description}
        </p>

        <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          <div>⏱️ <strong>{course.estimatedDuration}</strong> Total Minutes</div>
          <div>📖 <strong>{course.modules?.length || 0}</strong> Modules</div>
          <div>👥 <strong>{course.enrolledCount || 0}</strong> Enrolled Students</div>
        </div>
      </div>

      {/* Modules and Lessons List */}
      <div>
        <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.5rem', color: 'var(--text-primary)', marginBottom: '1.5rem' }}>
          Course Curriculum &amp; Lessons
        </h2>

        {course.modules?.length === 0 ? (
          <div className="admin-card" style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            No curriculum modules created for this course yet.
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {course.modules?.map((mod, idx) => (
              <div key={mod.id} className="admin-card" style={{ padding: '1.75rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
                  <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--gold-primary)', fontSize: '1.15rem', margin: 0 }}>
                    {mod.title}
                  </h3>
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    {mod.lessons?.length || 0} Lessons
                  </span>
                </div>

                {mod.description && (
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '1.25rem', lineHeight: 1.5 }}>
                    {mod.description}
                  </p>
                )}

                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                  {mod.lessons?.map((les, lIdx) => (
                    <div
                      key={les.id}
                      style={{
                        padding: '1rem',
                        background: 'rgba(0, 0, 0, 0.25)',
                        border: '1px solid var(--border-color)',
                        borderRadius: '8px',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                        <span style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.95rem' }}>
                          {lIdx + 1}. {les.title}
                        </span>
                        <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                          ⏱️ {les.estimatedDuration || 15} mins
                        </span>
                      </div>

                      <div style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', lineHeight: 1.5, marginBottom: les.codeExample ? '0.75rem' : 0 }}>
                        {les.content?.length > 150 ? `${les.content.substring(0, 150)}...` : les.content}
                      </div>

                      {les.codeExample && (
                        <div
                          style={{
                            background: '#070C1B',
                            padding: '0.75rem 1rem',
                            borderRadius: '6px',
                            border: '1px solid rgba(197, 155, 39, 0.2)',
                            fontFamily: 'Consolas, monospace',
                            fontSize: '0.8rem',
                            color: '#93c5fd',
                            overflowX: 'auto',
                            maxHeight: 120,
                          }}
                        >
                          <code>{les.codeExample}</code>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
