from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import requests
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

infoSet = []
API_key = 'RGAPI-625160d1-8730-4bb1-abd1-a8fa38c9dee5';

class UserInfo:
    def __init__(self, id, puuid, summonerid, name, tag):
        self.id = id
        self.puuid = puuid
        self.summonerid = summonerid
        self.name = name
        self.tag = tag

@app.route('/', methods=['GET', 'POST'])
def main():
    return "Hello World"
def setUser():
    userName = input("닉네임: ")
    userTag = input("테그: ")
    res_puuid = requests.get("https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + userName + "/" + userTag + "?api_key=" + API_key)
    res_id = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userName + "?api_key=" + API_key)
    res_summonerid = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userName + "?api_key=" + API_key)
    data = list()
    data.append(res_puuid.text)
    data = json.loads(data)
    if res.status_code == 200:
        infoSet.append({"puuid" : data['puuid']})
        return jsonify({"puuid": data['puuid']})

if __name__ == '__main__':
    app.run(debug=True)

