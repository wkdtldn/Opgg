import React from "react";
import { Container, Col } from "react-bootstrap";

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
  if (props.data.user !== "") {
    return (
      <div>
        <div>
          <p>{JSON.stringify(props.data.user)}</p>
          <div></div>
          <div>
            <img
              // src={`https://opgg-static.akamaized.net/images/medals_new/${props.data.user.tier}.png?image=q_auto,f_webp,w_144&v=1702977255104`}
              src={imageTag("tier")}
              width="8%"
              alt="TIER"
            ></img>
          </div>
          <p>{JSON.stringify(props.data.match)}</p>
          <div>
            <h2>전적 들어갈 부분</h2>
            <hr />
            <div className="border">
              {/* Blue Team  == 승리여부 확인과 함께 */}
              <div>
                {/* Player */}
                {props.data.match.map((player, index) => (
                  <Container fluid key={index}>
                    {/* Champion */}
                    <Col className="item">
                      <div>
                        <img
                          src={imageTag("champion", index)}
                          width="3%"
                          alt="champion"
                        ></img>
                      </div>
                    </Col>
                    {/* PlayerName */}
                    <Col className="item">
                      <p>{player.name}</p>
                    </Col>
                    {/* KDA */}
                    <Col className="item">
                      <p>
                        {player.kills} / {player.deaths} / {player.assists}
                      </p>
                    </Col>
                    {/* Item */}
                    <div></div>
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
