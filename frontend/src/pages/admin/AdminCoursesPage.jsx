import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { adminService } from '../../services/api';

export default function AdminCoursesPage() {
  const navigate = useNavigate();

  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [editingCourse, setEditingCourse] = useState(null);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState(null);

  // Form State
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    category: 'Java',
    difficultyLevel: 'BEGINNER',
    estimatedDuration: 60,
    learningObjectives: '',
    prerequisites: '',
  });

  useEffect(() => {
    loadCourses();
  }, []);

  const loadCourses = async () => {
    setLoading(true);
    const res = await adminService.getAllCourses();
    if (res.success && res.data) {
      setCourses(res.data);
    }
    setLoading(false);
  };

  const openCreateModal = () => {
    setEditingCourse(null);
    setFormData({
      title: '',
      description: '',
      category: 'Java',
      difficultyLevel: 'BEGINNER',
      estimatedDuration: 60,
      learningObjectives: '',
      prerequisites: '',
    });
    setShowCreateModal(true);
  };

  const openEditModal = (course) => {
    setEditingCourse(course);
    setFormData({
      title: course.title || '',
      description: course.description || '',
      category: course.category || 'Java',
      difficultyLevel: course.difficultyLevel || 'BEGINNER',
      estimatedDuration: course.estimatedDuration || 60,
      learningObjectives: course.learningObjectives || '',
      prerequisites: course.prerequisites || '',
    });
    setShowCreateModal(true);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.title.trim()) {
      setMessage({ type: 'error', text: 'Course title is required' });
      return;
    }

    setSaving(true);
    const payload = {
      ...formData,
      estimatedDuration: Number(formData.estimatedDuration) || 60,
    };

    const apiCall = editingCourse
      ? adminService.updateCourse(editingCourse.id, payload)
      : adminService.createCourse(payload);

    const res = await apiCall;
    setSaving(false);

    if (res.success) {
      setShowCreateModal(false);
      setMessage({
        type: 'success',
        text: editingCourse ? 'Course updated successfully' : 'New course draft created successfully',
      });
      setTimeout(() => setMessage(null), 3500);
      loadCourses();
    } else {
      setMessage({ type: 'error', text: res.error || 'Operation failed' });
    }
  };

  const handlePublishToggle = async (course) => {
    const isPublished = course.status === 'PUBLISHED';
    const apiCall = isPublished ? adminService.unpublishCourse(course.id) : adminService.publishCourse(course.id);
    const res = await apiCall;

    if (res.success) {
      setMessage({ type: 'success', text: `Course "${course.title}" ${isPublished ? 'unpublished to draft' : 'published to catalog'}` });
      setTimeout(() => setMessage(null), 3500);
      loadCourses();
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to update status' });
      setTimeout(() => setMessage(null), 4000);
    }
  };

  const handleDelete = async (courseId, title) => {
    if (!window.confirm(`Delete draft course "${title}"? This cannot be undone.`)) return;
    const res = await adminService.deleteCourse(courseId);
    if (res.success) {
      setMessage({ type: 'success', text: `Course "${title}" deleted` });
      setTimeout(() => setMessage(null), 3500);
      loadCourses();
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to delete course' });
      setTimeout(() => setMessage(null), 4000);
    }
  };

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2.5rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginBottom: '0.4rem' }}>
            <Link to="/admin/dashboard" style={{ color: 'var(--text-secondary)' }}>Admin Dashboard</Link>
            <span style={{ margin: '0 0.5rem' }}>/</span>
            <span style={{ color: 'var(--gold-primary)' }}>Courses Management</span>
          </div>
          <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2.25rem', color: 'var(--text-primary)', margin: 0 }}>
            Course Authoring &amp; Management
          </h1>
        </div>

        <button
          onClick={openCreateModal}
          className="cta-btn cta-btn-primary"
          style={{ padding: '0.75rem 1.5rem' }}
          id="btn-create-course"
        >
          ➕ Author New Course
        </button>
      </div>

      {/* Message Banner */}
      {message && (
        <div className={`auth-alert ${message.type === 'success' ? 'success-alert' : 'error-alert'}`} style={{ marginBottom: '2rem' }}>
          <span>{message.type === 'success' ? '✅' : '⚠️'}</span>
          <span>{message.text}</span>
        </div>
      )}

      {/* Course List */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '3rem 0' }}>
          <div className="spinner" style={{ margin: '0 auto 1rem', width: 36, height: 36 }}></div>
          <p style={{ color: 'var(--text-muted)' }}>Loading course catalog...</p>
        </div>
      ) : courses.length === 0 ? (
        <div className="admin-card" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>🛠️</span>
          <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
            No Courses Created Yet
          </h3>
          <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
            Create your first production course track to start organizing modules and curriculum.
          </p>
          <button onClick={openCreateModal} className="cta-btn cta-btn-primary">
            Author New Course &rarr;
          </button>
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(360px, 1fr))', gap: '2rem' }}>
          {courses.map((course) => {
            const isPublished = course.status === 'PUBLISHED';
            const isDraft = course.status === 'DRAFT';

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
                </div>

                <h3 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--text-primary)', marginBottom: '0.75rem', lineHeight: 1.3 }}>
                  {course.title}
                </h3>

                <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6, marginBottom: '1.25rem', flexGrow: 1 }}>
                  {course.description?.length > 130 ? `${course.description.substring(0, 130)}...` : course.description}
                </p>

                <div
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    padding: '0.75rem 0',
                    borderTop: '1px solid var(--border-color)',
                    borderBottom: '1px solid var(--border-color)',
                    marginBottom: '1.25rem',
                    fontSize: '0.8rem',
                    color: 'var(--text-muted)',
                  }}
                >
                  <span>📖 {course.moduleCount || 0} Modules</span>
                  <span>⏱️ {course.estimatedDuration} mins</span>
                  <span>👥 {course.enrolledCount || 0} Students</span>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', marginBottom: '0.75rem' }}>
                  <button
                    onClick={() => navigate(`/admin/courses/${course.id}/curriculum`)}
                    className="cta-btn cta-btn-primary"
                    style={{ padding: '0.6rem', fontSize: '0.85rem', textAlign: 'center' }}
                  >
                    📖 Curriculum ({course.moduleCount || 0})
                  </button>

                  <button
                    onClick={() => openEditModal(course)}
                    className="cta-btn cta-btn-secondary"
                    style={{ padding: '0.6rem', fontSize: '0.85rem', textAlign: 'center' }}
                  >
                    ✏️ Edit Info
                  </button>
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <button
                    onClick={() => handlePublishToggle(course)}
                    className="text-link-btn"
                    style={{ fontSize: '0.8rem', color: isPublished ? '#f87171' : 'var(--gold-primary)' }}
                  >
                    {isPublished ? 'Unpublish to Draft' : 'Publish to Catalog'}
                  </button>

                  {isDraft && (
                    <button
                      onClick={() => handleDelete(course.id, course.title)}
                      className="text-link-btn"
                      style={{ fontSize: '0.8rem', color: '#f87171' }}
                    >
                      Delete Draft
                    </button>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Create / Edit Course Modal */}
      {showCreateModal && (
        <div className="modal-backdrop" onClick={() => setShowCreateModal(false)}>
          <div
            className="modal-container"
            onClick={(e) => e.stopPropagation()}
            style={{ maxWidth: 650, maxHeight: '90vh', overflowY: 'auto' }}
          >
            <button className="modal-close-btn" onClick={() => setShowCreateModal(false)}>
              &times;
            </button>

            <div className="modal-header">
              <h2 className="modal-title" style={{ fontFamily: 'var(--font-serif)' }}>
                {editingCourse ? 'Edit Course Information' : 'Author New Course'}
              </h2>
              <p className="modal-subtitle">
                Define the track structure, difficulty, prerequisites, and learning objectives.
              </p>
            </div>

            <form onSubmit={handleSubmit} className="auth-form">
              <div className="form-group">
                <label className="form-label">Course Title *</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="e.g. Master Enterprise Java with Spring Boot"
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  required
                />
              </div>

              <div className="form-row-2">
                <div className="form-group">
                  <label className="form-label">Category *</label>
                  <select
                    className="form-input"
                    value={formData.category}
                    onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                  >
                    <option value="Java">Java</option>
                    <option value="Python">Python</option>
                    <option value="Web Development">Web Development</option>
                    <option value="Cloud Architecture">Cloud Architecture</option>
                  </select>
                </div>

                <div className="form-group">
                  <label className="form-label">Difficulty Level *</label>
                  <select
                    className="form-input"
                    value={formData.difficultyLevel}
                    onChange={(e) => setFormData({ ...formData, difficultyLevel: e.target.value })}
                  >
                    <option value="BEGINNER">Beginner</option>
                    <option value="INTERMEDIATE">Intermediate</option>
                    <option value="ADVANCED">Advanced</option>
                  </select>
                </div>
              </div>

              <div className="form-group">
                <label className="form-label">Estimated Total Duration (Minutes)</label>
                <input
                  type="number"
                  min="10"
                  className="form-input"
                  value={formData.estimatedDuration}
                  onChange={(e) => setFormData({ ...formData, estimatedDuration: e.target.value })}
                />
              </div>

              <div className="form-group">
                <label className="form-label">Course Description *</label>
                <textarea
                  className="form-input"
                  rows="3"
                  placeholder="Provide an overview of the curriculum and technologies covered..."
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  required
                ></textarea>
              </div>

              <div className="form-group">
                <label className="form-label">Learning Objectives (What will students achieve?)</label>
                <textarea
                  className="form-input"
                  rows="2"
                  placeholder="- Master OOP principles\n- Architect robust REST APIs\n- Write unit tests"
                  value={formData.learningObjectives}
                  onChange={(e) => setFormData({ ...formData, learningObjectives: e.target.value })}
                ></textarea>
              </div>

              <div className="form-group">
                <label className="form-label">Prerequisites</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="e.g. Basic programming familiarity, computer literacy"
                  value={formData.prerequisites}
                  onChange={(e) => setFormData({ ...formData, prerequisites: e.target.value })}
                />
              </div>

              <button
                type="submit"
                disabled={saving}
                className="submit-auth-btn"
                style={{ marginTop: '1rem' }}
                id="btn-save-course"
              >
                {saving ? 'Saving...' : editingCourse ? 'Update Course' : 'Create Course Draft'}
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
