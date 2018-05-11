from flask import Flask, request # , jsonify, request
from flask_restplus import Api, Resource
# from sklearn.externals import joblib


##################################################################
# Function for demo purposes
def do_something_with_json(data):
    value_1 = data.get('value_1')
    value_2 = data.get('value_2')
    sum_ = value_1 + value_2
    return value_1, value_2, sum_

##################################################################

app = Flask(__name__)
api = Api(app, version='0.1', title='...title...',
          description='...description...', contact='...contact...')

# Create new namespace with URL prefix
ns = api.namespace('my_namespace', description='...description...')

##################################################################
# Serializers
from flask_restplus import fields

my_json = api.model('my_json', {
    'value_1': fields.Integer(description='value_1'),
    'value_2': fields.Integer(description='value_2'),
})

my_todo = api.model('my_todo', {
    'the_todo': fields.String(description='the_todo'),
})

##################################################################

@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    @api.expect(my_json)
    def post(self):
        value_1, value_2, sum_ = do_something_with_json(request.json)
        return {'v1': value_1, 'v2': value_2, 'sum': sum_}

@ns.route('/hi')
class HiYou(Resource):
    def get(self):
        return {'hi': 'you'}



todos = {}

@ns.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    @api.expect(my_todo)
    def put(self, todo_id):
        todos[todo_id] = request.json.get('the_todo')
        return {todo_id: todos[todo_id]}


# The following can be called via 127.0.0.1:5000/approute,
# but is not displayed in Swagger 
# @app.route('/approute')
# def approute_test():
#     return 'approute - test'

#@api.route('/predict', methods=['POST'])
#def predict():
#    if request.method == 'POST':
#        try:
#            data = request.get_json()
#            lstat = float(data['LSTAT'])
#
#            lin_reg = joblib.load('linear_regression_model.pkl')
#        except ValueError:
#            return jsonify('Please enter a number.')
#
#        return jsonify(lin_reg.predict(lstat).tolist())

if __name__ == '__main__':
    app.run(debug=True)
