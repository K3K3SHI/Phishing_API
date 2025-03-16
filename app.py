from flask import Flask, jsonify, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load your ML model
def load_model():
    with open("intrusion_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# Function to preprocess the 30 features (if needed)
def preprocess_features(features):
    # Convert the features to a numpy array and reshape for the model
    features_array = np.array(features).reshape(1, -1)  # Reshape for a single sample
    return features_array

@app.route("/")
def home():
    return jsonify({"message": "Intrusion Detection API is running!"})

@app.route("/check", methods=["POST"])
def check_intrusion():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Invalid request"}), 400

    features = data["features"]
    if len(features) != 30:  # Ensure exactly 30 features are provided
        return jsonify({"error": "Expected 30 features"}), 400

    # Preprocess the features
    processed_features = preprocess_features(features)

    # Use the ML model to predict
    prediction = model.predict(processed_features)[0]  # Replace with your actual prediction logic
    return jsonify({"result": "malicious" if prediction == 1 else "safe"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
