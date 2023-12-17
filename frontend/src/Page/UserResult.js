import React from "react";
import "../App.css";
import axios from "axios";

axios.create({
  baseURL: "http://127.0.0.1:5000",
  withCredentials: true,
});

function UserResulf() {
  return (
    <button
      onClick={axios
        .get(baseURL)
        .then((res) => {
          console.log(res.data);
        })
        .catch(() => {
          console.error();
        })}
    ></button>
  );
}
