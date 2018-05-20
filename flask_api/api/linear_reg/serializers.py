from flask_restplus import fields
from api.restplus import api

prediction_input = api.model('prediction_input', {
    'value_1': fields.Integer(description='value_1'),
    'value_2': fields.Integer(description='value_2'),
})


prediction_output = api.model('prediction_output', {
    'output_1': fields.Float(description='output_1'),
})

