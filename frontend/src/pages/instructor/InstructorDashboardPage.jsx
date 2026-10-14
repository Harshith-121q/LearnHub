import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { instructorService } from '../../services/api';
import { useAuth } from '../../context/useAuth';

export default function InstructorDashboardPage() {
  const { user } = useAuth();
  const navigate = useNavigate();

  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadAssignedCourses();
  }, []);

  const loadAssignedCourses = async () => {
    setLoading(true);
    const res = await instructorService.getAssignedCourses();
    if (res.success && res.data) {
      setCourses(res.data);
    }
    setLoading(false);
  };

  const totalCourses = courses.length;
  const totalStudents = courses.reduce((sum, c) => sum + (c.totalEnrolledStudents || 0), 0);
  const totalCompleted = courses.reduce((sum, c) => sum + (c.studentsCompleted || 0), 0);
  const totalStarted = courses.reduce((sum, c) => sum + (c.studentsStarted || 0), 0);
  const avgCompletion = totalCourses > 0
    ? Math.round((courses.reduce((sum, c) => sum + (c.averageCompletionPercentage || 0), 0) / totalCourses) * 10) / 10
    : 0;

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Header */}
      <div style={{ marginBottom: '2.5rem' }}>
        <div className="greeting-pill" style={{ marginBottom: '0.5rem' }}>
          <span className="live-dot"></span>
          <span>Instructor Faculty Portal</span>
        </div>
        <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2.25rem', color: 'var(--text-primary)', margin: 0 }}>
          Instructor Overview &bull; <span className="gold-text">{user?.fullName || 'Faculty Member'}</span>
        </h1>
        <p style={{ color: 'var(--text-secondary)', marginTop: '0.4rem', fontSize: '0.95rem' }}>
          Monitor your assigned courses, oversee enrolled student cohorts, and inspect learning progress.
        </p>
      </div>

      {/* Metrics Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: '1.5rem', marginBottom: '3rem' }}>
        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>📚</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--text-primary)' }}>{totalCourses}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Assigned Courses</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>👥</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--gold-primary)' }}>{totalStudents}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Total Students Enrolled</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>⚡</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--gold-primary)' }}>{totalStarted}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Active Students</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>🏆</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: '#34d399' }}>{totalCompleted}</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Graduated Students</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>📈</div>
          <div style={{ fontSize: '2rem', fontWeight: 700, color: 'var(--gold-primary)' }}>{avgCompletion}%</div>
          <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Cohort Avg Completion</div>
        </div>
      </div>

      {/* Assigned Courses Section */}
      <div>
        <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.5rem', color: 'var(--text-primary)', marginBottom: '1.5rem' }}>
          Assigned Courses
        </h2>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '3rem 0' }}>
            <div className="spinner" style={{ margin: '0 auto 1rem', width: 36, height: 36 }}></div>
            <p style={{ color: 'var(--text-muted)' }}>Loading assigned courses...</p>
          </div>
        ) : courses.length === 0 ? (
          <div className="admin-card" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
            <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>👨‍🏫</span>
            <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
              No Courses Assigned Yet
            </h3>
            <p style={{ color: 'var(--text-muted)', maxWidth: 460, margin: '0 auto' }}>
              Your administrator will assign you to oversee specific courses. Once assigned, you can track enrolled students and progress metrics here.
            </p>
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '2rem' }}>
            {courses.map((course) => {
              const avg = Math.round((course.averageCompletionPercentage || 0) * 10) / 10;
              return (
                <div
                  key={course.id}
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
                      {course.category} &bull; {course.difficultyLevel}
                    </span>
                    <span
                      style={{
                        fontSize: '0.75rem',
                        padding: '0.2rem 0.6rem',
                        borderRadius: '12px',
                        fontWeight: 600,
                        background: course.status === 'PUBLISHED' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(239, 68, 68, 0.15)',
                        color: course.status === 'PUBLISHED' ? '#34d399' : '#f87171',
                      }}
                    >
                      {course.status}
                    </span>
                  </div>

                  <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--text-primary)', marginBottom: '0.75rem', lineHeight: 1.3 }}>
                    {course.title}
                  </h3>

                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6, marginBottom: '1.25rem', flexGrow: 1 }}>
                    {course.description?.length > 120 ? `${course.description.substring(0, 120)}...` : course.description}
                  </p>

                  {/* Course stats */}
                  <div
                    style={{
                      background: 'rgba(255, 255, 255, 0.02)',
                      border: '1px solid var(--border-color)',
                      borderRadius: '8px',
                      padding: '0.75rem 1rem',
                      marginBottom: '1.25rem',
                      display: 'grid',
                      gridTemplateColumns: 'repeat(3, 1fr)',
                      gap: '0.5rem',
                      textAlign: 'center',
                    }}
                  >
                    <div>
                      <div style={{ fontWeight: 700, color: 'var(--text-primary)', fontSize: '1.1rem' }}>
                        {course.totalEnrolledStudents || 0}
                      </div>
                      <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Enrolled</div>
                    </div>
                    <div>
                      <div style={{ fontWeight: 700, color: '#34d399', fontSize: '1.1rem' }}>
                        {course.studentsCompleted || 0}
                      </div>
                      <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Completed</div>
                    </div>
                    <div>
                      <div style={{ fontWeight: 700, color: 'var(--gold-primary)', fontSize: '1.1rem' }}>
                        {avg}%
                      </div>
                      <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Avg Progress</div>
                    </div>
                  </div>

                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
                    <button
                      onClick={() => navigate(`/instructor/courses/${course.id}`)}
                      className="cta-btn cta-btn-secondary"
                      style={{ padding: '0.6rem 0.5rem', fontSize: '0.85rem', textAlign: 'center' }}
                    >
                      📖 Curriculum
                    </button>
                    <button
                      onClick={() => navigate(`/instructor/courses/${course.id}/students`)}
                      className="cta-btn cta-btn-primary"
                      style={{ padding: '0.6rem 0.5rem', fontSize: '0.85rem', textAlign: 'center' }}
                    >
                      👥 View Students &rarr;
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
