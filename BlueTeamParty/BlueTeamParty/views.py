"""
Routes and views for the flask application.
"""

from datetime import datetime
import flask as fl
from BlueTeamParty import app, darksky

import json

@app.route('/')
@app.route('/home')
def home():
    return fl.render_template('index.html', title="Test Title")

def api_model_house():
    pass

@app.route("/demo/portfolio-points")
def demo_portfolio_points():
    pass

@app.route("/weather", methods=['POST'])
def get_weather():
    req_dict = fl.request.form
    print(req_dict)
    ret = darksky.Darksky.forecast(float(req_dict['lat']), float(req_dict['lon']))
    print(ret)
    return fl.jsonify(ret)

@app.route("/weather/current", methods=['POST'])
def get_current_weather():
    pass

@app.route("/weather/historical", methods=['POST'])
def get_weather_historical():
    req_dict = fl.request.form
    print(req_dict)
    ret = darksky.Darksky.time_machine(float(req_dict['lat']), float(req_dict['lon']), req_dict['time'])
    print(ret)
    return fl.jsonify(ret)

@app.route("/api/power_prediction", methods=['POST'])
def power_prediction():
    req_dict = fl.request.form
    id = req_dict['id']
    curr_state = req_dict['current_state']
    # get lat/lon

    # call darksky
    # prep darksky
    # do model

    ret = {}
    return fl.jsonify(ret)
