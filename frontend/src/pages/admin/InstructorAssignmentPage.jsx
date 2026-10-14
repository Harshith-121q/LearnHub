import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { adminService, courseService } from '../../services/api';

export default function InstructorAssignmentPage() {
  const [courses, setCourses] = useState([]);
  const [instructors, setInstructors] = useState([]);
  const [selectedCourseId, setSelectedCourseId] = useState('');
  const [selectedCourseDetail, setSelectedCourseDetail] = useState(null);
  const [selectedInstructorId, setSelectedInstructorId] = useState('');
  const [loading, setLoading] = useState(true);
  const [assigning, setAssigning] = useState(false);
  const [message, setMessage] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  useEffect(() => {
    if (selectedCourseId) {
      loadCourseDetail(selectedCourseId);
    } else {
      setSelectedCourseDetail(null);
    }
  }, [selectedCourseId]);

  const loadData = async () => {
    setLoading(true);
    const [coursesRes, instRes] = await Promise.all([
      adminService.getAllCourses(),
      adminService.getInstructors(),
    ]);

    if (coursesRes.success && coursesRes.data) {
      setCourses(coursesRes.data);
      if (coursesRes.data.length > 0) {
        setSelectedCourseId(String(coursesRes.data[0].id));
      }
    }
    if (instRes.success && instRes.data) {
      setInstructors(instRes.data);
    }
    setLoading(false);
  };

  const loadCourseDetail = async (courseId) => {
    const res = await courseService.getCourseById(courseId);
    if (res.success && res.data) {
      setSelectedCourseDetail(res.data);
    }
  };

  const handleAssign = async (e) => {
    e.preventDefault();
    if (!selectedCourseId || !selectedInstructorId) {
      setMessage({ type: 'error', text: 'Please select an instructor to assign' });
      return;
    }

    setAssigning(true);
    const res = await adminService.assignInstructor(selectedCourseId, Number(selectedInstructorId));
    setAssigning(false);

    if (res.success) {
      setMessage({ type: 'success', text: 'Instructor assigned successfully' });
      setTimeout(() => setMessage(null), 3500);
      setSelectedInstructorId('');
      loadCourseDetail(selectedCourseId);
      adminService.getAllCourses().then((r) => r.success && setCourses(r.data));
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to assign instructor' });
    }
  };

  const handleRemove = async (instructorId, name) => {
    if (!window.confirm(`Remove instructor ${name} from this course?`)) return;

    const res = await adminService.removeInstructor(selectedCourseId, instructorId);
    if (res.success) {
      setMessage({ type: 'success', text: `Instructor ${name} removed from course` });
      setTimeout(() => setMessage(null), 3500);
      loadCourseDetail(selectedCourseId);
      adminService.getAllCourses().then((r) => r.success && setCourses(r.data));
    } else {
      setMessage({ type: 'error', text: res.error || 'Failed to remove instructor' });
    }
  };

  const assignedInstructorIds = new Set(
    selectedCourseDetail?.assignedInstructors?.map((i) => i.id) || []
  );

  const availableToAssign = instructors.filter((i) => !assignedInstructorIds.has(i.id));

  return (
    <div className="section-container" style={{ padding: '3rem 2rem 5rem' }}>
      {/* Breadcrumb */}
      <div style={{ marginBottom: '2rem', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
        <Link to="/admin/dashboard" style={{ color: 'var(--text-secondary)' }}>Admin Dashboard</Link>
        <span style={{ margin: '0 0.5rem' }}>/</span>
        <span style={{ color: 'var(--gold-primary)' }}>Instructor Assignments</span>
      </div>

      {/* Header */}
      <div style={{ marginBottom: '2.5rem' }}>
        <h1 style={{ fontFamily: 'var(--font-serif)', fontSize: '2.25rem', color: 'var(--text-primary)', margin: 0 }}>
          Faculty &amp; Instructor Course Assignments
        </h1>
        <p style={{ color: 'var(--text-secondary)', marginTop: '0.4rem', fontSize: '0.95rem' }}>
          Assign qualified faculty members to oversee course delivery and monitor student cohorts.
        </p>
      </div>

      {/* Message alert */}
      {message && (
        <div className={`auth-alert ${message.type === 'success' ? 'success-alert' : 'error-alert'}`} style={{ marginBottom: '2rem' }}>
          <span>{message.type === 'success' ? '✅' : '⚠️'}</span>
          <span>{message.text}</span>
        </div>
      )}

      {loading ? (
        <div style={{ textAlign: 'center', padding: '3rem 0' }}>
          <div className="spinner" style={{ margin: '0 auto 1rem', width: 36, height: 36 }}></div>
          <p style={{ color: 'var(--text-muted)' }}>Loading instructor roster...</p>
        </div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '2rem' }}>
          {/* Left Column: Select Course & Assign Form */}
          <div className="admin-card" style={{ padding: '2rem' }}>
            <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--text-primary)', marginBottom: '1.25rem' }}>
              Assign Faculty Member
            </h2>

            <div className="form-group">
              <label className="form-label">Select Course</label>
              <select
                className="form-input"
                value={selectedCourseId}
                onChange={(e) => setSelectedCourseId(e.target.value)}
              >
                {courses.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.title} ({c.category})
                  </option>
                ))}
              </select>
            </div>

            <form onSubmit={handleAssign}>
              <div className="form-group">
                <label className="form-label">Select Registered Instructor</label>
                <select
                  className="form-input"
                  value={selectedInstructorId}
                  onChange={(e) => setSelectedInstructorId(e.target.value)}
                  disabled={availableToAssign.length === 0}
                >
                  <option value="">
                    {availableToAssign.length === 0
                      ? 'All available instructors are already assigned'
                      : '-- Select Instructor --'}
                  </option>
                  {availableToAssign.map((inst) => (
                    <option key={inst.id} value={inst.id}>
                      👨‍🏫 {inst.fullName} (@{inst.username})
                    </option>
                  ))}
                </select>
              </div>

              <button
                type="submit"
                disabled={assigning || !selectedInstructorId}
                className="cta-btn cta-btn-primary"
                style={{ width: '100%', marginTop: '0.75rem', padding: '0.75rem' }}
                id="btn-confirm-assign"
              >
                {assigning ? 'Assigning...' : 'Assign Instructor to Course &rarr;'}
              </button>
            </form>
          </div>

          {/* Right Column: Currently Assigned Instructors */}
          <div className="admin-card" style={{ padding: '2rem' }}>
            <h2 style={{ fontFamily: 'var(--font-serif)', fontSize: '1.25rem', color: 'var(--gold-primary)', marginBottom: '0.5rem' }}>
              Assigned Instructors
            </h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: '1.5rem' }}>
              Faculty members assigned to <strong>{selectedCourseDetail?.title || 'Selected Course'}</strong>
            </p>

            {selectedCourseDetail?.assignedInstructors?.length === 0 ? (
              <div style={{ textAlign: 'center', padding: '2.5rem 1rem', color: 'var(--text-muted)' }}>
                <span style={{ fontSize: '2.5rem', display: 'block', marginBottom: '0.5rem' }}>👥</span>
                No instructors currently assigned to this course.
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                {selectedCourseDetail?.assignedInstructors?.map((inst) => (
                  <div
                    key={inst.id}
                    style={{
                      padding: '1rem',
                      background: 'rgba(0, 0, 0, 0.25)',
                      border: '1px solid var(--border-color)',
                      borderRadius: '8px',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                      <div className="greeting-avatar" style={{ width: 36, height: 36, fontSize: '0.9rem' }}>
                        {inst.fullName ? inst.fullName[0] : 'I'}
                      </div>
                      <div>
                        <div style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{inst.fullName}</div>
                        <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                          @{inst.username} &bull; {inst.email}
                        </div>
                      </div>
                    </div>

                    <button
                      onClick={() => handleRemove(inst.id, inst.fullName)}
                      className="cta-btn cta-btn-secondary"
                      style={{ padding: '0.35rem 0.65rem', fontSize: '0.75rem', color: '#f87171' }}
                      title="Remove from course"
                    >
                      Remove
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
