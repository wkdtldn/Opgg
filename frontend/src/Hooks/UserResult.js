import React from "react";
import Container from "react-bootstrap/Container";
import "../App.css";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
// import Accordion from "react-bootstrap/Accordion";
// import { useAccordionButton } from "react-bootstrap/AccordionButton";
// import Card from "react-bootstrap/Card";

function UserResult(props) {
  const imageTag = (tag, playerIndex, iteamIndex) => {
    if (tag === "tier") {
      if (props.data.user.tier === "") {
        return false;
      } else {
        return `https://opgg-static.akamaized.net/images/medals_new/${props.data.user.tier}.png?image=q_auto,f_webp,w_144&v=1702977255104`;
      }
    } else if (tag === "item") {
      return `https://opgg-static.akamaized.net/meta/images/lol/item/${props.data.match[playerIndex].items[iteamIndex]}.png?image=q_auto,f_webp,w_64,h_64&v=1700641403304`;
      // } else if (tag === "spell") {
    } else if (tag === "champion") {
      return `https://opgg-static.akamaized.net/meta/images/lol/champion/${props.data.match[playerIndex].championName}.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160,h_160&v=1700641403304`;
      // } else if (tag === "runeMain") {
      // } else if (tag === "runeAssist") {
      // }
    }
  };
  const styles = (status, name) => {
    if (status === true) {
      if (name === props.data.user.name) {
        return "playerWrapper minWin";
      } else {
        return "playerWrapper win";
      }
    } else {
      if (name === props.data.user.name) {
        return "playerWrapper minLose";
      } else {
        return "playerWrapper lose";
      }
    }
  };
  if (props.data.user !== "") {
    return (
      <div>
        <div>
          <p>{JSON.stringify(props.data.user)}</p>
          <div></div>
          <div>
            <img src={imageTag("tier")} width="8%" alt="TIER"></img>
          </div>
          <p>{JSON.stringify(props.data.match)}</p>
          <div>
            <h2>전적 들어갈 부분</h2>
            <hr />
            <div>
              {/* Blue Team  == 승리여부 확인과 함께 */}
              <div>
                {/* Player */}
                {props.data.match.map((player, index) => (
                  <Container
                    key={index}
                    className={styles(player.win, player.name)}
                  >
                    {/* Champion */}
                    <img
                      className="playerInfo"
                      src={imageTag("champion", index)}
                      width="32px"
                      height="32px"
                      style={{
                        borderRadius: "150 / 2",
                        overflow: "hidden",
                        borderWidth: "3",
                      }}
                      alt={player.championName}
                    ></img>
                    {/* PlayerName */}
                    <Col>
                      <Row className="playerInfo">{player.name}</Row>
                      <Row className="playerInfo">#{player.tag}</Row>
                    </Col>
                    <span className="playerInfo">
                      {player.kills} / {player.deaths} / {player.assists}
                    </span>
                    {/* Item */}
                  </Container>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    return false;
  }
}
export default UserResult;
