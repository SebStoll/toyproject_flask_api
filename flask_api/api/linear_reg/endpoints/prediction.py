from flask_restplus import Resource
from api.restplus import api

ns = api.namespace('prediction', description='Operations related to prediction')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world_prediction'}