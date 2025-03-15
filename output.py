import requests

url = "http://127.0.0.1:5000/predict"

# Make sure to send exactly 30 features (update with real data)
data = {"features": [0] * 30}  # 30 dummy values, replace with actual input

response = requests.post(url, json=data)
print(response.json())  # Should return {"prediction": ...} if it works
