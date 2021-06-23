from flask_restx import Resource
from app.measurements import measurement_api


@measurement_api.route('')
class Measurements(Resource):
    def get(self):
        return {'key': 'value'}
