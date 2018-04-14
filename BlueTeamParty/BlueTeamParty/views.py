"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from BlueTeamParty import app, darksky

import json

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title="Test Title")

def api_model_house():
    pass

