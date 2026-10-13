import React, { useState, useEffect, useCallback } from 'react';
import TechCard from '../components/TechCard';
import { API_ENDPOINTS } from '../utils/constants';
import { healthService } from '../services/api';

/**
 * LandingPage component for Phase 2: MySQL Database Configuration & Verification.
 */
export default function LandingPage({ healthResult, healthLoading, onRefreshHealth }) {
  const [detailedData, setDetailedData] = useState(null);
  const [loadingDetailed, setLoadingDetailed] = useState(false);

  const fetchDetailedStatus = useCallback(async () => {
    setLoadingDetailed(true);
    const data = await healthService.getHealthStatus();
    setDetailedData(data);
    setLoadingDetailed(false);
  }, []);

  useEffect(() => {
    fetchDetailedStatus();
  }, [fetchDetailedStatus]);

  const handleRefreshAll = () => {
    if (onRefreshHealth) onRefreshHealth();
    fetchDetailedStatus();
  };

  const techStackList = [
    {
      title: 'React.js + Vite',
      role: 'Frontend Layer',
      badge: 'Client',
      icon: '⚛️',
      description: 'Lightning-fast modern React single-page application built on Vite with modular design.',
    },
    {
      title: 'Spring Boot 3',
      role: 'Backend REST API',
      badge: 'Server',
      icon: '🍃',
      description: 'Robust Java enterprise backend with structured controllers, services, and global exception handling.',
    },
    {
      title: 'Spring Data JPA',
      role: 'Object-Relational Mapping',
      badge: 'ORM',
      icon: '🏛️',
      description: 'Hibernate-powered persistence layer with declarative repositories and entity lifecycle auditing.',
    },
    {
      title: 'MySQL 8.0',
      role: 'Relational Database',
      badge: 'Database',
      icon: '🐬',
      description: 'Structured relational data storage configured safely through environment variables (DB_URL, DB_USERNAME, DB_PASSWORD).',
    },
    {
      title: 'Jakarta Validation',
      role: 'Data Validation',
      badge: 'Security',
      icon: '🛡️',
      description: 'Standard declarative input validation for REST requests with centralized error formatting.',
    },
    {
      title: 'Spring Boot DevTools',
      role: 'Developer Experience',
      badge: 'Tooling',
      icon: '⚡',
      description: 'Automatic restart and live-reload capabilities for streamlined full-stack development cycles.',
    },
  ];

  const packagesList = [
    { name: 'config', desc: 'CORS & global application configuration beans' },
    { name: 'controller', desc: 'REST endpoints and HTTP request handlers' },
    { name: 'service', desc: 'Business logic layer and database health validation' },
    { name: 'repository', desc: 'Spring Data JPA data access interfaces' },
    { name: 'entity', desc: 'JPA database entity definitions' },
    { name: 'dto', desc: 'Data Transfer Objects & request/response payloads' },
    { name: 'exception', desc: 'Centralized exception handlers & custom errors' },
  ];

  const dbState = detailedData?.data?.database?.status || 'CHECKING';
  const isDbUp = dbState === 'UP';

  return (
    <div className="landing-page" id="landing-page">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-pill">
          <span className="pill-dot"></span>
          <span>Phase 2 &mdash; MySQL Database Connectivity</span>
        </div>
        <h1 className="hero-heading">
          Skill Learning &amp; <span className="gradient-text">Assessment Platform</span>
        </h1>
        <p className="hero-subheading">
          Welcome to <strong>LearnHub</strong>. Phase 2 configures and validates Spring Boot integration with MySQL 8.0
          and Spring Data JPA with resilient health verification.
        </p>

        {/* Live Connectivity Test Card */}
        <div className="connectivity-card" id="connectivity-card">
          <div className="connectivity-card-header">
            <div className="card-title-group">
              <span className="card-indicator-icon">🔌</span>
              <div>
                <h2 className="card-title">Full-Stack &amp; Database Health Status</h2>
                <p className="card-subtitle">Endpoints: <code>GET {API_ENDPOINTS.HEALTH}</code> &bull; <code>GET {API_ENDPOINTS.HEALTH_STATUS}</code></p>
              </div>
            </div>
            <button
              onClick={handleRefreshAll}
              disabled={healthLoading || loadingDetailed}
              className="refresh-btn"
              id="btn-recheck-health"
            >
              {healthLoading || loadingDetailed ? 'Testing...' : '🔄 Re-check Health'}
            </button>
          </div>

          <div className="connectivity-body">
            <div className="metrics-row">
              <div className="metric-item">
                <span className="metric-label">Backend API</span>
                <span className={`metric-value ${healthResult?.success ? 'text-success' : 'text-danger'}`}>
                  {healthResult?.success ? 'ONLINE (200)' : 'OFFLINE'}
                </span>
              </div>
              <div className="metric-item">
                <span className="metric-label">MySQL Database</span>
                <span className={`metric-value ${isDbUp ? 'text-success' : 'text-danger'}`}>
                  {isDbUp ? `CONNECTED (${detailedData?.data?.database?.database || 'MySQL'})` : 'UNAVAILABLE'}
                </span>
              </div>
              <div className="metric-item">
                <span className="metric-label">API Latency</span>
                <span className="metric-value">{healthResult?.latencyMs ? `${healthResult.latencyMs} ms` : '--'}</span>
              </div>
              <div className="metric-item">
                <span className="metric-label">Overall Health</span>
                <span className={`metric-value ${isDbUp ? 'text-success' : 'text-danger'}`}>
                  {detailedData?.data?.status || (healthResult?.success ? 'UP' : 'DOWN')}
                </span>
              </div>
            </div>

            {/* Health Payload Details */}
            {detailedData && (
              <div className="payload-box">
                <div className="payload-box-header">
                  <span>Server Response Envelope (<code>/api/health/status</code> &mdash; HTTP {detailedData.statusCode || 200})</span>
                  <button
                    onClick={fetchDetailedStatus}
                    disabled={loadingDetailed}
                    className="detail-toggle-btn"
                    id="btn-fetch-details"
                  >
                    {loadingDetailed ? 'Refreshing...' : 'Refresh Status Envelope'}
                  </button>
                </div>
                <pre className="payload-json" id="payload-health-json">
                  {JSON.stringify(detailedData, null, 2)}
                </pre>
              </div>
            )}

            {detailedData && !isDbUp && (
              <div className="connection-error-box">
                <p className="error-title">⚠️ MySQL Database is not yet connected</p>
                <p className="error-desc">
                  {detailedData?.data?.database?.message || 'Unable to establish database connection.'}
                  <br />
                  Make sure <code>learnhub_db</code> is created and valid credentials are supplied via <code>DB_USERNAME</code> and <code>DB_PASSWORD</code>.
                </p>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Tech Stack Breakdown */}
      <section className="tech-section">
        <div className="section-header">
          <h2 className="section-title">Integrated Technology Stack</h2>
          <p className="section-subtitle">
            Enterprise-grade, robust components configured for scalability and modularity.
          </p>
        </div>
        <div className="tech-grid" id="tech-stack-grid">
          {techStackList.map((item) => (
            <TechCard
              key={item.title}
              title={item.title}
              role={item.role}
              badge={item.badge}
              icon={item.icon}
              description={item.description}
            />
          ))}
        </div>
      </section>

      {/* Backend Architecture Structure */}
      <section className="architecture-section">
        <div className="section-header">
          <h2 className="section-title">Backend Architecture Layers</h2>
          <p className="section-subtitle">
            Organized strictly into clean, maintainable Spring Boot packages.
          </p>
        </div>
        <div className="packages-grid">
          {packagesList.map((pkg) => (
            <div key={pkg.name} className="package-item">
              <span className="package-badge">com.learnhub.{pkg.name}</span>
              <p className="package-desc">{pkg.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Database Connection Instructions */}
      <section className="db-notice-section">
        <div className="db-notice-card">
          <div className="db-notice-icon">🗄️</div>
          <div className="db-notice-content">
            <h3 className="db-notice-title">MySQL Database Configuration Guide</h3>
            <p className="db-notice-text">
              The project is configured with Spring Data JPA and MySQL Connector. To connect your MySQL database:
            </p>
            <ol className="db-steps-list">
              <li>Open MySQL / MySQL Workbench and create the database: <code>CREATE DATABASE IF NOT EXISTS learnhub_db;</code></li>
              <li>Set your MySQL password in <code>backend/src/main/resources/application.properties</code> or via environment variable <code>$env:DB_PASSWORD="your_password"</code>.</li>
              <li>Re-check health or restart the backend: <code>.\mvnw.cmd spring-boot:run</code>.</li>
            </ol>
          </div>
        </div>
      </section>
    </div>
  );
}
