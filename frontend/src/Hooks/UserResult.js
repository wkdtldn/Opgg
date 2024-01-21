import React from "react";
import "../App.css";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
// import Accordion from "react-bootstrap/Accordion";
// import { useAccordionButton } from "react-bootstrap/AccordionButton";
// import Card from "react-bootstrap/Card";

function UserResult(props) {
  const imageTag = (tag, playerIndex) => {
    if (tag === "tier") {
      if (props.data.user.tier === "") {
        return false;
      } else {
        return `https://opgg-static.akamaized.net/images/medals_new/${props.data.user.tier}.png?image=q_auto,f_webp,w_144&v=1702977255104`;
      }
      // } else if (tag === "spell") {
    } else if (tag === "champion") {
      return `https://opgg-static.akamaized.net/meta/images/lol/champion/${props.data.match[playerIndex].championName}.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160,h_160&v=1700641403304`;
      // } else if (tag === "runeMain") {
      // } else if (tag === "runeAssist") {
      // }
    }
  };
  const itemCheck = (itemNumber) => {
    var elementList = document.getElementsByTagName("img");
    for (var i = 0; i < elementList.length; i++) {
      if (elementList[i].alt === 0) {
        elementList[i].classList.add("noItem");
      } else {
        return `https://opgg-static.akamaized.net/meta/images/lol/14.1.1/item/${itemNumber}.png?image=q_auto,f_webp,w_64,h_64&v=1700641403304`;
      }
    }
  };
  const styles = (status, name) => {
    if (status === true) {
      if (name === props.data.user.name) {
        return "contents minWin";
      } else {
        return "contents win";
      }
    } else {
      if (name === props.data.user.name) {
        return "contents minLose";
      } else {
        return "contents lose";
      }
    }
  };
  if (props.data.user !== "") {
    return (
      <div>
        <div>
          <p>{JSON.stringify(props.data.user)}</p>
          <Container>
            <Col>
              <Row>
                <img
                  src={imageTag("tier")}
                  width="8%"
                  alt={props.data.user.tier}
                ></img>
              </Row>
              <Row style={{ marginLeft: "20px" }}>
                {props.data.user.tier}
                {props.data.user.rank}{" "}
              </Row>
            </Col>
          </Container>
          <p>{JSON.stringify(props.data)}</p>
          <div>
            <h2>전적 들어갈 부분</h2>
            <hr />
            <div>
              {/* Blue Team  == 승리여부 확인과 함께 */}
              <table className="table">
                {/* Blue Team & Red Team */}
                <thead></thead>
                {/* Player */}
                <tbody>
                  {props.data.match.map((player, playerIndex) => {
                    return (
                      <tr
                        key={playerIndex}
                        className={styles(player.win, player.name)}
                      >
                        {/* Champion */}
                        <td className="champion">
                          <div className="">
                            <img
                              className="playerInfo ChampionImage"
                              src={imageTag("champion", playerIndex)}
                              style={{
                                borderRadius: "150 / 2",
                                overflow: "hidden",
                                borderWidth: "3",
                              }}
                              alt={player.championName}
                            ></img>
                          </div>
                        </td>
                        {/* PlayerName */}
                        <td className="Name">
                          {/* PlayerName */}
                          <Col className="center">
                            <Row className="playerName">{player.name}</Row>
                            <Row className="playerTag">#{player.tag}</Row>
                          </Col>
                        </td>
                        <td className="kda">
                          <span className="playerInfo">
                            {player.kills} / {player.deaths} / {player.assists}
                          </span>
                        </td>
                        {/* Item */}
                        <td className="items">
                          <div className="item">
                            <div style={{ position: "relative" }}>
                              <img
                                className="itemImage"
                                src={itemCheck(player.items[0])}
                                alt={player.items[0]}
                              ></img>
                            </div>
                          </div>
                          <div className="item">
                            <div style={{ position: "relative" }}>
                              <img
                                className="itemImage"
                                src={itemCheck(player.items[1])}
                                alt={player.items[1]}
                              ></img>
                            </div>
                          </div>
                          <div className="item">
                            <div style={{ position: "relative" }}>
                              <img
                                className="itemImage"
                                src={itemCheck(player.items[2])}
                                alt={player.items[2]}
                              ></img>
                            </div>
                          </div>
                          <div className="item">
                            <div style={{ position: "relative" }}>
                              <img
                                className="itemImage"
                                src={itemCheck(player.items[3])}
                                alt={player.items[3]}
                              ></img>
                            </div>
                          </div>
                          <div className="item">
                            <div style={{ position: "relative" }}>
                              <img
                                className="itemImage"
                                src={itemCheck(player.items[4])}
                                alt={player.items[4]}
                              ></img>
                            </div>
                          </div>
                          <div className="item">
                            <div style={{ position: "relative" }}>
                              <img
                                className="itemImage"
                                src={itemCheck(player.items[5])}
                                alt={player.items[5]}
                              ></img>
                            </div>
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    return (
      <div>
        <h1>플레이어를 검색해주세요</h1>
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLcN6Og1idKRsHDP7_tDdbDDp2GhGoYyx8Gg&usqp=CAU"
          alt="행복하다"
          className="resetImage"
        ></img>
      </div>
    );
  }
}
export default UserResult;
