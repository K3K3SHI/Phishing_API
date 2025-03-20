import requests

# Define the API URL
API_URL = "http://localhost:5000/check"  # Replace with your actual URL if different

# Sample data with 30 features
sample_data = {
    "features": [
        0.6, 0.4, 0.1, 1.2, 1.7, 1.9, 0.7, 1.3, 0.8, 0.3,
        0.6, 0.9, 0.4, 0.6, 1.3, 0.6, 1.9, 1.0, 1.1, 1.2,
        0.8, 0.9, 0.4, 0.6, 1.0, 0.9, 0.0, 1.7, 1.0, 1.9
    ]
}

# Send a POST request to the API
try:
    response = requests.post(API_URL, json=sample_data)
    response.raise_for_status()  # Raise an error for bad status codes
    result = response.json()
    print("API Response:", result)
except requests.exceptions.RequestException as e:
    print(f"Error calling API: {e}")
