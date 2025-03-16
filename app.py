from flask import Flask, jsonify, request
import pickle
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the ML model
def load_model():
    try:
        with open("random_forest_model.pkl", "rb") as f:
            model = pickle.load(f)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_model()

# Preprocess the input features (if needed)
def preprocess_features(features):
    try:
        # Convert the features to a numpy array and reshape for the model
        features_array = np.array(features).reshape(1, -1)  # Reshape for a single sample
        return features_array
    except Exception as e:
        print(f"Error preprocessing features: {e}")
        return None

# Home route
@app.route("/")
def home():
    return jsonify({"message": "Intrusion Detection API is running!"})

# Check route for predictions
@app.route("/check", methods=["POST"])
def check_intrusion():
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data or "features" not in data:
            return jsonify({"error": "Invalid request: 'features' key is missing"}), 400

        # Extract features
        features = data["features"]
        if len(features) != 30:  # Ensure exactly 30 features are provided
            return jsonify({"error": "Expected 30 features"}), 400

        # Preprocess features
        processed_features = preprocess_features(features)
        if processed_features is None:
            return jsonify({"error": "Feature preprocessing failed"}), 500

        # Make prediction
        prediction = model.predict(processed_features)[0]  # Predict and get the first result
        result = "malicious" if prediction == 1 else "safe"
        return jsonify({"result": result})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT if provided, otherwise default to 5000
    app.run(host="0.0.0.0", port=port)
