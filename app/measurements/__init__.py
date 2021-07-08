from flask import Blueprint
from flask_restx import Api

measurement = Blueprint('measurement', __name__,
                        url_prefix='/api/measurements')

measurement_api = Api(measurement)

import app.measurements.apis
