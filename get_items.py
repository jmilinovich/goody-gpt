import requests
import json
import os
from dotenv import load_dotenv

# Load API Key from environment variable
load_dotenv('env.local')
API_KEY = os.environ.get('GOODY_API_KEY')
if not API_KEY:
    raise ValueError("GOODY_API_KEY environment variable is not set.")

BASE_URL = 'https://api.ongoody.com/v1/products'
HEADERS = {'Authorization': f'Bearer {API_KEY}'}
PARAMS = {'page': 1, 'per_page': 100}  # Start with the first page and max items per page
all_products = []

while True:
    response = requests.get(BASE_URL, headers=HEADERS, params=PARAMS)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data: HTTP {response.status_code}")
        break

    data = response.json()
    
    # Check if 'data' key exists in the response
    if 'data' not in data or not data['data']:
        print("No more data to fetch or 'data' key is missing in the response.")
        break

    all_products.extend(data['data'])

    # Increment the page number for the next iteration
    PARAMS['page'] += 1

# Exporting to a JSON file
output_directory = 'json'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open('json/products_data.json', 'w') as file:
    json.dump(all_products, file, indent=4)

print(f'Total products fetched: {len(all_products)}')