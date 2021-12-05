import recommender

import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
  return 'Hello World'

@app.route('/recommendation', methods=['POST'])
def recommend():
  results = recommender.recommend(request.args.get('request'))
  formatted_results = []

  for result in results:
    params = {
      'input': compileAddress(result['address']),
      'key': 'AIzaSyBdrIv-3ggQwhyjuFrLSpjmSR1aj05FeUU',
      'inputtype': 'textquery'
    }
    r = requests.get(url="https://maps.googleapis.com/maps/api/place/findplacefromtext/json", params=params)
    data = r.json()
    
    params2 = {
      'key': 'AIzaSyBdrIv-3ggQwhyjuFrLSpjmSR1aj05FeUU',
      'place_id': data['candidates'][0]['place_id']
    }
    r2 = r = requests.get(url="https://maps.googleapis.com/maps/api/place/details/json", params=params2)
    data2 = r2.json()

    formatted_result = {
      'name': result['name'],
      'formatted_address': data2['result']['formatted_address'],
      'location': {
        'lat': data2['result']['geometry']['location']['lat'],
        'lng': data2['result']['geometry']['location']['lng'],
      },
      'url': data2['result']['url'],
      'icon': data2['result']['icon'],
      'rating': result['rating']
    }

    formatted_results.append(formatted_result)

  return jsonify(formatted_results),200

def compileAddress(addrArr):
  fin = ""
  for sect in addrArr:
    fin += sect
  return fin