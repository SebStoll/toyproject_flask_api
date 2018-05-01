from flask import Flask, jsonify, request
from sklearn.externals import joblib
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            lstat = float(data['LSTAT'])

            lin_reg = joblib.load('linear_regression_model.pkl')
        except ValueError:
            return jsonify('Please enter a number.')

        return jsonify(lin_reg.predict(lstat).tolist())

if __name__ == '__main__':
    app.run(debug=True)
