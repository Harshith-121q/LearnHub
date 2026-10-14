import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import UserDashboardBanner from '../components/UserDashboardBanner';
import { useAuth } from '../context/useAuth';

export default function LandingPage({ onOpenAuth }) {
  const { isAuthenticated, user } = useAuth();
  const navigate = useNavigate();
  const [activeCourseModal, setActiveCourseModal] = useState(null);

  const handleDashboardClick = () => {
    if (!isAuthenticated) {
      onOpenAuth('register');
      return;
    }
    if (user?.role === 'ROLE_ADMIN') navigate('/admin/dashboard');
    else if (user?.role === 'ROLE_INSTRUCTOR') navigate('/instructor/dashboard');
    else navigate('/student/dashboard');
  };

  const [contactForm, setContactForm] = useState({
    name: '',
    email: '',
    role: 'STUDENT',
    interest: 'Java Programming',
    message: '',
  });
  const [formSubmitted, setFormSubmitted] = useState(false);

  const handleContactSubmit = (e) => {
    e.preventDefault();
    if (!isAuthenticated && onOpenAuth) {
      onOpenAuth('register');
    } else {
      setFormSubmitted(true);
      setTimeout(() => setFormSubmitted(false), 4000);
    }
  };

  const courses = [
    {
      id: 'java-programming',
      title: 'Java Programming',
      subtitle: 'Complete enterprise software development track from JVM fundamentals to advanced OOP.',
      image: '/course-java.jpg',
      icon: '☕',
      badge: 'Core Track',
      level: 'Beginner to Advanced',
      duration: '45+ Hours',
      modules: [
        'Module 1: Java Fundamentals (JDK, JRE, JVM, Variables, Data Types, Operators)',
        'Module 2: Control Flow (Conditional Statements, Switch, For & While Loops, Break/Continue)',
        'Module 3: Methods, Arrays & String Manipulation',
        'Module 4: Object-Oriented Programming (Classes, Inheritance, Polymorphism, Encapsulation)',
        'Module 5: Exception Handling, Generics & Collections Framework',
        'Module 6: Advanced Fundamentals, Multi-threading & Practical Practice',
      ],
    },
    {
      id: 'python-programming',
      title: 'Python Programming',
      subtitle: 'Versatile programming fundamentals, structured data analysis, and modular software engineering.',
      image: null,
      fallbackGradient: 'linear-gradient(135deg, #1e293b, #0f172a)',
      icon: '🐍',
      badge: 'Core Track',
      level: 'Beginner to Advanced',
      duration: '40+ Hours',
      modules: [
        'Module 1: Python Fundamentals (Installation, First Script, Variables, I/O, Operators)',
        'Module 2: Conditional Statements, Loops & Logical Control Flow',
        'Module 3: Strings, Lists, Tuples, Sets & Dictionaries',
        'Module 4: Functions, Lambdas, Scopes & Modular Architecture',
        'Module 5: Object-Oriented Python (Classes, Dunder Methods, Inheritance)',
        'Module 6: File Handling, Exceptions & Practical Software Projects',
      ],
    },
    {
      id: 'software-architecture',
      title: 'Full-Stack Architecture',
      subtitle: 'Modern software engineering principles, robust REST API designs, and scalable database integration.',
      image: null,
      fallbackGradient: 'linear-gradient(135deg, #0f172a, #1a2744)',
      icon: '🏛️',
      badge: 'Engineering',
      level: 'Intermediate',
      duration: '35+ Hours',
      modules: [
        'Module 1: REST API Architectural Principles & HTTP Conventions',
        'Module 2: Spring Boot 3 Core, Controllers & Layered Services',
        'Module 3: Relational Database Persistence with Spring Data JPA & Hibernate',
        'Module 4: Secure Stateless Authentication with Spring Security 6 & JWT',
        'Module 5: Dynamic Client Integration with React.js & State Management',
        'Module 6: Production Engineering, Testing & Deployment Pipelines',
      ],
    },
  ];

  return (
    <div className="prosperum-landing" id="prosperum-landing">
      {/* Cinematic Dark Navy Hero Section */}
      <section className="prosperum-hero" id="hero-section">
        <div className="hero-backdrop-overlay"></div>
        <div className="hero-content-wrapper">
          <div className="hero-grid">
            {/* Left Hero Column */}
            <div className="hero-text-block">
              <div className="hero-gold-pill">
                <span className="gold-pill-dot"></span>
                <span>Structured Programming &amp; Progress Platform</span>
              </div>
              <h1 className="hero-luxury-title">
                Master In-Demand <br />
                <span className="title-serif">Programming Excellence</span>
              </h1>
              <p className="hero-luxury-desc">
                Learn modern Java and Python step by step through structured modules, verified code examples,
                and persistent progress tracking tailored for academic and professional achievement.
              </p>

              <div className="hero-cta-group">
                <button
                  onClick={() => navigate('/courses')}
                  className="btn-gold-primary"
                  id="btn-explore-curriculum"
                >
                  Explore Courses &rarr;
                </button>
                <button
                  onClick={handleDashboardClick}
                  className="btn-navy-outline"
                  id="btn-hero-auth-cta"
                >
                  {isAuthenticated ? 'Open My Workspace &rarr;' : 'Get Started Free'}
                </button>
              </div>
            </div>

            {/* Right Hero Column: Luxury Floating Feature Tiles */}
            <div className="hero-badges-block">
              <div className="floating-tiles-stack">
                <div className="floating-tile tile-growth">
                  <span className="tile-icon">↗</span>
                  <div className="tile-text">
                    <span className="tile-headline">Persistent Progress</span>
                    <span className="tile-sub">Real-time lesson tracking</span>
                  </div>
                </div>

                <div className="floating-tile tile-gold">
                  <span className="tile-icon">👥</span>
                  <div className="tile-text">
                    <span className="tile-headline">Dedicated Instructors</span>
                    <span className="tile-sub">Assigned course monitoring</span>
                  </div>
                </div>

                <div className="floating-tile tile-security">
                  <span className="tile-icon">🛡️</span>
                  <div className="tile-text">
                    <span className="tile-headline">Admin Quality Curated</span>
                    <span className="tile-sub">Structured zero-gap lessons</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* User Status / Quick Actions if authenticated or guest CTA */}
          <div className="hero-banner-slot">
            <UserDashboardBanner onOpenAuth={onOpenAuth} />
          </div>
        </div>
      </section>

      {/* 3 Overlapping Feature Cards */}
      <section className="overlapping-cards-section" id="overview-cards">
        <div className="prosperum-container">
          <div className="overlapping-cards-grid">
            <div className="overlap-card">
              <div className="overlap-card-icon-wrap">
                <span className="overlap-icon">☕</span>
              </div>
              <h3 className="overlap-card-title">Java Programming</h3>
              <p className="overlap-card-desc">
                From JVM fundamentals, data types, and control flow to advanced object-oriented design and collections.
              </p>
              <button
                onClick={() => setActiveCourseModal(courses[0])}
                className="overlap-card-link"
              >
                Discover Curriculum &rarr;
              </button>
            </div>

            <div className="overlap-card">
              <div className="overlap-card-icon-wrap gold-wrap">
                <span className="overlap-icon">🐍</span>
              </div>
              <h3 className="overlap-card-title">Python Programming</h3>
              <p className="overlap-card-desc">
                Master Python syntax, built-in data structures, modular functions, OOP, and real-world scripting projects.
              </p>
              <button
                onClick={() => setActiveCourseModal(courses[1])}
                className="overlap-card-link"
              >
                Discover Curriculum &rarr;
              </button>
            </div>

            <div className="overlap-card">
              <div className="overlap-card-icon-wrap navy-wrap">
                <span className="overlap-icon">📈</span>
              </div>
              <h3 className="overlap-card-title">Persistent Progress</h3>
              <p className="overlap-card-desc">
                Automatic formula-driven progress computation: (completed / total) &times; 100 with seamless cross-session resumption.
              </p>
              <button
                onClick={() => onOpenAuth(isAuthenticated ? 'me' : 'login')}
                className="overlap-card-link"
              >
                View Tracking &rarr;
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Courses / "Our Educational Solutions" Section */}
      <section className="solutions-section" id="solutions-section">
        <div className="prosperum-container">
          <div className="solutions-header">
            <h2 className="solutions-title">Our Learning Solutions</h2>
            <p className="solutions-subtitle">
              Comprehensive, structured educational curriculums authored by platform administrators.
            </p>
          </div>

          <div className="solutions-grid">
            {courses.map((course) => (
              <div key={course.id} className="solution-card">
                <div className="solution-card-media">
                  {course.image ? (
                    <img src={course.image} alt={course.title} className="solution-img" />
                  ) : (
                    <div className="solution-img-fallback" style={{ background: course.fallbackGradient }}>
                      <span className="fallback-symbol">{course.icon}</span>
                      <span className="fallback-tag">{course.badge}</span>
                    </div>
                  )}
                  <div className="solution-badge-overlay">
                    <span className="badge-overlay-icon">{course.icon}</span>
                  </div>
                </div>

                <div className="solution-card-body">
                  <div className="solution-meta-row">
                    <span className="solution-pill">{course.level}</span>
                    <span className="solution-duration">⏱️ {course.duration}</span>
                  </div>
                  <h3 className="solution-card-title">{course.title}</h3>
                  <p className="solution-card-desc">{course.subtitle}</p>

                  <div className="solution-modules-preview">
                    <span className="modules-count-tag">{course.modules.length} Ordered Modules</span>
                    <ul className="modules-bullet-list">
                      {course.modules.slice(0, 3).map((mod, i) => (
                        <li key={i}>{mod.split('(')[0]}</li>
                      ))}
                    </ul>
                  </div>

                  <button
                    onClick={() => setActiveCourseModal(course)}
                    className="solution-btn-gold"
                  >
                    View Curriculum
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div style={{ textAlign: 'center', marginTop: '3rem' }}>
            <button
              onClick={() => navigate('/courses')}
              className="cta-btn cta-btn-primary"
              style={{ padding: '0.85rem 2.25rem', fontSize: '1rem' }}
              id="btn-browse-all-catalog"
            >
              Browse Complete Course Catalog &rarr;
            </button>
          </div>
        </div>
      </section>

      {/* "How We Work" & Quick Registration Section */}
      <section className="how-we-work-section" id="how-we-work-section">
        <div className="prosperum-container">
          <div className="how-we-work-grid">
            {/* Left: How We Work timeline */}
            <div className="how-work-info">
              <h2 className="how-work-title">How We Work</h2>
              <p className="how-work-desc">
                LearnHub delivers a guided learning methodology where topics are ordered sequentially to guarantee comprehension.
              </p>

              <div className="steps-timeline">
                <div className="timeline-step">
                  <div className="step-circle">
                    <span>1</span>
                  </div>
                  <div className="step-content">
                    <h4 className="step-heading">Course Enrollment</h4>
                    <p className="step-desc">
                      Explore published courses in Java or Python. One-click enrollment safeguards against duplicates.
                    </p>
                  </div>
                </div>

                <div className="timeline-connector"></div>

                <div className="timeline-step">
                  <div className="step-circle step-gold">
                    <span>2</span>
                  </div>
                  <div className="step-content">
                    <h4 className="step-heading">Sequential Learning</h4>
                    <p className="step-desc">
                      Study lessons in ordered succession with verified code examples, conceptual explanations, and duration estimates.
                    </p>
                  </div>
                </div>

                <div className="timeline-connector"></div>

                <div className="timeline-step">
                  <div className="step-circle step-navy">
                    <span>3</span>
                  </div>
                  <div className="step-content">
                    <h4 className="step-heading">Persistent Progress</h4>
                    <p className="step-desc">
                      Mark completed lessons to automatically increment your persistent progress percentage and resume instantly.
                    </p>
                  </div>
                </div>
              </div>
            </div>

            {/* Right: Rich Dark Navy Quick Consultation / Registration Box */}
            <div className="consultation-box">
              <div className="consultation-inner">
                <h3 className="consultation-title">Start Learning Today</h3>
                <p className="consultation-subtitle">
                  Create your account to unlock courses, monitor progress, and access learning modules.
                </p>

                {formSubmitted ? (
                  <div className="consultation-success">
                    <span className="success-icon">✓</span>
                    <h4>Account Request Received</h4>
                    <p>Welcome to LearnHub! Please proceed to sign in with your credentials.</p>
                  </div>
                ) : (
                  <form onSubmit={handleContactSubmit} className="consultation-form">
                    <div className="form-row-dual">
                      <div className="form-group-prosperum">
                        <label>Your Name</label>
                        <input
                          type="text"
                          placeholder="e.g. Alex Morgan"
                          value={contactForm.name}
                          onChange={(e) => setContactForm({ ...contactForm, name: e.target.value })}
                          required
                        />
                      </div>
                      <div className="form-group-prosperum">
                        <label>Email Address</label>
                        <input
                          type="email"
                          placeholder="alex@learnhub.com"
                          value={contactForm.email}
                          onChange={(e) => setContactForm({ ...contactForm, email: e.target.value })}
                          required
                        />
                      </div>
                    </div>

                    <div className="form-row-dual">
                      <div className="form-group-prosperum">
                        <label>Platform Role</label>
                        <select
                          value={contactForm.role}
                          onChange={(e) => setContactForm({ ...contactForm, role: e.target.value })}
                        >
                          <option value="STUDENT">Student (Learner)</option>
                          <option value="INSTRUCTOR">Instructor (Course Monitor)</option>
                        </select>
                      </div>
                      <div className="form-group-prosperum">
                        <label>Target Course</label>
                        <select
                          value={contactForm.interest}
                          onChange={(e) => setContactForm({ ...contactForm, interest: e.target.value })}
                        >
                          <option value="Java Programming">Java Programming</option>
                          <option value="Python Programming">Python Programming</option>
                          <option value="Full-Stack Architecture">Full-Stack Architecture</option>
                        </select>
                      </div>
                    </div>

                    <div className="form-group-prosperum">
                      <label>Learning Goals or Questions</label>
                      <textarea
                        rows={3}
                        placeholder="Tell us what you are aiming to build or learn..."
                        value={contactForm.message}
                        onChange={(e) => setContactForm({ ...contactForm, message: e.target.value })}
                      ></textarea>
                    </div>

                    <button type="submit" className="btn-consultation-submit" id="btn-submit-quick-form">
                      {isAuthenticated ? 'Update Preferences' : 'Register & Start Learning'}
                    </button>
                  </form>
                )}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Course Detail Modal */}
      {activeCourseModal && (
        <div className="curriculum-modal-backdrop" onClick={() => setActiveCourseModal(null)}>
          <div className="curriculum-modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-top-bar">
              <div className="modal-title-group">
                <span className="modal-course-icon">{activeCourseModal.icon}</span>
                <div>
                  <h3 className="modal-course-title">{activeCourseModal.title}</h3>
                  <span className="modal-course-sub">{activeCourseModal.level} &bull; {activeCourseModal.duration}</span>
                </div>
              </div>
              <button
                className="modal-close-cross"
                onClick={() => setActiveCourseModal(null)}
              >
                &times;
              </button>
            </div>

            <div className="modal-scroll-area">
              <p className="modal-course-desc">{activeCourseModal.subtitle}</p>

              <h4 className="curriculum-heading">Curriculum Modules &amp; Topics</h4>
              <div className="modal-modules-accordion">
                {activeCourseModal.modules.map((m, idx) => {
                  const parts = m.split(': ');
                  const modTitle = parts[0];
                  const modTopics = parts[1] || '';
                  return (
                    <div key={idx} className="accordion-module-card">
                      <div className="accordion-module-header">
                        <span className="module-number-badge">{idx + 1}</span>
                        <span className="module-name-text">{modTitle}</span>
                      </div>
                      {modTopics && (
                        <p className="module-topics-snippet">{modTopics}</p>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="modal-bottom-actions">
              <button
                className="btn-gold-primary"
                onClick={() => {
                  setActiveCourseModal(null);
                  onOpenAuth(isAuthenticated ? 'me' : 'register');
                }}
              >
                {isAuthenticated ? 'Open Course in Workspace' : 'Enroll in This Course'}
              </button>
              <button
                className="btn-modal-cancel"
                onClick={() => setActiveCourseModal(null)}
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
