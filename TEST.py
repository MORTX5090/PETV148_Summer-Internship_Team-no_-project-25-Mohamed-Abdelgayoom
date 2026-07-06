import requests

# 1. The scan route URL on your local Flask server
url = "http://127.0.0.1:5000/scan"

# 2. Prepare the URL we want to scan (as if the user typed it into the input box)
data_to_send = {"url": "https://google.com"}

print("Sending the URL to the server... Please wait")

# 3. Send a POST request exactly as required in the app.py file
response = requests.post(url, data=data_to_send)

# 4. Print the result returned by the server
print("\n=== Scan Result from the Server ===")
print(response.json())