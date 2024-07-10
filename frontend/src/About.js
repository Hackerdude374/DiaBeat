import React from 'react';
import './About.css';

function About() {
  const profiles = [
    {
      name: 'Joe He',
      location: 'Staten Island',
      description: 'AI Specialist with experience in predictive modeling and data analysis.',
      linkedin: 'https://www.linkedin.com/in/joe-he/'
    },
    {
      name: 'Robert Le',
      location: 'Staten Island',
      description: 'Software Engineer with a background in full stack development.',
      linkedin: 'https://www.linkedin.com/in/robert-le/'
    },
    {
      name: 'Keon Brown',
      location: 'Staten Island',
      description: 'Data Scientist with a focus on machine learning and statistical analysis.',
      linkedin: 'https://www.linkedin.com/in/keon-brown/'
    },
    {
      name: 'Ashwin Anil',
      location: 'Staten Island',
      description: 'DevOps Engineer with expertise in cloud infrastructure and CI/CD pipelines.',
      linkedin: 'https://www.linkedin.com/in/ashwin-anil/'
    }
  ];

  return (
    <div className="about-container">
      <h1>About Us</h1>
      <div className="profiles">
        {profiles.map((profile, index) => (
          <div key={index} className="profile-card">
            <img
              src={`https://via.placeholder.com/150?text=${profile.name.split(' ')[0]}`}
              alt={profile.name}
              className="profile-pic"
            />
            <h2>{profile.name}</h2>
            <p>{profile.location}</p>
            <p>{profile.description}</p>
            <a href={profile.linkedin} target="_blank" rel="noopener noreferrer">
              View LinkedIn
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default About;
