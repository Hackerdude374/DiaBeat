import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import Form from './Form';
import About from './About';
import Contact from './Contact';
import DiaBeatLogo from './DiaBeatLogo.png';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <div className="navbar-left">
            <img src={DiaBeatLogo} alt="Logo" className="navbar-logo" />
            <span className="navbar-title">Diabeat</span>
          </div>
          <div className="navbar-right">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
            <Link to="/contact">Contact</Link>
          </div>
        </nav>
        <Routes>
          <Route path="/" element={<Form />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
