import React, { useState } from "react";
import "../App.css";
import axios from "axios";

function Player() {
  const [User, setUser] = useState("");
  const searchUserOnchange = (event) => {
    setUser(event.target.value);
  };

  const communication = () => {
    const seperator = User.split("#");
    let user;
    axios
      .post("http://127.0.0.1:5000/", { Name: seperator[0], Tag: seperator[1] })
      .then((res) => {
        user = res.data["user"];
        console.log(res.data);
      })
      .catch((error) => {
        console.log(error);
      });
    return (
      <div>
        <span>{user}</span>
      </div>
    );
  };
  const enterKeyPress = (event) => {
    if (event.key === "Enter") {
      communication();
    }
  };

  return (
    <div>
      <input
        placeholder="플레이어 이름 + #태그"
        onChange={searchUserOnchange}
        onKeyDown={enterKeyPress}
        value={User}
      ></input>
    </div>
  );
}
function UserResult() {
  return (
    <div>
      <span></span>
    </div>
  );
}

export { Player, UserResult };
