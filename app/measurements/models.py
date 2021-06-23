from app import db
from datetime import datetime


class Measurement(db.Model):
    __tablename__ = 'measurements'

    id = db.Column(db.Integer, primary_key=True)
    pollution = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    time_stamp = db.Column(db.DateTime(timezone=True), nullable=False,
                           default=datetime.utcnow)

    def __init__(self, pollution, humidity, temperature):
        self.pollution = pollution
        self.humidity = humidity
        self.temperature = temperature
