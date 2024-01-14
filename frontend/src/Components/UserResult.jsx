import React from "react";

function UserResult(props) {
  let Tag;
  const imageTag = (target) => {
    if (typeof props.data.user.target === "string") {
      Tag = props.data.user.target.toLowerCase();
    } else {
      Tag = props.data.user.target;
    }
    if (target === "tier") {
      return `https://opgg-static.akamaized.net/images/medals_new/${Tag}.png?image=q_auto,f_webp,w_144&v=1702977255104`;
    }
  };
  if (props.data.user !== "") {
    return (
      <div>
        <div>
          <img
            src={imageTag("tier")}
            width="50%"
            alt="BRONZE
          "
          ></img>
        </div>
      </div>
    );
  } else {
    return false;
  }
}
export default UserResult;
