import json

# Load the JSON data from file
with open('json/products_data.json', 'r') as file:
    products_data = json.load(file)

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate through each product in the data
for product in products_data:
    # Extract the 'name' and 'recipient_description' fields
    item_name = product.get('name', 'No Name Available')
    item_description = product.get('recipient_description', 'No Description Available')
    
    # Extract the brand name
    brand_name = product.get('brand', {}).get('name', 'No Brand Available')
    
    # Append the extracted information to the list
    extracted_data.append({
        'name': item_name,
        'description': item_description,
        'brand': brand_name
    })

# Write the extracted data to a new JSON file
with open('json/extracted_items.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)

print("Extraction completed. Data written to extracted_items.json")
