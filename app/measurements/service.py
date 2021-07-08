from app import db
from app.measurements.models import Measurement


class MeasurementService:
    @staticmethod
    def get_by_id(id):
        return db.session.query(Measurement).\
            filter(Measurement.id == id).\
            one_or_none()

    @staticmethod
    def get_all():
        measurements = db.session.query(Measurement)

        return measurements.all()

    @staticmethod
    def get_latest():
        return db.session.query(Measurement).\
            order_by(Measurement.id.desc()).\
            first()

    @staticmethod
    def create(post_data):
        measurement = Measurement(air_quality=post_data['air_quality'],
                                  temperature=post_data['temperature'],
                                  humidity=post_data['humidity'])
        db.session.add(measurement)
        db.session.commit()

        return measurement
