from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Dummy price prediction function
def predict_price(size, bedrooms, bathrooms):
    return round((size * 3000) + (bedrooms * 50000) + (bathrooms * 30000), 2)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        size = float(data['size'])
        bedrooms = int(data['bedrooms'])
        bathrooms = int(data['bathrooms'])
        
        predicted_price = predict_price(size, bedrooms, bathrooms)

        return jsonify({'price': predicted_price})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
