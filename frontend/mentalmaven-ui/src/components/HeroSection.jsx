import React from "react";
import { useNavigate } from "react-router-dom";
import "./HeroSection.css";
import therapyimage from "../assets/therapy-img.png";

const HeroSection = () => {
  const navigate = useNavigate();

  return (
    <div className="hero">
      <div className="hero-text">
        <h1>Illness is Illness!</h1>
        <h1>
          Mental Health <span className="highlight">is</span> Health!
        </h1>
        <h2>
          Taking Care of Your Mental Well-Being is Just as Important as
          Physical Health!
        </h2>

        <div className="hero-buttons">
          <button className="register-btn" onClick={() => navigate("/register")}>
            Register Now
          </button>
          <button className="login-btn" onClick={() => navigate("/login")}>
            Log In
          </button>
        </div>
      </div>
      <div className="hero-photo">
        <img className="photo-img" src={therapyimage} alt="Therapy" />
      </div>
    </div>
  );
};

export default HeroSection;
