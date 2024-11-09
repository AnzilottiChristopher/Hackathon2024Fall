//import logo from './logo.svg';
import './web_resources/App.css';
import logo from './web_resources/img_small.png'; // Tell webpack this JS file uses this image

function App() {
  return (
    // this is our A P P!
    <div className="App">
      <header className="App-header">
        <img src={logo} alt="HACKQU"/><br/>
        <h1 class="display-1">Fall 2024 Hackathon</h1><br/>
        <p>
          <b>Team Name</b>: Let's make a game!<br/>
          <b>Team Members</b>: Christopher Anzilotti, Paul Zegarek, Peter Zegarek
        </p>
        <button id="gameButton" type="button" class="btn btn-info">Let's see our game!</button>
      </header>
      <div class="main">
        <h2><b>Our Theme: </b>Sustainability</h2>
        <h3>Game Summary</h3>
        <p>
          This game is a side-scrolling platformer where you play as a hero and act to save the world.
          You will talk to animals and fight enemies, using abilities inspired by our planet Earth!
        </p>
        <h3>Target Audience</h3>
        <p>
          Our target audience consists of people who enjoy side-scrolling platfomers, such as Mario, Sonic, or any big game that fits the criteria.
        </p>
        <h3>Controls</h3>
        <ul>
        <li><b>A: </b>Move Left</li>
        <li><b>D: </b>Move Right</li>
        <li><b>Space: </b>Jump</li>
        </ul>
      </div>
    </div>
    /*
    OLD HEADER

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
    */
  );
}

export default App;
