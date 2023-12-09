from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import requests
import pandas as pd

app = Flask(__name__)
CORS(app)


API_key = 'RGAPI-625160d1-8730-4bb1-abd1-a8fa38c9dee5';

@app.route('/', methods=['GET', 'POST'])
def main():
    # if request.method == 'POST':
    #     return 'Hello World';
    # if request.method == 'GET':
        # userName = input()
        # userTag = input()
        res = requests.get(f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/jolf/KR1?api_key=RGAPI-625160d1-8730-4bb1-abd1-a8fa38c9dee5")
        print(res)
        return jsonify({'data': res})

if __name__ == '__main__':
    app.run(debug=True)
