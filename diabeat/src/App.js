import logo from './logo.svg';
import './App.css';
import { User, SecondUser } from './User';

function App() {
  const name = "Matt";
  const age = 29;
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      
        <User name={name} age={age} />
        <SecondUser />
      </header>
    </div>
  );
}

export default App;
