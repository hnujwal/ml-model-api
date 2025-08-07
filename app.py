from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
    return "Machine Learning Model API is Running!"
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = model.predict(np.array(data).reshape(1, -1))
    return jsonify({'prediction': prediction.tolist()})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)