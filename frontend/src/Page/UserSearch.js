import React, { useState } from "react";
import "../App.css";
import axios from "axios";

function UserInput() {
  const [User, setUser] = useState("");
  const searchUserOnchange = (event) => {
    setUser(event.target.value);
    console.log(User);
  };
  const communication = () => {
    const seperator = User.split("#");
    console.log(seperator);
    axios
      .post("http://127.0.0.1:5000/", { Name: seperator[0], Tag: seperator[1] })
      .then((res) => {
        console.log(res.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div>
      <input
        placeholder="플레이어 이름 + #테그"
        onChange={searchUserOnchange}
        value={User}
      ></input>
      <button onClick={communication}>button</button>
    </div>
  );
}
function UserResult() {
  const Stats visualization

  return (
    <div>
      <span></span>
    </div>
  );
}

export { UserInput, UserResult };
