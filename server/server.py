from flask import Flask, render_template, request, jsonify
import util
import os

app = Flask(__name__, template_folder='client')  # 👈 tell Flask to look for templates in client/

@app.route('/')
def index():
    return render_template('index.html')  # Make sure this matches your file name exactly

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    location = data['location']
    sqft = float(data['total_sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000, debug=True)

