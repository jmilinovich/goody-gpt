import json

# Step 1: Read the JSON content
input_file_path = 'json/flatfile.json'
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Step 2: Transform each item
transformed_data = []
for item in data:
    transformed_item = {
        "id": item["id"],
        "text": f"The product {item['name']} by {item['brand']} is {item['subtitle']}",
        "meta_price": item["price"],
        "meta_image_url": item.get("image_url", ""),  # Using .get() for safety in case some items might lack "image_url"
        "meta_brand": item["brand"]
    }
    transformed_data.append(transformed_item)

# Step 3: Write the transformed data to vantage.json
output_file_path = 'json/vantage.json'
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(transformed_data, file, indent=4, ensure_ascii=False)

print("Transformation completed. Data written to vantage.json")
