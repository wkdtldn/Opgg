from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
import requests
import pandas as pd
import json

app = Flask(__name__)
CORS(app)


API_key = 'RGAPI-625160d1-8730-4bb1-abd1-a8fa38c9dee5';

@app.route('/', methods=['GET', 'POST'])
def main():
    # if request.method == 'POST':
    #     return 'Hello World';
    # if request.method == 'GET':
        # userName = "jolf"
        # userTag = "KR1"
        url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/jolf/KR1?api_key=RGAPI-625160d1-8730-4bb1-abd1-a8fa38c9dee5"
        res = requests.get(url, headers={"X-Riot-Token": API_key })
        if res.status_code == 200:
            return jsonify({'data': res.text})
        

if __name__ == '__main__':
    app.run(debug=True)

