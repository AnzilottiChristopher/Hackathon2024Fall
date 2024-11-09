//import logo from './logo.svg';
import './web_resources/App.css';
import logo from './web_resources/img_small.png'; // Tell webpack this JS file uses this image

import img1 from './web_resources/message.png'; // Story
import scr1 from './web_resources/screen1.png';
import scr2 from './web_resources/screen2.png';
import winScreen from './web_resources/winScreen.png';

function App() {
  return (
    // this is our A P P!
    <div className="App">
      <header className="App-header">
        <img src={logo} alt="HACKQU"/><br/>
        <h1 class="display-1">Our Fall 2024 Hackathon Project!</h1><br/>
        <p>
          <b>Team Name</b>: Let's make a game!<br/>
          <b>Team Members</b>: Christopher Anzilotti, Paul Zegarek, Peter Zegarek
        </p>
        <button id="gameButton" type="button" class="btn btn-info">Let's see our game!</button>
      </header>
      <div class="main">
        <h2><b>Our Theme: </b>Sustainability</h2>
        <p>We had to come up with a solution that will help people conserve natural resources and protect global ecosystems to support health and wellbeing, now and in the future</p>
        <h3>Game Summary</h3>
        <p>
          This game is a side-scrolling platformer where you play as a hero and act to save the world.
          You will fight pollution slime enemies, and collect light orbs that will save the world from pollution.
        </p>
        <h3>Target Audience</h3>
        <p>
          Our target audience consists of people who enjoy side-scrolling platfomers, such as Mario, Sonic, or any big game that fits the criteria.
          However, our message is applicable to every person in the world, not just those who enjoy platformers.
        </p>
        <h3>Controls</h3>
        <ul>
        <li><b>A: </b>Move Left</li>
        <li><b>D: </b>Move Right</li>
        <li><b>Space: </b>Jump</li>
        </ul>
        <h3>Inspiration</h3>
        <p>The game was inspired by events that we know contribute to the global climate crisis many of us are facing in different places of the world.
          With climate change being such an important issue in our world, we wanted to address it in a way that would be fun for people who play video games.
          It is meant to be a fun experience, that shows the player the damage that pollution can cause.
        </p>
        <h3>Screenshots</h3>
        <img class="responsive" src={img1} alt=""/><img class="responsive" src={scr1} alt=""/><img class="responsive" src={scr2} alt=""/><img class="responsive" src={winScreen} alt=""/>
        <h3>Future Plans</h3>
        <p>If we had some more time to work on this game, we would have added better animations. We also would have made the story more fleshed out and meaningful.
        </p>
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
