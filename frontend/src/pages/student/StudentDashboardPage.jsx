import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { studentService } from '../../services/api';
import { useAuth } from '../../context/useAuth';

export default function StudentDashboardPage() {
  const { user } = useAuth();
  const navigate = useNavigate();

  const [enrollments, setEnrollments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadEnrollments();
  }, []);

  const loadEnrollments = async () => {
    setLoading(true);
    const res = await studentService.getMyEnrollments();
    if (res.success && res.data) {
      setEnrollments(res.data);
    }
    setLoading(false);
  };

  const totalEnrolled = enrollments.length;
  const completedCount = enrollments.filter((e) => e.completed).length;
  const inProgressCount = totalEnrolled - completedCount;
  const avgProgress = totalEnrolled > 0
    ? Math.round((enrollments.reduce((sum, e) => sum + (e.progressPercentage || 0), 0) / totalEnrolled) * 10) / 10
    : 0;

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1.5rem', marginBottom: '2.5rem' }}>
        <div>
          <div className="greeting-pill" style={{ marginBottom: '0.5rem' }}>
            <span className="live-dot"></span>
            <span>Student Learning Portal</span>
          </div>
          <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2.25rem', color: 'var(--text-primary)', margin: 0 }}>
            Welcome back, <span className="gold-text">{user?.fullName || 'Scholar'}</span>!
          </h1>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.4rem', fontSize: '0.95rem' }}>
            Track your ongoing progress, step through sequential lessons, and master technical disciplines.
          </p>
        </div>

        <Link to="/courses" className="cta-btn cta-btn-secondary" style={{ padding: '0.75rem 1.5rem' }}>
          Explore More Tracks &rarr;
        </Link>
      </div>

      {/* Metrics Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.5rem', marginBottom: '3rem' }}>
        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>📚</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--text-primary)' }}>{totalEnrolled}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Enrolled Courses</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>⚡</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--gold-primary)' }}>{inProgressCount}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>In-Progress Tracks</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>🏆</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#34d399' }}>{completedCount}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Completed Tracks</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>📊</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--gold-primary)' }}>{avgProgress}%</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Average Completion</div>
        </div>
      </div>

      {/* Enrolled Courses Section */}
      <div style={{ marginBottom: '3rem' }}>
        <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.5rem', color: 'var(--text-primary)', marginBottom: '1.5rem' }}>
          My Active Courses
        </h2>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '3rem 0' }}>
            <div className="spinner" style={{ margin: '0 auto 1rem', width: 36, height: 36 }}></div>
            <p style={{ color: 'var(--text-muted)' }}>Loading your enrollments...</p>
          </div>
        ) : enrollments.length === 0 ? (
          <div className="admin-card" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
            <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>🎓</span>
            <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.75rem' }}>
              You haven't enrolled in any courses yet
            </h3>
            <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem', maxWidth: 450, margin: '0 auto 1.5rem' }}>
              Explore our verified Java and Python curriculums to start your sequential learning journey.
            </p>
            <Link to="/courses" className="cta-btn cta-btn-primary">
              Browse Available Courses &rarr;
            </Link>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: '2rem' }}>
            {enrollments.map((enrollment) => {
              const progress = Math.round((enrollment.progressPercentage || 0) * 10) / 10;
              const isDone = Boolean(enrollment.completed);

              return (
                <div
                  key={enrollment.id}
                  className="luxury-card course-card"
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    padding: '1.75rem',
                    background: 'var(--surface-color)',
                    border: '1px solid var(--border-color)',
                    borderRadius: '12px',
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                    <span style={{ fontSize: '0.75rem', color: 'var(--gold-primary)', fontWeight: 600, textTransform: 'uppercase' }}>
                      {enrollment.courseCategory || 'Core Curriculum'}
                    </span>
                    <span
                      style={{
                        fontSize: '0.75rem',
                        padding: '0.2rem 0.6rem',
                        borderRadius: '12px',
                        fontWeight: 600,
                        background: isDone ? 'rgba(52, 211, 153, 0.15)' : 'rgba(197, 155, 39, 0.15)',
                        color: isDone ? '#34d399' : 'var(--gold-primary)',
                      }}
                    >
                      {isDone ? 'Completed' : 'In Progress'}
                    </span>
                  </div>

                  <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--text-primary)', marginBottom: '1rem', lineHeight: 1.3 }}>
                    {enrollment.courseTitle}
                  </h3>

                  {/* Progress Bar */}
                  <div style={{ marginBottom: '1.25rem' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', color: 'var(--text-secondary)', marginBottom: '0.4rem' }}>
                      <span>Progress</span>
                      <strong style={{ color: isDone ? '#34d399' : 'var(--gold-primary)' }}>{progress}%</strong>
                    </div>
                    <div style={{ width: '100%', height: '8px', background: 'rgba(255, 255, 255, 0.08)', borderRadius: '4px', overflow: 'hidden' }}>
                      <div
                        style={{
                          width: `${progress}%`,
                          height: '100%',
                          background: isDone
                            ? 'linear-gradient(90deg, #10b981, #34d399)'
                            : 'linear-gradient(90deg, #C59B27, #E5B235)',
                          transition: 'width 0.4s ease',
                        }}
                      ></div>
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.4rem', textAlign: 'right' }}>
                      {enrollment.completedLessonsCount || 0} of {enrollment.totalLessonsCount || 0} lessons completed
                    </div>
                  </div>

                  <div style={{ marginTop: 'auto', paddingTop: '1rem', borderTop: '1px solid var(--border-color)' }}>
                    <button
                      onClick={() => navigate(`/student/courses/${enrollment.courseId}/learn`)}
                      className="cta-btn cta-btn-primary"
                      style={{ width: '100%', textAlign: 'center', padding: '0.75rem' }}
                      id={`btn-resume-course-${enrollment.courseId}`}
                    >
                      {isDone ? '🔄 Review Curriculum' : '▶️ Resume Next Lesson'}
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
