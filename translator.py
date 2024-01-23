# Import required libraries
import requests , uuid, json

# Add your subscription key and endpoint
subscription_key = "5f99ff41d5df43318e757898083e2b40"
endpoint = "https://api.cognitive.microsofttranslator.com/"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "centralindia"

# Define the API path and construct the complete API URL
path = '/translate'
constructed_url = endpoint + path

# Set translation parameters
params = {
    'api-version': '3.0',
    'from': 'en',   # Source language is English
    'to': ['de', 'ja',]  # Target languages are German and Japanese
}

# Set request headers
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# Specify the text you want to translate in the request body
body = [{
    'text': 'good morning'
}]

# Make API request using POST method
request = requests.post(constructed_url, params=params, headers=headers, json=body)

# Parse the JSON response
response = request.json()

# Print the response in a readable format
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
