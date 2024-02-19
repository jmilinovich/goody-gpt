import pandas as pd

# Load the JSON data into a pandas DataFrame
json_file_path = 'json/vantage.json'
df = pd.read_json(json_file_path)

# Transform DataFrame to match the desired structure
df['id'] = df['id']
df['text'] = df['text']
df['meta_price'] = df['meta_price']
df['meta_image_url'] = df['meta_image_url']
df['meta_brand'] = df['meta_brand']

# Define the output Parquet file path
parquet_file_path = 'json/vantage.parquet'

# Write the DataFrame to a Parquet file
df.to_parquet(parquet_file_path, index=False)

print(f"Data written to {parquet_file_path}")
