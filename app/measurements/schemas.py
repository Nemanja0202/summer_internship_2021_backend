from marshmallow import Schema, fields


class MeasureentRequestSchema(Schema):
    air_quality = fields.Float(required=True)
    temperature = fields.Float(required=True)
    humidity = fields.Float(required=True)


class MeasurementResponseSchema(Schema):
    id = fields.Integer()
    air_quality = fields.Float()
    temperature = fields.Float()
    humidity = fields.Float()
    time_stamp = fields.DateTime()
