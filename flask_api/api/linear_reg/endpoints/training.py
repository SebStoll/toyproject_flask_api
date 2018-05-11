from flask_restplus import Resource
from api.restplus import api

ns = api.namespace('linear_reg/training', description='Operations related to trainig')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world_training'}