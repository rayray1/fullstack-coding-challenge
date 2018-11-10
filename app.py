from flask import Flask, render_template, jsonify, request
import requests
import json
from flask_sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)


# Translator class
class Translator:
    def __init__(self):
        self.url = 'https://sandbox.unbabel.com/tapi/v2/translation/'
        self.header = {'Authorization': 'ApiKey fullstack-challenge:9db71b322d43a6ac0f681784ebdcc6409bb83359'}

    # Translate english phrase
    def translate_eng(self, data):
        payload = {"text": data, "source_language": "en", "target_language": "es", "text_format": "text"}
        payload = json.dumps(payload)
        response = requests.post(url=self.url, headers=self.header, data=payload)
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            return response.json

    # Translated phrase
    @staticmethod
    def get_translation(uid):
        url = 'https://sandbox.unbabel.com/tapi/v2/translation/' + uid
        header = {'Authorization': 'ApiKey fullstack-challenge:9db71b322d43a6ac0f681784ebdcc6409bb83359'}
        translated = requests.get(url=url, headers=header)
        if translated.status_code == 200:
            return translated.json()


# Homepage
@app.route('/')
def index():
    return render_template("index.html")


# Send initial translation request
@app.route("/feed", methods=['POST'])
def feed():
    phrase = request.get_json()
    response = Translator().translate_eng(data=phrase['load'])
    translated_code = Translator().get_translation(uid=response['uid'])
    return jsonify(translated_code)


# Check if translation is complete
@app.route("/get-update", methods=['GET', 'POST'])
def get_update():
    uid = request.get_json()
    print(uid)
    translated_code = Translator().get_translation(uid=uid['uuid'])
    return jsonify(translated_code)


if __name__ == '__main__':
    app.run(debug=True)
