import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { instructorService } from '../../services/api';

export default function StudentProgressPage() {
  const { id: courseId, studentId } = useParams();
  const navigate = useNavigate();

  const [progressDetail, setProgressDetail] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadStudentDetail();
  }, [courseId, studentId]);

  const loadStudentDetail = async () => {
    setLoading(true);
    const res = await instructorService.getStudentProgress(courseId, studentId);
    if (res.success && res.data) {
      setProgressDetail(res.data);
    } else {
      setError(res.error || 'Failed to load student progress detail');
    }
    setLoading(false);
  };

  const formatDate = (isoString) => {
    if (!isoString) return '—';
    try {
      return new Date(isoString).toLocaleString(undefined, {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return isoString;
    }
  };

  if (loading) {
    return (
      <div className="section-container" style={{ padding: '6rem 2rem', textAlign: 'center' }}>
        <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
        <p style={{ color: 'var(--text-muted)' }}>Loading student audit history...</p>
      </div>
    );
  }

  if (error || !progressDetail) {
    return (
      <div className="section-container" style={{ padding: '4rem 2rem', textAlign: 'center' }}>
        <div className="admin-card" style={{ maxWidth: 600, margin: '0 auto', padding: '3rem 2rem' }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>⚠️</span>
          <h2 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '1rem' }}>
            {error || 'Student Record Not Found'}
          </h2>
          <Link to={`/instructor/courses/${courseId}/students`} className="cta-btn cta-btn-primary">
            &larr; Back to Enrolled Students
          </Link>
        </div>
      </div>
    );
  }

  const progress = Math.round((progressDetail.progressPercentage || 0) * 10) / 10;
  const isDone = Boolean(progressDetail.completed);

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Breadcrumb */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          <Link to="/instructor/dashboard" style={{ color: 'var(--text-secondary)' }}>Instructor Portal</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <Link to={`/instructor/courses/${courseId}/students`} style={{ color: 'var(--text-secondary)' }}>Students</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <span style={{ color: 'var(--gold-primary)' }}>{progressDetail.studentName}</span>
        </div>

        <Link to={`/instructor/courses/${courseId}/students`} className="cta-btn cta-btn-secondary" style={{ padding: '0.5rem 1rem', fontSize: '0.85rem' }}>
          &larr; Back to Cohort
        </Link>
      </div>

      {/* Header Profile Card */}
      <div className="admin-card" style={{ padding: '2rem', marginBottom: '2.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1.5rem' }}>
          <div style={{ display: 'flex', gap: '1.25rem', alignItems: 'center' }}>
            <div className="greeting-avatar" style={{ width: 54, height: 54, fontSize: '1.35rem' }}>
              {progressDetail.studentName ? progressDetail.studentName[0] : 'S'}
            </div>
            <div>
              <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.85rem', color: 'var(--text-primary)', margin: 0 }}>
                {progressDetail.studentName}
              </h1>
              <div style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.25rem' }}>
                @{progressDetail.studentUsername} &bull; {progressDetail.studentEmail}
              </div>
            </div>
          </div>

          <div style={{ textAlign: 'right' }}>
            <span
              style={{
                padding: '0.35rem 0.85rem',
                borderRadius: '20px',
                fontSize: '0.85rem',
                fontWeight: 600,
                background: isDone ? 'rgba(52, 211, 153, 0.15)' : 'rgba(197, 155, 39, 0.15)',
                color: isDone ? '#34d399' : 'var(--gold-primary)',
              }}
            >
              {isDone ? '🏆 Course Completed' : '⚡ In Progress'}
            </span>
            <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginTop: '0.4rem' }}>
              Enrolled: {formatDate(progressDetail.enrolledAt)}
            </div>
          </div>
        </div>

        {/* Progress Bar */}
        <div style={{ marginTop: '2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem', marginBottom: '0.5rem' }}>
            <span style={{ color: 'var(--text-secondary)' }}>
              Completed Lessons: <strong>{progressDetail.completedLessonsCount || 0}</strong> of <strong>{progressDetail.totalLessonsCount || 0}</strong>
            </span>
            <strong style={{ color: isDone ? '#34d399' : 'var(--gold-primary)', fontSize: '1.1rem' }}>
              {progress}%
            </strong>
          </div>
          <div style={{ width: '100%', height: '10px', background: 'rgba(255, 255, 255, 0.08)', borderRadius: '5px', overflow: 'hidden' }}>
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
        </div>
      </div>

      {/* Activity Audit Trail */}
      <div>
        <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.5rem', color: 'var(--text-primary)', marginBottom: '1.5rem' }}>
          Learning Activity History &amp; Audit Trail
        </h2>

        {progressDetail.recentActivities?.length === 0 ? (
          <div className="admin-card" style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            No activity records logged for this student yet.
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {progressDetail.recentActivities?.map((act) => {
              const isComplete = act.activityType === 'LESSON_COMPLETED' || act.activityType === 'COURSE_COMPLETED';
              const isEnrolledAct = act.activityType === 'COURSE_ENROLLED';

              return (
                <div
                  key={act.id}
                  style={{
                    padding: '1rem 1.25rem',
                    background: 'var(--surface-color)',
                    border: '1px solid var(--border-color)',
                    borderRadius: '8px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    flexWrap: 'wrap',
                    gap: '0.75rem',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                    <span style={{ fontSize: '1.25rem' }}>
                      {act.activityType === 'COURSE_COMPLETED'
                        ? '🏆'
                        : isComplete
                        ? '✅'
                        : isEnrolledAct
                        ? '🎓'
                        : '📖'}
                    </span>
                    <div>
                      <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.9rem' }}>
                        {act.description}
                      </div>
                      <div style={{ fontSize: '0.75rem', color: 'var(--gold-primary)', marginTop: '0.15rem' }}>
                        {act.activityType.replace(/_/g, ' ')}
                      </div>
                    </div>
                  </div>

                  <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    {formatDate(act.timestamp)}
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
