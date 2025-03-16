from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API is running!"})

@app.route("/check", methods=["POST"])
def check_phishing():
    data = request.get_json()
    if not data or "website" not in data:
        return jsonify({"error": "Invalid request"}), 400
    return jsonify({"result": "safe"})  # Dummy response for now

if __name__ == "__main__":
    app.run(debug=True)
