"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
import flask as fl
from BlueTeamParty import app, darksky, model

import json

dataModel = model.Model()

@app.route('/')
@app.route('/home')
def home():
    return fl.render_template('index.html', title="Test Title")

@app.route("/api/portfolio-points", methods=['GET'])
def portfolio_points():
    ret = dataModel.ids_as_json()
    return fl.jsonify(ret)

@app.route("/weather", methods=['POST'])
def get_weather():
    req_dict = fl.request.form
<<<<<<< HEAD
=======
    force=True
>>>>>>> 5cfcc72ef10279fe6b9247bd6044ba17980194b6
    print(req_dict)
    ret = darksky.Darksky.forecast(float(req_dict['lat']), float(req_dict['lon']))
    print(ret)
    return fl.jsonify(ret)


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
    curr_state = int(req_dict['current_state'])

    ret = dataModel.power_prediction_model(id, curr_state)
    return fl.jsonify(ret)
