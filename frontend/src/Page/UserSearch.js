import React, { useState } from "react";
import "../App.css";

function UserInput() {
  const [User, setUser] = useState("");
  const searchUser = (event) => {
    setUser(event.target.value);
  };
  return (
    <div>
      <input
        placeholder="닉네임 검색"
        value={User}
        onChange={searchUser}
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

export { UserInput, UserResult };
