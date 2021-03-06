from flask import request
from flask_restplus import Resource
from api.restplus import api
from api.linear_reg.serializers import prediction_input, prediction_output
from api.linear_reg.business import do_prediction

ns = api.namespace('prediction', description='Operations related to prediction')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world_prediction'}
    
    @api.expect(prediction_input)
    @api.marshal_with(prediction_output)
    def post(self):
        value_1, value_2, prediction = do_prediction(request.json)
        return {'v1': value_1, 'v2': value_2, 'output_1': prediction}