from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import requests
import pandas as pd
import json
import UserData;

app = Flask(__name__)
CORS(app)

API_key = 'RGAPI-086af0b8-7e66-48bd-badb-9b06335a69b0';

Data = {"puuid" : "", "gameName" : "" , "tagLine" : "", "id" : "", "summonerLevel" : "", "accountId" : "", "tier" : "", "rank" : "", "matchID" : ""}

matchData = list()

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
    res = requests.get("https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + userName + "/" + userTag + "?api_key=" + API_key)
    if res.status_code == 200:
        user_info_collect(res,"puuid")
        user_info_collect(res,"gameName")
        user_info_collect(res,"tagLine")
        res = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userName + "?api_key=" + API_key)
        user_info_collect(res,"id")
        user_info_collect(res,"accountId")
        user_info_collect(res,"summonerLevel")
        res = requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + Data["id"] + "?api_key=" + API_key)
        user_info_collect(res[0], "tier")
        user_info_collect(res[0], "rank")
        res = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + Data["puuid"] +"/ids?type=normal&count=1&api_key=" + API_key)
        user_info_collect(res,"matchID")        
        res_match = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/" + Data["matchID"] + "?api_key=" + API_key)
        match_info_collect(res_match)
        return jsonify(UserData.user_data_set(Data))
    else:
        return jsonify({'Result' : False})

def user_info_collect(item, name):
    data = item.text
    data = json.loads(data)
    Data[name] = data[name]
    print(Data)

def match_info_collect(item):
    data = item.text
    data = json.loads(data)
    matchData.append(data)


if __name__ == '__main__':
    app.run(debug=True)
