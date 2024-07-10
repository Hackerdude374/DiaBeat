import React from 'react';
import './App.css';
import Form from './Form';
import DiaBeatLogo from './DiaBeatLogo.png';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <nav className="navbar">
          <div className="navbar-left">
            <img src={DiaBeatLogo} alt="Logo" className="navbar-logo" />
            <span className="navbar-title">Diabeat</span>
          </div>
          <div className="navbar-right">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
          </div>
        </nav>
        <Form />
      </header>
    </div>
  );
}

export default App;
