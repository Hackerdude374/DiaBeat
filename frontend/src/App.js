import React from 'react';
import diabeatLogo from './DiaBeatLogo.png';
import './App.css';
import Form from './Form';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <nav className="navbar">
          <img src={diabeatLogo} className="navbar-logo" alt="DiaBeatLogo" />
          <div className="navbar-links">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
          </div>
        </nav>
        <Form />
      </header>
    </div>
  );
}

export default App;
