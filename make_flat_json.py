import json
import os

# Define the output directory
output_directory = 'json'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Load the JSON data from file
with open('json/products_data.json', 'r') as file:
    products_data = json.load(file)

# Initialize an empty list to store the extracted data
extracted_data = []

# Iterate through each product in the data
for product in products_data:
    # Copy the product dictionary while excluding specific fields
    excluded_fields = ['variants', 'variants_label', 'variants_num_selectable', 'restricted_states', 'price_is_variable', 'images', 'subtitle_short', 'recipient_description']
    item_copy = {key: value for key, value in product.items() if key not in excluded_fields}

    # Extract only the brand name
    item_copy['brand'] = product.get('brand', {}).get('name', 'No Brand Available')
    
    # Extract the URL of the first image, if available
    image_url = product['images'][0].get('image_large', {}).get('url', '') if product.get('images') else ''
    item_copy['image_url'] = image_url

    # Append the modified item dictionary to the list
    extracted_data.append(item_copy)

# Define the output file path within the output directory
output_file_path = os.path.join(output_directory, 'flatfile.json')

# Write the extracted data to a new JSON file in the specified directory
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(extracted_data, file, indent=4, ensure_ascii=False)

print(f"Extraction completed. Data written to {output_file_path}")
