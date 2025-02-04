import requests
import json

# Define the URL and the payload
url = 'http://localhost:1234/v1/chat/completions'
payload = {
    "model": "llama-3.2-1b-instruct",
    "messages": [
        {"role": "system", "content": "Always answer in rhymes. Today is Thursday"},
        {"role": "user", "content": "What day is it today?"},
    ]
}

# Convert the payload to a JSON string
data = json.dumps(payload)

# Make the POST request
response = requests.post(url, data=data, headers={'Content-Type': 'application/json'})

print(response.status_code)
print(response.text)
