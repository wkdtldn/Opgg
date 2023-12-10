from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import requests
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

Data = list()
API_key = 'RGAPI-d6b46f86-ce5f-498b-a30a-f3660691f317';

## UserInfo에 들어갈 Data
userData = { "level" : "", "name" : "", "tag" : "", "tier" : "" , "rank" : "" }
MatchInfo = list()

class UserInfo:
    def __init__(self, level, name, tag, tier, rank, match):
        self.level = level
        self.name = name
        self.tag = tag
        self.tier = tier
        self.rank = rank
        self.match = match


@app.route('/',methods=['GET', 'POST'])
def main():
    userName = "jolf"
    userTag = "KR1"
    res_puuid = requests.get("https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + userName + "/" + userTag + "?api_key=" + API_key)
    if res_puuid.status_code == 200:
        res_id = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userName + "?api_key=" + API_key)
        user_info_collect(res_puuid)
        user_info_collect(res_id)
        res_tier = requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + Data[1]["id"] + "?api_key=" + API_key)
        res_matchID = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + Data[0]["puuid"] +"/ids?type=normal&count=1&api_key=" + API_key)
        user_info_collect(res_tier)
        user_info_collect(res_matchID)        
        res_matchInfo = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/" + Data[3][0] + "?api_key=" + API_key)
        user_info_collect(res_matchInfo)
        userData["level"] = Data[1]["summonerLevel"]
        userData["name"] = Data[0]["gameName"]
        userData["tag"] = Data[0]["tagLine"]
        userData["tier"] = Data[2][0]["tier"]
        userData["rank"] = Data[2][0]["rank"]
        MatchInfo = Data[4]
        print(MatchInfo)
        return jsonify(userData)
    else:
        return jsonify({'Result' : False})

def user_info_collect(item):
    data = item.text
    data = json.loads(data)
    Data.append(data)
    

@app.route('/index', methods=['GET', 'POST'])
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

