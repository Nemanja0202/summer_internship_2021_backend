from flask import request

from flask_restx import Resource
from app.measurements import measurement_api
from app.measurements.schemas import MeasurementResponseSchema, \
    MeasureentRequestSchema
from app.measurements.service import MeasurementService


@measurement_api.route('')
class MeasurementsApi(Resource):
    def get(self):
        all_measurements = MeasurementService().get_all()

        return MeasurementResponseSchema(many=True).dump(all_measurements)

    def post(self):
        post_data = MeasureentRequestSchema().load(request.json)
        measurement = MeasurementService().create(post_data=post_data)

        return MeasurementResponseSchema().dump(measurement)


@measurement_api.route('/latest')
class MeasurementApi(Resource):
    def get(self):
        measurement = MeasurementService().get_latest()

        return MeasurementResponseSchema().dump(measurement)


@measurement_api.route('/<int:id>')
class MeasurementApi(Resource):
    def get(self, id):
        measurement = MeasurementService().get_by_id(id=id)

        return MeasurementResponseSchema().dump(measurement)
