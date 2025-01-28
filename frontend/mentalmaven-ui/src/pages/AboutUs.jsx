import React from "react";
import "./AboutUs.css";

const AboutUs = () => {
  return (
    <div className="about-us">
      <div className="logo-container">
        <img src="./logo.jpg" alt="MentalMaven Logo" className="logo" />
      </div>
      <div className="content">
        <h1>MentalMaven</h1>
        <p>
         The logo symbolizes the importance of emotional well-being and the connection between mental and emotional health. 
         The word "MentalMaven" stands for "Mental Companion." We provide a platform that helps raise awareness about mental health by offering therapy sessions along with useful tips and strategies.
        </p>

      </div>
    </div>
  );
};

export default AboutUs;
