from app import app
from flask import render_template
import json

@app.route('/')
def index():
    # Here, you would typically query a database to get traffic data.
    traffic_data = [
        {"location": "Location 1", "traffic_condition": "Heavy"},
        {"location": "Location 2", "traffic_condition": "Clear"}
    ]
    return render_template('index.html', traffic_data=traffic_data)
