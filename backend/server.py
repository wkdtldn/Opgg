from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import requests
import pandas as pd
import json
import UserData;

app = Flask(__name__)

CORS(app)

API_key = 'RGAPI-9232c512-649d-436e-a4dd-09d645e7572b';

Data = {"puuid" : "", "gameName" : "" , "tagLine" : "", "id" : "", "summonerLevel" : "", "accountId" : "", "tier" : "", "rank" : "", "matchID" : ""}

match = { "matchID" : "", "matchInfo" : ""}

class UserInfo:
    def __init__(self, level, name, tag, tier, rank, match):
        self.level = level
        self.name = name
        self.tag = tag
        self.tier = tier
        self.rank = rank
        self.match = match


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print("POST")
        data = request.get_json()
        print(data)
        userName = data["Name"]
        userTag = data["Tag"]
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
            user_info_collect(res, "tier")
            user_info_collect(res, "rank")
            res = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + Data["puuid"] +"/ids?type=normal&count=1&api_key=" + API_key)
            match_info_collect(res, "matchID")        
            res_match = requests.get("https://asia.api.riotgames.com/lol/match/v5/matches/" + match["matchID"] + "?api_key=" + API_key)
            match_info_collect(res_match, "matchInfo")
            UserData.user_data_set(Data)
            return json.dumps({"match" : UserData.match_data_set(match), "user" : UserData.userInfo, 'Result' : True})
        else:
            return jsonify({'Result' : False})

def user_info_collect(item, name):
    data = item.text
    data = json.loads(data)
    if str(type(data)) == "<class 'dict'>":
        Data[name] = data[name]
    else:
        Data[name] = data[0][name]

def match_info_collect(item,name):
    data = item.text
    data = json.loads(data)
    if str(type(data)) == "<class 'dict'>":
        match[name] = data
    else:
        match[name] = data[0]


if __name__ == "__main__":
    app.run(debug=True)
