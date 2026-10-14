import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { adminService } from '../../services/api';
import { useAuth } from '../../context/useAuth';

export default function AdminDashboardPage() {
  const { user } = useAuth();
  const navigate = useNavigate();

  const [stats, setStats] = useState(null);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionMsg, setActionMsg] = useState(null);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    setLoading(true);
    const [statsRes, coursesRes] = await Promise.all([
      adminService.getStats(),
      adminService.getAllCourses(),
    ]);

    if (statsRes.success) setStats(statsRes.data);
    if (coursesRes.success) setCourses(coursesRes.data || []);
    setLoading(false);
  };

  const handlePublishToggle = async (course) => {
    const isPublished = course.status === 'PUBLISHED';
    const apiCall = isPublished ? adminService.unpublishCourse(course.id) : adminService.publishCourse(course.id);
    const res = await apiCall;

    if (res.success) {
      setActionMsg({ type: 'success', text: `Course "${course.title}" ${isPublished ? 'unpublished to draft' : 'published to catalog'}` });
      setTimeout(() => setActionMsg(null), 3500);
      loadDashboardData();
    } else {
      setActionMsg({ type: 'error', text: res.error || 'Failed to update course status' });
      setTimeout(() => setActionMsg(null), 4000);
    }
  };

  const handleArchive = async (courseId, title) => {
    if (!window.confirm(`Are you sure you want to archive course "${title}"?`)) return;
    const res = await adminService.archiveCourse(courseId);
    if (res.success) {
      setActionMsg({ type: 'success', text: `Course "${title}" archived` });
      setTimeout(() => setActionMsg(null), 3500);
      loadDashboardData();
    } else {
      setActionMsg({ type: 'error', text: res.error || 'Failed to archive course' });
      setTimeout(() => setActionMsg(null), 4000);
    }
  };

  const handleDelete = async (courseId, title) => {
    if (!window.confirm(`Are you sure you want to delete draft course "${title}"? This cannot be undone.`)) return;
    const res = await adminService.deleteCourse(courseId);
    if (res.success) {
      setActionMsg({ type: 'success', text: `Course "${title}" deleted` });
      setTimeout(() => setActionMsg(null), 3500);
      loadDashboardData();
    } else {
      setActionMsg({ type: 'error', text: res.error || 'Failed to delete course' });
      setTimeout(() => setActionMsg(null), 4000);
    }
  };

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1.5rem', marginBottom: '2.5rem' }}>
        <div>
          <div className="greeting-pill" style={{ marginBottom: '0.5rem' }}>
            <span className="live-dot"></span>
            <span>Administrator Control Center</span>
          </div>
          <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2.25rem', color: 'var(--text-primary)', margin: 0 }}>
            System Governance &bull; <span className="gold-text">{user?.fullName || 'Administrator'}</span>
          </h1>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.4rem', fontSize: '0.95rem' }}>
            Manage technical curriculum, author structured lessons, and coordinate faculty assignments.
          </p>
        </div>

        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <button
            onClick={() => navigate('/admin/courses')}
            className="cta-btn cta-btn-primary"
            style={{ padding: '0.75rem 1.25rem', fontSize: '0.9rem' }}
            id="btn-admin-manage-courses"
          >
            ➕ Manage &amp; Author Courses
          </button>
          <button
            onClick={() => navigate('/admin/instructors')}
            className="cta-btn cta-btn-secondary"
            style={{ padding: '0.75rem 1.25rem', fontSize: '0.9rem' }}
            id="btn-admin-manage-instructors"
          >
            👥 Assign Instructors
          </button>
        </div>
      </div>

      {/* Action Notification */}
      {actionMsg && (
        <div
          className={`auth-alert ${actionMsg.type === 'success' ? 'success-alert' : 'error-alert'}`}
          style={{ marginBottom: '2rem' }}
        >
          <span>{actionMsg.type === 'success' ? '✅' : '⚠️'}</span>
          <span>{actionMsg.text}</span>
        </div>
      )}

      {/* Metrics Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '1.25rem', marginBottom: '3rem' }}>
        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>📚</div>
          <div style={{ fontSize: '1.85rem', fontWeight: 700, color: 'var(--text-primary)' }}>
            {stats?.totalCourses || courses.length}
          </div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Total Courses</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>🟢</div>
          <div style={{ fontSize: '1.85rem', fontWeight: 700, color: '#34d399' }}>
            {stats?.publishedCourses || courses.filter((c) => c.status === 'PUBLISHED').length}
          </div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Published Tracks</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>📝</div>
          <div style={{ fontSize: '1.85rem', fontWeight: 700, color: 'var(--gold-primary)' }}>
            {stats?.draftCourses || courses.filter((c) => c.status === 'DRAFT').length}
          </div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Draft Curricula</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>👨‍🏫</div>
          <div style={{ fontSize: '1.85rem', fontWeight: 700, color: 'var(--text-primary)' }}>
            {stats?.totalInstructors || 0}
          </div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Faculty Instructors</div>
        </div>

        <div className="admin-card" style={{ padding: '1.5rem', textAlign: 'center' }}>
          <div style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>🎓</div>
          <div style={{ fontSize: '1.85rem', fontWeight: 700, color: 'var(--gold-primary)' }}>
            {stats?.totalEnrollments || 0}
          </div>
          <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Active Enrollments</div>
        </div>
      </div>

      {/* Courses Catalog Table */}
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
          <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.5rem', color: 'var(--text-primary)', margin: 0 }}>
            Course Curriculums &amp; Lifecycle Management
          </h2>
          <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
            {courses.length} Courses in System
          </span>
        </div>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '3rem 0' }}>
            <div className="spinner" style={{ margin: '0 auto 1rem', width: 36, height: 36 }}></div>
            <p style={{ color: 'var(--text-muted)' }}>Loading course registries...</p>
          </div>
        ) : courses.length === 0 ? (
          <div className="admin-card" style={{ textAlign: 'center', padding: '3rem 2rem' }}>
            <span style={{ fontSize: '2.5rem', display: 'block', marginBottom: '0.75rem' }}>📚</span>
            <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
              No Courses Created Yet
            </h3>
            <button onClick={() => navigate('/admin/courses')} className="cta-btn cta-btn-primary">
              Create First Course &rarr;
            </button>
          </div>
        ) : (
          <div className="admin-card" style={{ padding: 0, overflow: 'hidden' }}>
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.875rem' }}>
                <thead>
                  <tr style={{ background: 'rgba(255, 255, 255, 0.03)', borderBottom: '1px solid var(--border-color)' }}>
                    <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Course</th>
                    <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Category &bull; Level</th>
                    <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Status</th>
                    <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Structure</th>
                    <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600 }}>Assigned Faculty</th>
                    <th style={{ padding: '1rem 1.25rem', color: 'var(--gold-primary)', fontWeight: 600, textAlign: 'right' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {courses.map((course) => {
                    const isPublished = course.status === 'PUBLISHED';
                    const isDraft = course.status === 'DRAFT';
                    const isArchived = course.status === 'ARCHIVED';

                    return (
                      <tr key={course.id} style={{ borderBottom: '1px solid var(--border-color)' }}>
                        <td style={{ padding: '1rem 1.25rem' }}>
                          <div style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.95rem' }}>
                            {course.title}
                          </div>
                          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                            ID: #{course.id} &bull; ⏱️ {course.estimatedDuration} mins
                          </div>
                        </td>

                        <td style={{ padding: '1rem 1.25rem' }}>
                          <span style={{ color: 'var(--gold-primary)', fontWeight: 500 }}>{course.category}</span>
                          <span style={{ color: 'var(--text-muted)', margin: '0 0.35rem' }}>&bull;</span>
                          <span style={{ color: 'var(--text-secondary)' }}>{course.difficultyLevel}</span>
                        </td>

                        <td style={{ padding: '1rem 1.25rem' }}>
                          <span
                            style={{
                              padding: '0.2rem 0.6rem',
                              borderRadius: '12px',
                              fontSize: '0.75rem',
                              fontWeight: 600,
                              background: isPublished
                                ? 'rgba(52, 211, 153, 0.15)'
                                : isDraft
                                ? 'rgba(197, 155, 39, 0.15)'
                                : 'rgba(148, 163, 184, 0.15)',
                              color: isPublished ? '#34d399' : isDraft ? 'var(--gold-primary)' : '#94a3b8',
                            }}
                          >
                            {course.status}
                          </span>
                        </td>

                        <td style={{ padding: '1rem 1.25rem', color: 'var(--text-secondary)' }}>
                          <div>{course.moduleCount || 0} Modules</div>
                          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                            {course.lessonCount || 0} Lessons &bull; {course.enrolledCount || 0} Learners
                          </div>
                        </td>

                        <td style={{ padding: '1rem 1.25rem' }}>
                          {course.assignedInstructors && course.assignedInstructors.length > 0 ? (
                            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.35rem' }}>
                              {course.assignedInstructors.map((inst) => (
                                <span
                                  key={inst.id}
                                  style={{
                                    fontSize: '0.75rem',
                                    background: 'rgba(255, 255, 255, 0.05)',
                                    padding: '0.15rem 0.5rem',
                                    borderRadius: '10px',
                                    color: 'var(--text-secondary)',
                                  }}
                                >
                                  👨‍🏫 {inst.fullName}
                                </span>
                              ))}
                            </div>
                          ) : (
                            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Unassigned</span>
                          )}
                        </td>

                        <td style={{ padding: '1rem 1.25rem', textAlign: 'right' }}>
                          <div style={{ display: 'flex', gap: '0.5rem', justifyContent: 'flex-end', flexWrap: 'wrap' }}>
                            <button
                              onClick={() => navigate(`/admin/courses/${course.id}/curriculum`)}
                              className="cta-btn cta-btn-primary"
                              style={{ padding: '0.35rem 0.75rem', fontSize: '0.75rem' }}
                              title="Add & organize modules and lessons"
                              id={`btn-curriculum-${course.id}`}
                            >
                              📖 Curriculum
                            </button>

                            <button
                              onClick={() => handlePublishToggle(course)}
                              className="cta-btn cta-btn-secondary"
                              style={{ padding: '0.35rem 0.75rem', fontSize: '0.75rem' }}
                              id={`btn-publish-toggle-${course.id}`}
                            >
                              {isPublished ? 'Unpublish' : 'Publish'}
                            </button>

                            {!isArchived && (
                              <button
                                onClick={() => handleArchive(course.id, course.title)}
                                className="cta-btn cta-btn-secondary"
                                style={{ padding: '0.35rem 0.6rem', fontSize: '0.75rem', color: '#94a3b8' }}
                                title="Archive course"
                              >
                                Archive
                              </button>
                            )}

                            {isDraft && (
                              <button
                                onClick={() => handleDelete(course.id, course.title)}
                                className="cta-btn cta-btn-secondary"
                                style={{ padding: '0.35rem 0.6rem', fontSize: '0.75rem', color: '#f87171' }}
                                title="Delete draft course"
                              >
                                🗑️
                              </button>
                            )}
                          </div>
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
    </div>
  );
}
