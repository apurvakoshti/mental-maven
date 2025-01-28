import React from 'react';
import './SurveyPrompt.css'; // Optional: Add styles here if needed
import Navbar from '../components/Navbar';
const SurveyPrompt = () => {
  return (
    <div className="survey-prompt-container">
      <div className="survey-content">
        <h1>Thank you for joining Mental Maven!</h1>
        <button className="survey-button">Take a Survey</button>
        <h2>This survey will take just a few minutes but can make a big difference!</h2>
      </div>
    </div>
  );
};

export default SurveyPrompt;