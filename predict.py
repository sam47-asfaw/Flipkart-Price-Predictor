from flask import Flask, jsonify, request
from waitress import serve

import xgboost as xgb
import numpy as np

import pickle

with open('./model_reg=1.0.bin', 'rb') as f_in:
    (dv,xgbst)= pickle.load(f_in)

app = Flask('Flipkart')


@app.route('/predict', methods= ['POST'])
def predict():

    product = request.get_json()

    X = dv.transform([product])

    dx = xgb.DMatrix(X, feature_names=dv.get_feature_names_out().tolist())
    pred = xgbst.predict(dx)
    pred = np.expm1(pred)[0]
    price = pred.round(2)
    
    result = {
        'Product Price': float(price)
    }
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)