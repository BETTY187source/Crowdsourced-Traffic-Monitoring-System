        
from datetime import datetime

class TrafficData:
    def __init__(self, user_id, location, traffic_condition, timestamp=None):
        self.user_id = user_id
        self.location = location
        self.traffic_condition = traffic_condition
        self.timestamp = timestamp or datetime.utcnow()
