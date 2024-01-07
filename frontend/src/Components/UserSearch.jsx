import React from "react";
import "../App.css";
import axios from "axios";
import UserResult from "./UserResult";

class Player extends React.Component {
  constructor(props) {
    super(props);
    this.state = { text: "" };
  }
  handleChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value,
    });
    console.log(this.state.text);
  };
  onEnterKeyDown = (event) => {
    if (event.key === "Enter") {
      this.getUserData();
    }
  };
  getUserData = (props) => {
    const seperator = this.state.text.split("#");
    axios
      .post("http://127.0.0.1:5000/", { Name: seperator[0], Tag: seperator[1] })
      .then((res) => {
        props = res.data;
        console.log(props);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  render() {
    return (
      <div>
        <input
          onChange={this.handleChange}
          name="text"
          onKeyDown={this.onEnterKeyDown}
          placeholder="플레이어 이름 + #태그"
        ></input>
        <div>
          <UserResult />
        </div>
      </div>
    );
  }
}

export default Player;
