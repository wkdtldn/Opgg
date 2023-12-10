from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import requests
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

userData = list()
API_key = 'RGAPI-d6b46f86-ce5f-498b-a30a-f3660691f317';

class UserInfo:
    def __init__(self, id, puuid, summonerid, name, tag):
        self.id = id
        self.puuid = puuid
        self.summonerid = summonerid
        self.name = name
        self.tag = tag



@app.route('/',methods=['GET', 'POST'])
def main():
    userName = "jolf"
    userTag = "KR1"
    res_puuid = requests.get("https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + userName + "/" + userTag + "?api_key=" + API_key)
    if res_puuid.status_code == 200:
        res_id = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userName + "?api_key=" + API_key)
        res_summonerid = requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userName + "?api_key=" + API_key)
        collect(res_puuid,"puuid")
        collect(res_id,"id")
        collect(res_summonerid,"summonerid")
        return jsonify(userData)
    else:
        return jsonify({'Result' : False})

def collect(item,name):
    data = item.text
    data = json.loads(data)
    userData.append({ name : data })
    return jsonify({ name : data})

@app.route('/index', methods=['GET', 'POST'])
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

