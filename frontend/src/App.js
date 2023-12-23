import "./App.css";
import { ChampionInput, ChampionResult } from "./Page/ChampionSearch";
import { UserInput, UserResult } from "./Page/UserSearch";
function App() {
  return (
    <div>
      <div>
        <ChampionInput />
        <ChampionResult />
      </div>
      <br />
      <div>
        <UserInput />
        <UserResult />
      </div>
    </div>
  );
}

export default App;
