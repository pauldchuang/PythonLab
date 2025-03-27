import requests
import logging
import http.client

# Enable HTTP connection debugging
http.client.HTTPConnection.debuglevel = 1
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Create a session
session = requests.Session()

# URL of the local API server
base_url = "http://127.0.0.1:8000"

# Make multiple requests
print("Making multiple requests to the same server with requests.Session:\n")
for i in range(5):
    response = session.get(f"{base_url}/")
    print(f"Request {i + 1}: {response.json()}")
