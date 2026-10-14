import React, { useState, useEffect, useMemo } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { studentService } from '../../services/api';

export default function LearningPage() {
  const { id: courseId } = useParams();
  const navigate = useNavigate();

  const [courseData, setCourseData] = useState(null);
  const [activeLessonId, setActiveLessonId] = useState(null);
  const [completedLessonIds, setCompletedLessonIds] = useState(new Set());
  const [progressPercentage, setProgressPercentage] = useState(0);
  const [completedLessonsCount, setCompletedLessonsCount] = useState(0);
  const [totalLessonsCount, setTotalLessonsCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [updating, setUpdating] = useState(false);
  const [copiedCode, setCopiedCode] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadLearningWorkspace();
  }, [courseId]);

  const loadLearningWorkspace = async () => {
    setLoading(true);
    const res = await studentService.getLearningContent(courseId);
    if (res.success && res.data) {
      const data = res.data;
      setCourseData(data);
      setCompletedLessonIds(new Set(data.completedLessonIds || []));
      setProgressPercentage(data.progressPercentage || 0);
      setCompletedLessonsCount(data.completedLessonsCount || 0);
      setTotalLessonsCount(data.totalLessonsCount || 0);

      // Select resume lesson or first lesson
      if (data.resumeLessonId) {
        setActiveLessonId(data.resumeLessonId);
      } else if (data.modules && data.modules.length > 0 && data.modules[0].lessons?.length > 0) {
        setActiveLessonId(data.modules[0].lessons[0].id);
      }
    } else {
      setError(res.error || 'Failed to load course workspace');
    }
    setLoading(false);
  };

  // Flatten all lessons across modules into a sequential array
  const flatLessons = useMemo(() => {
    if (!courseData?.modules) return [];
    const list = [];
    courseData.modules.forEach((mod) => {
      (mod.lessons || []).forEach((les) => {
        list.push({ ...les, moduleTitle: mod.title, moduleId: mod.id });
      });
    });
    return list;
  }, [courseData]);

  // Current active lesson object and navigation indices
  const currentLessonIndex = useMemo(() => {
    return flatLessons.findIndex((l) => l.id === activeLessonId);
  }, [flatLessons, activeLessonId]);

  const activeLesson = flatLessons[currentLessonIndex] || null;
  const prevLesson = currentLessonIndex > 0 ? flatLessons[currentLessonIndex - 1] : null;
  const nextLesson = currentLessonIndex < flatLessons.length - 1 ? flatLessons[currentLessonIndex + 1] : null;

  // Log lesson opened on change
  useEffect(() => {
    if (activeLessonId) {
      studentService.recordLessonOpened(activeLessonId);
    }
  }, [activeLessonId]);

  const handleToggleComplete = async () => {
    if (!activeLesson || updating) return;
    setUpdating(true);

    const isCurrentlyCompleted = completedLessonIds.has(activeLesson.id);
    const apiCall = isCurrentlyCompleted
      ? studentService.markLessonIncomplete(activeLesson.id)
      : studentService.markLessonComplete(activeLesson.id);

    const res = await apiCall;
    setUpdating(false);

    if (res.success && res.data) {
      const updatedEnrollment = res.data;
      setProgressPercentage(updatedEnrollment.progressPercentage || 0);
      setCompletedLessonsCount(updatedEnrollment.completedLessonsCount || 0);
      setTotalLessonsCount(updatedEnrollment.totalLessonsCount || 0);

      const nextCompleted = new Set(completedLessonIds);
      if (isCurrentlyCompleted) {
        nextCompleted.delete(activeLesson.id);
      } else {
        nextCompleted.add(activeLesson.id);
      }
      setCompletedLessonIds(nextCompleted);
    }
  };

  const handleNextLesson = async () => {
    if (!nextLesson) return;

    // Automatically mark the current lesson completed upon proceeding to the next topic
    if (activeLesson && !completedLessonIds.has(activeLesson.id)) {
      setUpdating(true);
      const res = await studentService.markLessonComplete(activeLesson.id);
      setUpdating(false);

      if (res.success && res.data) {
        const updatedEnrollment = res.data;
        setProgressPercentage(updatedEnrollment.progressPercentage || 0);
        setCompletedLessonsCount(updatedEnrollment.completedLessonsCount || 0);
        setTotalLessonsCount(updatedEnrollment.totalLessonsCount || 0);

        const nextCompleted = new Set(completedLessonIds);
        nextCompleted.add(activeLesson.id);
        setCompletedLessonIds(nextCompleted);
      }
    }

    setActiveLessonId(nextLesson.id);
  };

  const handleCopyCode = (code) => {
    if (!code) return;
    navigator.clipboard.writeText(code);
    setCopiedCode(true);
    setTimeout(() => setCopiedCode(false), 2000);
  };

  if (loading) {
    return (
      <div className="section-container" style={{ padding: '6rem 2rem', textAlign: 'center' }}>
        <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
        <p style={{ color: 'var(--text-muted)' }}>Opening learning workspace...</p>
      </div>
    );
  }

  if (error || !courseData) {
    return (
      <div className="section-container" style={{ padding: '4rem 2rem', textAlign: 'center' }}>
        <div className="admin-card" style={{ maxWidth: 600, margin: '0 auto', padding: '3rem 2rem' }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>⚠️</span>
          <h2 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '1rem' }}>
            {error || 'Unable to access learning workspace'}
          </h2>
          <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
            Please ensure you are enrolled in this course with an active student account.
          </p>
          <Link to="/student/dashboard" className="cta-btn cta-btn-primary">
            &larr; Back to Student Dashboard
          </Link>
        </div>
      </div>
    );
  }

  const isCurrentCompleted = activeLesson ? completedLessonIds.has(activeLesson.id) : false;
  const isCourseFinished = progressPercentage >= 100.0;

  return (
    <div style={{ display: 'flex', minHeight: 'calc(100vh - 80px)', background: 'var(--bg-primary)' }}>
      {/* Sidebar: Curriculum Tree */}
      <aside
        style={{
          width: 340,
          background: 'rgba(11, 19, 43, 0.98)',
          borderRight: '1px solid var(--border-color)',
          display: 'flex',
          flexDirection: 'column',
          flexShrink: 0,
        }}
      >
        {/* Sidebar Header with Progress Bar */}
        <div style={{ padding: '1.5rem', borderBottom: '1px solid var(--border-color)' }}>
          <Link
            to="/student/dashboard"
            style={{ fontSize: '0.8rem', color: 'var(--text-muted)', display: 'inline-flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.75rem' }}
          >
            &larr; Dashboard
          </Link>
          <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.15rem', color: 'var(--text-primary)', lineHeight: 1.3, marginBottom: '1rem' }}>
            {courseData.title}
          </h2>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', color: 'var(--text-secondary)', marginBottom: '0.35rem' }}>
              <span>Progress ({completedLessonsCount}/{totalLessonsCount})</span>
              <strong style={{ color: isCourseFinished ? '#34d399' : 'var(--gold-primary)' }}>
                {Math.round(progressPercentage * 10) / 10}%
              </strong>
            </div>
            <div style={{ width: '100%', height: '6px', background: 'rgba(255, 255, 255, 0.08)', borderRadius: '3px', overflow: 'hidden' }}>
              <div
                style={{
                  width: `${progressPercentage}%`,
                  height: '100%',
                  background: isCourseFinished
                    ? 'linear-gradient(90deg, #10b981, #34d399)'
                    : 'linear-gradient(90deg, #C59B27, #E5B235)',
                  transition: 'width 0.3s ease',
                }}
              ></div>
            </div>
          </div>
        </div>

        {/* Modules & Lessons List */}
        <div style={{ flexGrow: 1, overflowY: 'auto', padding: '1rem' }}>
          {courseData.modules?.map((mod, mIdx) => (
            <div key={mod.id} style={{ marginBottom: '1.25rem' }}>
              <div
                style={{
                  fontSize: '0.8rem',
                  fontWeight: 600,
                  color: 'var(--gold-primary)',
                  textTransform: 'uppercase',
                  letterSpacing: '0.04em',
                  marginBottom: '0.5rem',
                  paddingLeft: '0.5rem',
                }}
              >
                Module {mIdx + 1}: {mod.title.replace(/^Module\s*\d+:\s*/i, '')}
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
                {mod.lessons?.map((les) => {
                  const isDone = completedLessonIds.has(les.id);
                  const isActive = les.id === activeLessonId;

                  return (
                    <button
                      key={les.id}
                      onClick={() => setActiveLessonId(les.id)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        width: '100%',
                        padding: '0.6rem 0.75rem',
                        borderRadius: '6px',
                        background: isActive
                          ? 'rgba(197, 155, 39, 0.15)'
                          : 'transparent',
                        border: isActive
                          ? '1px solid rgba(197, 155, 39, 0.3)'
                          : '1px solid transparent',
                        color: isActive
                          ? 'var(--gold-primary)'
                          : isDone
                          ? 'var(--text-primary)'
                          : 'var(--text-secondary)',
                        textAlign: 'left',
                        cursor: 'pointer',
                        fontSize: '0.85rem',
                        transition: 'all 0.15s ease',
                      }}
                    >
                      <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', overflow: 'hidden' }}>
                        <span>{isDone ? '✅' : '⚪'}</span>
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                          {les.title}
                        </span>
                      </span>
                      <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', flexShrink: 0, marginLeft: '0.5rem' }}>
                        {les.estimatedDuration || 15}m
                      </span>
                    </button>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      </aside>

      {/* Main Learning Workspace */}
      <main style={{ flexGrow: 1, overflowY: 'auto', padding: '2.5rem 3rem' }}>
        {/* Course 100% Celebration Banner */}
        {isCourseFinished && (
          <div
            className="auth-alert success-alert"
            style={{
              padding: '1.25rem',
              marginBottom: '2rem',
              background: 'rgba(16, 185, 129, 0.15)',
              border: '1px solid rgba(16, 185, 129, 0.4)',
              borderRadius: '8px',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <span style={{ fontSize: '1.75rem' }}>🏆</span>
              <div>
                <strong style={{ color: '#34d399', fontSize: '1.05rem', display: 'block' }}>
                  Track Completed &bull; 100% Mastery Achieved!
                </strong>
                <span style={{ color: 'var(--text-secondary)', fontSize: '0.875rem' }}>
                  You have successfully completed every lesson in this curriculum. You can review topics or step into additional tracks.
                </span>
              </div>
            </div>
          </div>
        )}

        {activeLesson ? (
          <div style={{ maxWidth: 860, margin: '0 auto' }}>
            {/* Breadcrumb & Meta */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', flexWrap: 'wrap', gap: '1rem' }}>
              <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                <span>{activeLesson.moduleTitle}</span>
                <span style={{ margin: '0 0.5rem' }}>&gt;</span>
                <span style={{ color: 'var(--gold-primary)' }}>{activeLesson.title}</span>
              </div>

              <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center' }}>
                <span
                  style={{
                    background: 'rgba(255, 255, 255, 0.05)',
                    padding: '0.2rem 0.6rem',
                    borderRadius: '12px',
                    fontSize: '0.75rem',
                    color: 'var(--text-secondary)',
                  }}
                >
                  ⏱️ {activeLesson.estimatedDuration || 15} mins
                </span>
                <span
                  style={{
                    background: isCurrentCompleted ? 'rgba(52, 211, 153, 0.15)' : 'rgba(197, 155, 39, 0.12)',
                    color: isCurrentCompleted ? '#34d399' : 'var(--gold-primary)',
                    padding: '0.2rem 0.6rem',
                    borderRadius: '12px',
                    fontSize: '0.75rem',
                    fontWeight: 600,
                  }}
                >
                  {isCurrentCompleted ? 'Completed' : 'In Progress'}
                </span>
              </div>
            </div>

            {/* Lesson Title */}
            <h1
              style={{
                fontFamily: 'var(--font-serif)',
                fontSize: '2rem',
                color: 'var(--text-primary)',
                marginBottom: '1.5rem',
                lineHeight: 1.3,
                borderBottom: '1px solid var(--border-color)',
                paddingBottom: '1rem',
              }}
            >
              {activeLesson.title}
            </h1>

            {/* Explanatory Content */}
            <div
              style={{
                color: 'var(--text-primary)',
                fontSize: '1.05rem',
                lineHeight: 1.8,
                marginBottom: '2.5rem',
                whiteSpace: 'pre-line',
              }}
            >
              {activeLesson.content}
            </div>

            {/* Code Example Snippet Box (if provided) */}
            {activeLesson.codeExample && (
              <div
                style={{
                  marginBottom: '2.5rem',
                  border: '1px solid rgba(197, 155, 39, 0.3)',
                  borderRadius: '8px',
                  overflow: 'hidden',
                  background: '#070C1B',
                }}
              >
                <div
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    padding: '0.6rem 1rem',
                    background: 'rgba(11, 19, 43, 0.95)',
                    borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
                    fontSize: '0.8rem',
                  }}
                >
                  <span style={{ color: 'var(--gold-primary)', fontWeight: 600 }}>
                    💻 Hands-On Code Example
                  </span>
                  <button
                    onClick={() => handleCopyCode(activeLesson.codeExample)}
                    style={{
                      background: 'transparent',
                      border: '1px solid rgba(255, 255, 255, 0.2)',
                      color: 'var(--text-secondary)',
                      borderRadius: '4px',
                      padding: '0.2rem 0.6rem',
                      cursor: 'pointer',
                      fontSize: '0.75rem',
                    }}
                  >
                    {copiedCode ? '✅ Copied!' : '📋 Copy Code'}
                  </button>
                </div>
                <pre
                  style={{
                    margin: 0,
                    padding: '1.25rem',
                    overflowX: 'auto',
                    fontFamily: 'Consolas, Monaco, "Courier New", monospace',
                    fontSize: '0.9rem',
                    color: '#e2e8f0',
                    lineHeight: 1.6,
                  }}
                >
                  <code>{activeLesson.codeExample}</code>
                </pre>
              </div>
            )}

            {/* Video / Resource Link (if provided) */}
            {activeLesson.videoUrl && (
              <div
                className="admin-card"
                style={{
                  padding: '1.25rem',
                  marginBottom: '2.5rem',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '1rem',
                }}
              >
                <span style={{ fontSize: '1.5rem' }}>🔗</span>
                <div>
                  <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.9rem' }}>
                    Supplementary Resource
                  </div>
                  <a
                    href={activeLesson.videoUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ color: 'var(--gold-primary)', fontSize: '0.85rem' }}
                  >
                    {activeLesson.videoUrl} &rarr;
                  </a>
                </div>
              </div>
            )}

            {/* Interactive Action Bar (Complete & Prev/Next) */}
            <div
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                paddingTop: '2rem',
                borderTop: '1px solid var(--border-color)',
                marginTop: '3rem',
                flexWrap: 'wrap',
                gap: '1rem',
              }}
            >
              <button
                onClick={() => prevLesson && setActiveLessonId(prevLesson.id)}
                disabled={!prevLesson}
                className="cta-btn cta-btn-secondary"
                style={{ opacity: prevLesson ? 1 : 0.4, cursor: prevLesson ? 'pointer' : 'not-allowed' }}
                id="btn-prev-lesson"
              >
                &larr; Previous Lesson
              </button>

              <button
                onClick={handleToggleComplete}
                disabled={updating}
                className="cta-btn cta-btn-primary"
                style={{
                  background: isCurrentCompleted
                    ? 'rgba(52, 211, 153, 0.2)'
                    : 'linear-gradient(135deg, var(--gold-primary) 0%, var(--gold-secondary) 100%)',
                  border: isCurrentCompleted ? '1px solid #34d399' : 'none',
                  color: isCurrentCompleted ? '#34d399' : '#0B132B',
                  fontWeight: 600,
                  padding: '0.75rem 1.75rem',
                }}
                id="btn-toggle-complete"
              >
                {updating ? 'Updating...' : isCurrentCompleted ? '✅ Mark as Incomplete' : '✓ Mark as Complete'}
              </button>

              <button
                onClick={handleNextLesson}
                disabled={!nextLesson || updating}
                className="cta-btn cta-btn-secondary"
                style={{ opacity: nextLesson ? 1 : 0.4, cursor: nextLesson ? 'pointer' : 'not-allowed' }}
                id="btn-next-lesson"
              >
                {updating ? 'Saving...' : 'Next Lesson \u2192'}
              </button>
            </div>
          </div>
        ) : (
          <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-muted)' }}>
            Select a lesson from the syllabus outline to begin learning.
          </div>
        )}
      </main>
    </div>
  );
}
