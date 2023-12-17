import React, { useState } from "react";
import "../App.css";
import axios from "axios";

function ChampionInput() {
  const [champion, setChampion] = useState("");
  const searchChampion = (event) => {
    setChampion(event.target.value);
  };
  return (
    <div>
      <input
        placeholder="챔피언 검색"
        value={champion}
        onChange={searchChampion}
      ></input>
    </div>
  );
}
function ChampionResult() {
  return (
    <div>
      <span></span>
    </div>
  );
}
export { ChampionInput, ChampionResult };
