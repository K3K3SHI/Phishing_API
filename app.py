import joblib
import numpy as np
from flask import Flask, request, jsonify

# Load the trained ML model
model = joblib.load("random_forest_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Get input JSON data
        features = np.array(data["features"]).reshape(1, -1)  # Convert to array
        prediction = model.predict(features)[0]  # Predict malicious (-1) or safe (1)

        return jsonify({"prediction": int(prediction)})  # Return JSON response
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the API locally for testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
