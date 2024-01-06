import "./App.css";
import { ChampionInput, ChampionResult } from "./Page/ChampionSearch";
import { Player, UserResult } from "./Page/UserSearch";
import React from "react";

class App extends React.Component {
  render() {
    return (
      <div className="outer">
        <div>
          <ChampionInput />
          <ChampionResult />
        </div>
        <div>
          <Player />
          <UserResult />
        </div>
      </div>
    );
  }
}

export default App;
