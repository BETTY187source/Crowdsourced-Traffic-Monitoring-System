from app import app
from flask import request, jsonify
from app.models import TrafficData

@app.route('/submit_data', methods=['POST'])
def submit_data():
    data = request.get_json()
    user_id = data['user_id']
    location = data['location']
    traffic_condition = data['traffic_condition']
    
    # Save data to database (skipped for simplicity)
    traffic_data = TrafficData(user_id, location, traffic_condition)
    
    # Here you would save traffic_data to a database (e.g., MongoDB)
    
    return jsonify({"status": "success", "message": "Traffic data submitted successfully"})
