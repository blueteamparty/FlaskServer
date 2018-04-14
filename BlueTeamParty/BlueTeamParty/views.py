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
