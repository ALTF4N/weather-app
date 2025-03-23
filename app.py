import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("f6f164cf74451f7482109df029db0d8c")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?id=524901&appid=f6f164cf74451f7482109df029db0d8c"

@app.route('/')
def home():
    # Default weather untuk Jakarta
    params = {
        'q': 'Jakarta',
        'appid': 'f6f164cf74451f7482109df029db0d8c',
        'units': 'metric',
        'lang': 'id'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return render_template('index.html', data=data)

@app.route('/search', methods=['POST'])
def search():
    city = request.form['city']
    params = {
        'q': city,
        'appid': 'f6f164cf74451f7482109df029db0d8c',
        'units': 'metric',
        'lang': 'id'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)