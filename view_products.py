import json

# Load the JSON data from file
with open('json/products_data.json', 'r') as file:
    data = json.load(file)

# Pretty print the JSON data
print(json.dumps(data, indent=4, sort_keys=True))
