import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { adminService, courseService } from '../../services/api';

export default function CourseCurriculumEditorPage() {
  const { id: courseId } = useParams();
  const navigate = useNavigate();

  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState(null);

  // Module modal state
  const [showModuleModal, setShowModuleModal] = useState(false);
  const [editingModule, setEditingModule] = useState(null);
  const [moduleForm, setModuleForm] = useState({ title: '', description: '' });

  // Lesson modal state
  const [showLessonModal, setShowLessonModal] = useState(false);
  const [targetModuleId, setTargetModuleId] = useState(null);
  const [editingLesson, setEditingLesson] = useState(null);
  const [lessonForm, setLessonForm] = useState({
    title: '',
    content: '',
    codeExample: '',
    videoUrl: '',
    durationMinutes: 15,
  });

  const [saving, setSaving] = useState(false);

  useEffect(() => {
    loadCurriculum();
  }, [courseId]);

  const loadCurriculum = async () => {
    setLoading(true);
    const res = await courseService.getCourseById(courseId);
    if (res.success && res.data) {
      setCourse(res.data);
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to load curriculum' });
    }
    setLoading(false);
  };

  // Module Actions
  const openAddModule = () => {
    setEditingModule(null);
    setModuleForm({ title: '', description: '' });
    setShowModuleModal(true);
  };

  const openEditModule = (mod) => {
    setEditingModule(mod);
    setModuleForm({ title: mod.title, description: mod.description || '' });
    setShowModuleModal(true);
  };

  const handleModuleSubmit = async (e) => {
    e.preventDefault();
    if (!moduleForm.title.trim()) return;

    setSaving(true);
    const apiCall = editingModule
      ? adminService.updateModule(editingModule.id, moduleForm)
      : adminService.addModule(courseId, moduleForm);

    const res = await apiCall;
    setSaving(false);

    if (res.success) {
      setShowModuleModal(false);
      setMessage({ type: 'success', text: editingModule ? 'Module updated' : 'Module added to curriculum' });
      setTimeout(() => setMessage(null), 3000);
      loadCurriculum();
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to save module' });
    }
  };

  const handleDeleteModule = async (moduleId, title) => {
    if (!window.confirm(`Delete module "${title}" and all its contained lessons?`)) return;
    const res = await adminService.deleteModule(moduleId);
    if (res.success) {
      setMessage({ type: 'success', text: `Module "${title}" deleted` });
      setTimeout(() => setMessage(null), 3000);
      loadCurriculum();
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to delete module' });
    }
  };

  const handleMoveModule = async (index, direction) => {
    if (!course?.modules) return;
    const mods = [...course.modules];
    const targetIndex = index + direction;
    if (targetIndex < 0 || targetIndex >= mods.length) return;

    const temp = mods[index];
    mods[index] = mods[targetIndex];
    mods[targetIndex] = temp;

    const orderedIds = mods.map((m) => m.id);
    const res = await adminService.reorderModules(courseId, orderedIds);
    if (res.success) {
      loadCurriculum();
    }
  };

  // Lesson Actions
  const openAddLesson = (moduleId) => {
    setTargetModuleId(moduleId);
    setEditingLesson(null);
    setLessonForm({
      title: '',
      content: '',
      codeExample: '',
      videoUrl: '',
      durationMinutes: 15,
    });
    setShowLessonModal(true);
  };

  const openEditLesson = (lesson, moduleId) => {
    setTargetModuleId(moduleId);
    setEditingLesson(lesson);
    setLessonForm({
      title: lesson.title,
      content: lesson.content,
      codeExample: lesson.codeExample || '',
      videoUrl: lesson.videoUrl || '',
      durationMinutes: lesson.durationMinutes || lesson.estimatedDuration || 15,
    });
    setShowLessonModal(true);
  };

  const handleLessonSubmit = async (e) => {
    e.preventDefault();
    if (!lessonForm.title.trim() || !lessonForm.content.trim()) return;

    setSaving(true);
    const payload = {
      ...lessonForm,
      durationMinutes: Number(lessonForm.durationMinutes) || 15,
    };

    const apiCall = editingLesson
      ? adminService.updateLesson(editingLesson.id, payload)
      : adminService.addLesson(targetModuleId, payload);

    const res = await apiCall;
    setSaving(false);

    if (res.success) {
      setShowLessonModal(false);
      setMessage({ type: 'success', text: editingLesson ? 'Lesson updated' : 'Lesson added to module' });
      setTimeout(() => setMessage(null), 3000);
      loadCurriculum();
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to save lesson' });
    }
  };

  const handleDeleteLesson = async (lessonId, title) => {
    if (!window.confirm(`Delete lesson "${title}"?`)) return;
    const res = await adminService.deleteLesson(lessonId);
    if (res.success) {
      setMessage({ type: 'success', text: `Lesson "${title}" deleted` });
      setTimeout(() => setMessage(null), 3000);
      loadCurriculum();
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to delete lesson' });
    }
  };

  const handleMoveLesson = async (moduleId, lessons, index, direction) => {
    const list = [...lessons];
    const targetIndex = index + direction;
    if (targetIndex < 0 || targetIndex >= list.length) return;

    const temp = list[index];
    list[index] = list[targetIndex];
    list[targetIndex] = temp;

    const orderedIds = list.map((l) => l.id);
    const res = await adminService.reorderLessons(moduleId, orderedIds);
    if (res.success) {
      loadCurriculum();
    }
  };

  if (loading) {
    return (
      <div className="section-container" style={{ padding: '6rem 2rem', textAlign: 'center' }}>
        <div className="spinner" style={{ margin: '0 auto 1.5rem', width: 40, height: 40 }}></div>
        <p style={{ color: 'var(--text-muted)' }}>Loading curriculum architect...</p>
      </div>
    );
  }

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Breadcrumb */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          <Link to="/admin/dashboard" style={{ color: 'var(--text-secondary)' }}>Admin Dashboard</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <Link to="/admin/courses" style={{ color: 'var(--text-secondary)' }}>Courses</Link>
          <span style={{ margin: '0 0.5rem' }}>/</span>
          <span style={{ color: 'var(--gold-primary)' }}>{course?.title || 'Curriculum'}</span>
        </div>

        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button
            onClick={() => navigate('/admin/instructors')}
            className="cta-btn cta-btn-secondary"
            style={{ padding: '0.5rem 1rem', fontSize: '0.85rem' }}
          >
            👥 Assign Instructors
          </button>
          <button
            onClick={openAddModule}
            className="cta-btn cta-btn-primary"
            style={{ padding: '0.5rem 1.25rem', fontSize: '0.85rem' }}
            id="btn-add-module"
          >
            ➕ Add Module
          </button>
        </div>
      </div>

      {/* Header Info */}
      <div className="admin-card" style={{ padding: '1.75rem', marginBottom: '2rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1rem' }}>
          <div>
            <span style={{ fontSize: '0.75rem', color: 'var(--gold-primary)', fontWeight: 600, textTransform: 'uppercase' }}>
              {course?.category} &bull; {course?.difficultyLevel}
            </span>
            <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.85rem', color: 'var(--text-primary)', margin: '0.25rem 0' }}>
              {course?.title}
            </h1>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', margin: 0 }}>
              Curriculum Architect: Define modules, lessons, explanations, and programming examples in sequential order.
            </p>
          </div>

          <span
            style={{
              padding: '0.25rem 0.75rem',
              borderRadius: '20px',
              fontSize: '0.8rem',
              fontWeight: 600,
              background: course?.status === 'PUBLISHED' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(197, 155, 39, 0.15)',
              color: course?.status === 'PUBLISHED' ? '#34d399' : 'var(--gold-primary)',
            }}
          >
            {course?.status}
          </span>
        </div>
      </div>

      {/* Message alert */}
      {message && (
        <div className={`auth-alert ${message.type === 'success' ? 'success-alert' : 'error-alert'}`} style={{ marginBottom: '2rem' }}>
          <span>{message.type === 'success' ? '✅' : '⚠️'}</span>
          <span>{message.text}</span>
        </div>
      )}

      {/* Modules and Lessons Hierarchy */}
      {course?.modules?.length === 0 ? (
        <div className="admin-card" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
          <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>📖</span>
          <h3 style={{ fontFamily: 'var(--font-serif)', color: 'var(--text-primary)', marginBottom: '0.5rem' }}>
            No Modules Created Yet
          </h3>
          <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
            Start structuring this course by adding its first thematic module.
          </p>
          <button onClick={openAddModule} className="cta-btn cta-btn-primary">
            ➕ Add First Module &rarr;
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
          {course?.modules?.map((mod, modIdx) => (
            <div
              key={mod.id}
              className="admin-card"
              style={{
                padding: '1.75rem',
                border: '1px solid rgba(197, 155, 39, 0.25)',
                background: 'rgba(11, 19, 43, 0.7)',
              }}
            >
              {/* Module Header with Reorder & Edit controls */}
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  marginBottom: '1rem',
                  paddingBottom: '0.75rem',
                  borderBottom: '1px solid var(--border-color)',
                  flexWrap: 'wrap',
                  gap: '0.75rem',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                    <button
                      onClick={() => handleMoveModule(modIdx, -1)}
                      disabled={modIdx === 0}
                      style={{
                        background: 'transparent',
                        border: 'none',
                        color: modIdx === 0 ? 'rgba(255,255,255,0.1)' : 'var(--text-secondary)',
                        cursor: modIdx === 0 ? 'not-allowed' : 'pointer',
                        padding: 0,
                        fontSize: '0.75rem',
                      }}
                      title="Move module up"
                    >
                      ▲
                    </button>
                    <button
                      onClick={() => handleMoveModule(modIdx, 1)}
                      disabled={modIdx === course.modules.length - 1}
                      style={{
                        background: 'transparent',
                        border: 'none',
                        color: modIdx === course.modules.length - 1 ? 'rgba(255,255,255,0.1)' : 'var(--text-secondary)',
                        cursor: modIdx === course.modules.length - 1 ? 'not-allowed' : 'pointer',
                        padding: 0,
                        fontSize: '0.75rem',
                      }}
                      title="Move module down"
                    >
                      ▼
                    </button>
                  </div>

                  <div>
                    <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--gold-primary)', margin: 0 }}>
                      {mod.title}
                    </h2>
                    {mod.description && (
                      <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', margin: '0.25rem 0 0' }}>
                        {mod.description}
                      </p>
                    )}
                  </div>
                </div>

                <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
                  <button
                    onClick={() => openAddLesson(mod.id)}
                    className="cta-btn cta-btn-primary"
                    style={{ padding: '0.4rem 0.85rem', fontSize: '0.8rem' }}
                    id={`btn-add-lesson-mod-${mod.id}`}
                  >
                    ➕ Add Lesson
                  </button>
                  <button
                    onClick={() => openEditModule(mod)}
                    className="cta-btn cta-btn-secondary"
                    style={{ padding: '0.4rem 0.65rem', fontSize: '0.8rem' }}
                    title="Edit module name"
                  >
                    ✏️
                  </button>
                  <button
                    onClick={() => handleDeleteModule(mod.id, mod.title)}
                    className="cta-btn cta-btn-secondary"
                    style={{ padding: '0.4rem 0.65rem', fontSize: '0.8rem', color: '#f87171' }}
                    title="Delete module"
                  >
                    🗑️
                  </button>
                </div>
              </div>

              {/* Lessons within this module */}
              {mod.lessons?.length === 0 ? (
                <div style={{ padding: '1rem', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem' }}>
                  No lessons in this module yet.{' '}
                  <button
                    onClick={() => openAddLesson(mod.id)}
                    className="text-link-btn"
                    style={{ color: 'var(--gold-primary)', fontSize: '0.85rem' }}
                  >
                    Add lesson now &rarr;
                  </button>
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                  {mod.lessons?.map((les, lesIdx) => (
                    <div
                      key={les.id}
                      style={{
                        padding: '1rem',
                        background: 'rgba(0, 0, 0, 0.3)',
                        border: '1px solid var(--border-color)',
                        borderRadius: '8px',
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'flex-start',
                        flexWrap: 'wrap',
                        gap: '1rem',
                      }}
                    >
                      <div style={{ display: 'flex', gap: '0.75rem', flex: '1 1 300px' }}>
                        {/* Lesson reorder arrows */}
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px', paddingTop: '4px' }}>
                          <button
                            onClick={() => handleMoveLesson(mod.id, mod.lessons, lesIdx, -1)}
                            disabled={lesIdx === 0}
                            style={{
                              background: 'transparent',
                              border: 'none',
                              color: lesIdx === 0 ? 'rgba(255,255,255,0.1)' : 'var(--text-secondary)',
                              cursor: lesIdx === 0 ? 'not-allowed' : 'pointer',
                              padding: 0,
                              fontSize: '0.7rem',
                            }}
                            title="Move lesson up"
                          >
                            ▲
                          </button>
                          <button
                            onClick={() => handleMoveLesson(mod.id, mod.lessons, lesIdx, 1)}
                            disabled={lesIdx === mod.lessons.length - 1}
                            style={{
                              background: 'transparent',
                              border: 'none',
                              color: lesIdx === mod.lessons.length - 1 ? 'rgba(255,255,255,0.1)' : 'var(--text-secondary)',
                              cursor: lesIdx === mod.lessons.length - 1 ? 'not-allowed' : 'pointer',
                              padding: 0,
                              fontSize: '0.7rem',
                            }}
                            title="Move lesson down"
                          >
                            ▼
                          </button>
                        </div>

                        <div style={{ flexGrow: 1 }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.35rem' }}>
                            <span style={{ fontWeight: 600, color: 'var(--text-primary)', fontSize: '0.95rem' }}>
                              {lesIdx + 1}. {les.title}
                            </span>
                            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                              ⏱️ {les.estimatedDuration || les.durationMinutes || 15} mins
                            </span>
                            {les.codeExample && (
                              <span style={{ fontSize: '0.7rem', background: 'rgba(59, 130, 246, 0.15)', color: '#60a5fa', padding: '0.1rem 0.4rem', borderRadius: '4px' }}>
                                💻 Code Example
                              </span>
                            )}
                          </div>

                          <div style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', lineHeight: 1.5, maxHeight: 60, overflow: 'hidden' }}>
                            {les.content}
                          </div>
                        </div>
                      </div>

                      <div style={{ display: 'flex', gap: '0.5rem', flexShrink: 0 }}>
                        <button
                          onClick={() => openEditLesson(les, mod.id)}
                          className="cta-btn cta-btn-secondary"
                          style={{ padding: '0.35rem 0.65rem', fontSize: '0.8rem' }}
                          title="Edit lesson"
                        >
                          ✏️ Edit
                        </button>
                        <button
                          onClick={() => handleDeleteLesson(les.id, les.title)}
                          className="cta-btn cta-btn-secondary"
                          style={{ padding: '0.35rem 0.65rem', fontSize: '0.8rem', color: '#f87171' }}
                          title="Delete lesson"
                        >
                          🗑️
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Module Add / Edit Modal */}
      {showModuleModal && (
        <div className="modal-backdrop" onClick={() => setShowModuleModal(false)}>
          <div className="modal-container" onClick={(e) => e.stopPropagation()} style={{ maxWidth: 500 }}>
            <button className="modal-close-btn" onClick={() => setShowModuleModal(false)}>&times;</button>
            <div className="modal-header">
              <h2 className="modal-title" style={{ fontFamily: 'var(--font-serif)' }}>
                {editingModule ? 'Edit Module' : 'Add Curriculum Module'}
              </h2>
            </div>
            <form onSubmit={handleModuleSubmit} className="auth-form">
              <div className="form-group">
                <label className="form-label">Module Title *</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="e.g. Module 1: Core Fundamentals and Syntax"
                  value={moduleForm.title}
                  onChange={(e) => setModuleForm({ ...moduleForm, title: e.target.value })}
                  required
                />
              </div>
              <div className="form-group">
                <label className="form-label">Description / Summary</label>
                <textarea
                  className="form-input"
                  rows="3"
                  placeholder="Overview of topics addressed in this module..."
                  value={moduleForm.description}
                  onChange={(e) => setModuleForm({ ...moduleForm, description: e.target.value })}
                ></textarea>
              </div>
              <button type="submit" disabled={saving} className="submit-auth-btn" id="btn-save-module">
                {saving ? 'Saving...' : editingModule ? 'Update Module' : 'Create Module'}
              </button>
            </form>
          </div>
        </div>
      )}

      {/* Lesson Add / Edit Modal */}
      {showLessonModal && (
        <div className="modal-backdrop" onClick={() => setShowLessonModal(false)}>
          <div
            className="modal-container"
            onClick={(e) => e.stopPropagation()}
            style={{ maxWidth: 700, maxHeight: '90vh', overflowY: 'auto' }}
          >
            <button className="modal-close-btn" onClick={() => setShowLessonModal(false)}>&times;</button>
            <div className="modal-header">
              <h2 className="modal-title" style={{ fontFamily: 'var(--font-serif)' }}>
                {editingLesson ? 'Edit Lesson' : 'Add New Lesson'}
              </h2>
              <p className="modal-subtitle">
                Provide instructional explanation, executable code examples, and estimated duration.
              </p>
            </div>
            <form onSubmit={handleLessonSubmit} className="auth-form">
              <div className="form-group">
                <label className="form-label">Lesson Title *</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="e.g. Object-Oriented Inheritance & Polymorphism"
                  value={lessonForm.title}
                  onChange={(e) => setLessonForm({ ...lessonForm, title: e.target.value })}
                  required
                />
              </div>

              <div className="form-group">
                <label className="form-label">Estimated Duration (Minutes)</label>
                <input
                  type="number"
                  min="1"
                  className="form-input"
                  value={lessonForm.durationMinutes}
                  onChange={(e) => setLessonForm({ ...lessonForm, durationMinutes: e.target.value })}
                />
              </div>

              <div className="form-group">
                <label className="form-label">Instructional Content / Lesson Explanation *</label>
                <textarea
                  className="form-input"
                  rows="6"
                  placeholder="Detailed instructional explanation and conceptual breakdowns..."
                  value={lessonForm.content}
                  onChange={(e) => setLessonForm({ ...lessonForm, content: e.target.value })}
                  required
                ></textarea>
              </div>

              <div className="form-group">
                <label className="form-label">Hands-On Programming Code Example</label>
                <textarea
                  className="form-input"
                  rows="5"
                  style={{ fontFamily: 'Consolas, monospace', fontSize: '0.85rem' }}
                  placeholder="// Executable programming sample\npublic class Demo {\n    public static void main(String[] args) {\n        ...\n    }\n}"
                  value={lessonForm.codeExample}
                  onChange={(e) => setLessonForm({ ...lessonForm, codeExample: e.target.value })}
                ></textarea>
              </div>

              <div className="form-group">
                <label className="form-label">Video or External Resource URL (Optional)</label>
                <input
                  type="url"
                  className="form-input"
                  placeholder="https://example.com/resources/lesson-video"
                  value={lessonForm.videoUrl}
                  onChange={(e) => setLessonForm({ ...lessonForm, videoUrl: e.target.value })}
                />
              </div>

              <button type="submit" disabled={saving} className="submit-auth-btn" id="btn-save-lesson">
                {saving ? 'Saving...' : editingLesson ? 'Update Lesson' : 'Add Lesson to Module'}
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
