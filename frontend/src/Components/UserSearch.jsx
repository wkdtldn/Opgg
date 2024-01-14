import React, { useState, useEffect } from "react";
import axios from "axios";
import UserResult from "./UserResult";

function Player() {
  const [text, setText] = useState("");
  const [userData, setUserData] = useState({ user: "", match: "" });
  useEffect(() => {
    console.log(userData);
  }, [userData]);
  const handleChange = (event) => {
    setText(event.target.value);
    console.log(text);
  };
  const onEnterKeyDown = (event) => {
    if (event.key === "Enter") {
      getUserData();
    }
  };
  const getUserData = () => {
    if (text.includes("#") === true) {
      const separator = text.split("#");
      axios
        .post("http://127.0.0.1:5000/", {
          Name: separator[0],
          Tag: separator[1],
        })
        .then((res) => {
          if (res.data.Result === true) {
            setUserData({ user: res.data.user, match: res.data.match });
          } else {
            alert("해당 유저가 존재하지 않습니다");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      alert("해당 유저가 존재하지 않습니다");
    }
  };
  return (
    <div>
      <input
        onChange={handleChange}
        name="text"
        onKeyDown={onEnterKeyDown}
        placeholder="플레이어 이름 + #태그"
      ></input>
      <div>
        <UserResult data={userData} />
      </div>
    </div>
  );
}

export default Player;
