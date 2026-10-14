import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { instructorService } from '../../services/api';

export default function EnrolledStudentsPage() {
  const { id: courseId } = useParams();
  const navigate = useNavigate();

  const [course, setCourse] = useState(null);
  const [students, setStudents] = useState([]);
  const [filter, setFilter] = useState('all');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, [courseId, filter]);

  const loadData = async () => {
    setLoading(true);
    const [courseRes, studentsRes] = await Promise.all([
      instructorService.getAssignedCourseContent(courseId),
      instructorService.getEnrolledStudents(courseId, filter),
    ]);

    if (courseRes.success) setCourse(courseRes.data);
    if (studentsRes.success) setStudents(studentsRes.data || []);
    setLoading(false);
  };

  const formatDate = (isoString) => {
    if (!isoString) return '—';
    try {
      return new Date(isoString).toLocaleDateString(undefined, {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
      });
    } catch {
      return isoString;
    }
  };

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Breadcrumb */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          <Link to="/instructor/dashboard" style={{ color: 'var(--text-secondary)' }}>Instructor Portal</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <Link to={`/instructor/courses/${courseId}`} style={{ color: 'var(--text-secondary)' }}>{course?.title || 'Course'}</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <span style={{ color: 'var(--gold-primary)' }}>Enrolled Cohort</span>
        </div>

        <Link to="/instructor/dashboard" className="cta-btn cta-btn-secondary" style={{ padding: '0.5rem 1rem', fontSize: '0.85rem' }}>
          &larr; Back to Dashboard
        </Link>
      </div>

      {/* Header */}
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2rem', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
          Enrolled Students &bull; <span className="gold-text">{course?.title || 'Loading...'}</span>
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
          Track individual student engagement, completion milestones, and real-time learning activity.
        </p>
      </div>

      {/* Filter Tabs */}
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem' }}>
        <button
          onClick={() => setFilter('all')}
          className={`tab-btn ${filter === 'all' ? 'active' : ''}`}
          style={{ padding: '0.5rem 1.25rem', borderRadius: '6px' }}
        >
          All Students ({students.length})
        </button>
        <button
          onClick={() => setFilter('in-progress')}
          className={`tab-btn ${filter === 'in-progress' ? 'active' : ''}`}
          style={{ padding: '0.5rem 1.25rem', borderRadius: '6px' }}
        >
          In Progress
        </button>
        <button
          onClick={() => setFilter('completed')}
          className={`tab-btn ${filter === 'completed' ? 'active' : ''}`}
          style={{ padding: '0.5rem 1.25rem', borderRadius: '6px' }}
        >
          Graduated (100%)
        </button>
      </div>

      {/* Students Table */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '3rem 0' }}>
          <div className="spinner" style={{ margin: '0 auto 1rem', width: 36, height: 36 }}></div>
          <p style={{ color: 'var(--text-muted)' }}>Loading student cohort...</p>
        </div>
      ) : students.length === 0 ? (
        <div className="admin-card" style={{ textAlign: 'center', padding: '3rem 2rem' }}>
          <span style={{ fontSize: '2.5rem', display: 'block', marginBottom: '0.75rem' }}>👥</span>
          <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
            No Students Found
          </h3>
          <p style={{ color: 'var(--text-muted)' }}>
            No students match the selected filter for this course.
          </p>
        </div>
      ) : (
        <div className="admin-card" style={{ padding: 0, overflow: 'hidden' }}>
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.9rem' }}>
              <thead>
                <tr style={{ background: 'rgba(255, 255, 255, 0.03)', borderBottom: '1px solid var(--border-color)' }}>
                  <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Student</th>
                  <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Enrolled Date</th>
                  <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Progress</th>
                  <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Status</th>
                  <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Last Activity</th>
                  <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600, textAlign: 'right' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {students.map((st) => {
                  const progress = Math.round((st.progressPercentage || 0) * 10) / 10;
                  const isDone = Boolean(st.completed);

                  return (
                    <tr
                      key={st.studentId}
                      style={{ borderBottom: '1px solid var(--border-color)', transition: 'background 0.15s ease' }}
                    >
                      <td style={{ padding: '1rem 1.25rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                          <div className="greeting-avatar" style={{ width: 34, height: 34, fontSize: '0.85rem' }}>
                            {st.studentName ? st.studentName[0] : 'S'}
                          </div>
                          <div>
                            <div style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{st.studentName}</div>
                            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                              @{st.studentUsername} &bull; {st.studentEmail}
                            </div>
                          </div>
                        </div>
                      </td>

                      <td style={{ padding: '1rem 1.25rem', color: 'var(--text-secondary)' }}>
                        {formatDate(st.enrolledAt)}
                      </td>

                      <td style={{ padding: '1rem 1.25rem', minWidth: 160 }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: '0.25rem' }}>
                          <span style={{ color: 'var(--text-muted)' }}>
                            {st.completedLessonsCount || 0} / {st.totalLessonsCount || 0} lessons
                          </span>
                          <strong style={{ color: isDone ? '#34d399' : 'var(--gold-primary)' }}>
                            {progress}%
                          </strong>
                        </div>
                        <div style={{ width: '100%', height: '6px', background: 'rgba(255, 255, 255, 0.08)', borderRadius: '3px', overflow: 'hidden' }}>
                          <div
                            style={{
                              width: `${progress}%`,
                              height: '100%',
                              background: isDone
                                ? 'linear-gradient(90deg, #10b981, #34d399)'
                                : 'linear-gradient(90deg, #C59B27, #E5B235)',
                            }}
                          ></div>
                        </div>
                      </td>

                      <td style={{ padding: '1rem 1.25rem' }}>
                        <span
                          style={{
                            padding: '0.2rem 0.6rem',
                            borderRadius: '12px',
                            fontSize: '0.75rem',
                            fontWeight: 600,
                            background: isDone ? 'rgba(52, 211, 153, 0.15)' : 'rgba(197, 155, 39, 0.15)',
                            color: isDone ? '#34d399' : 'var(--gold-primary)',
                          }}
                        >
                          {isDone ? 'Completed' : 'In Progress'}
                        </span>
                      </td>

                      <td style={{ padding: '1rem 1.25rem', color: 'var(--text-secondary)', fontSize: '0.8rem', maxWidth: 220 }}>
                        {st.lastActivityDescription ? (
                          <div>
                            <div style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                              {st.lastActivityDescription}
                            </div>
                            <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>
                              {formatDate(st.lastActivityDate)}
                            </div>
                          </div>
                        ) : (
                          <span style={{ color: 'var(--text-muted)' }}>No recent activity</span>
                        )}
                      </td>

                      <td style={{ padding: '1rem 1.25rem', textAlign: 'right' }}>
                        <button
                          onClick={() => navigate(`/instructor/courses/${courseId}/students/${st.studentId}`)}
                          className="cta-btn cta-btn-secondary"
                          style={{ padding: '0.4rem 0.85rem', fontSize: '0.8rem' }}
                          id={`btn-view-student-${st.studentId}`}
                        >
                          Inspect Detail &rarr;
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}
