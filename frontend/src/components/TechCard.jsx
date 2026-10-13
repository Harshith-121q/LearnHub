import React from 'react';

/**
 * TechCard component representing a stack technology item.
 */
export default function TechCard({ title, role, description, badge, icon }) {
  return (
    <div className="tech-card" id={`tech-card-${title.toLowerCase().replace(/[^a-z0-9]/g, '-')}`}>
      <div className="tech-card-header">
        <div className="tech-icon-wrapper">
          <span className="tech-icon">{icon}</span>
        </div>
        <span className="tech-badge">{badge}</span>
      </div>
      <h3 className="tech-title">{title}</h3>
      <p className="tech-role">{role}</p>
      <p className="tech-description">{description}</p>
    </div>
  );
}
