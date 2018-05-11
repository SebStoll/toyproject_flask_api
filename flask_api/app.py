from flask import Flask, Blueprint
import settings
from api.restplus import api
from api.linear_reg.endpoints.training import ns as linear_reg_training_namespace
from api.linear_reg.endpoints.prediction import ns as linear_reg_prediction_namespace

app = Flask(__name__)



def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    #flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    #flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    #flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    #flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    #flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    #flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    configure_app(flask_app)
    
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(linear_reg_training_namespace)
    api.add_namespace(linear_reg_prediction_namespace)
    flask_app.register_blueprint(blueprint)
    
    #api.init_app(flask_app)
    
def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG)
    
if __name__=='__main__':
    main()






###################################################################
###################################################################
###################################################################
#api = Api(app, version='0.1', title='...title...',
#          description='...description...', contact='...contact...')
#
## Create new namespace with URL prefix
#ns = api.namespace('my_namespace', description='...description...')
#
###################################################################
## Serializers
#from flask_restplus import fields
#
#my_json = api.model('my_json', {
#    'value_1': fields.Integer(description='value_1'),
#    'value_2': fields.Integer(description='value_2'),
#})
#
#my_todo = api.model('my_todo', {
#    'the_todo': fields.String(description='the_todo'),
#})
#
###################################################################
#
#@ns.route('/hello')
#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}
#    @api.expect(my_json)
#    def post(self):
#        value_1, value_2, sum_ = do_something_with_json(request.json)
#        return {'v1': value_1, 'v2': value_2, 'sum': sum_}
#
#@ns.route('/hi')
#class HiYou(Resource):
#    def get(self):
#        return {'hi': 'you'}
#
#
#
#todos = {}
#
#@ns.route('/<string:todo_id>')
#class TodoSimple(Resource):
#    def get(self, todo_id):
#        return {todo_id: todos[todo_id]}
#
#    @api.expect(my_todo)
#    def put(self, todo_id):
#        todos[todo_id] = request.json.get('the_todo')
#        return {todo_id: todos[todo_id]}
#
#
## The following can be called via 127.0.0.1:5000/approute,
## but is not displayed in Swagger 
## @app.route('/approute')
## def approute_test():
##     return 'approute - test'
#
##@api.route('/predict', methods=['POST'])
##def predict():
##    if request.method == 'POST':
##        try:
##            data = request.get_json()
##            lstat = float(data['LSTAT'])
##
##            lin_reg = joblib.load('linear_regression_model.pkl')
##        except ValueError:
##            return jsonify('Please enter a number.')
##
##        return jsonify(lin_reg.predict(lstat).tolist())
#
#if __name__ == '__main__':
#    app.run(debug=True)
