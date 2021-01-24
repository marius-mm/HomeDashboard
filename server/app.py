from flask import Flask, jsonify
from flask_cors import CORS
import requests
#ToDo
#you should only allow cross-origin requests from the domain where the front-end application is hosted. Refer to the Flask-CORS documentation for more info on this.

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/corona/Erlangen')
def coronaData():
    y = requests.get('https://api.corona-zahlen.org/districts/' + '09562')
    y = y.json()['data']['09562']
    return y

@app.route('/corona/germany')
def coronaGermany():
    return requests.get('https://api.corona-zahlen.org/germany').json()

@app.route('/corona/map/districts')
def coronaMapDistricts():
    return requests.get('https://api.corona-zahlen.org/germany')

     



# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()