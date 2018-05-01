from flask import Flask # , jsonify, request
from flask_restplus import Api, Resource
# from sklearn.externals import joblib
app = Flask(__name__)
api = Api(app, version='0.1', title='...title...',
          description='...description...', contact='...contact...')

ns = api.namespace('namespace', description='...description...')

@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@ns.route('/hi')
class HiYou(Resource):
    def get(self):
        return {'hi': 'you'}


# The following can be called via 127.0.0.1:5000/approute,
# but is not displayed in Swagger 
@app.route('/approute')
def approute_test():
    return 'approute - test'

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
