import React, { useState } from "react";
import "../App.css";
import axios from "axios";

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
      <button
        onClick={axios
          .get(baseURL)
          .then((res) => {
            console.log(res.data);
          })
          .catch(() => {
            console.error();
          })}
      >
        button
      </button>
    </div>
  );
}
function UserResult() {
  axios.create({
    baseURL: "http://127.0.0.1:5000",
    withCredentials: true,
  });

  return (
    <div>
      <span></span>
    </div>
  );
}

export { UserInput, UserResult };
