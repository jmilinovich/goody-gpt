import json
import csv

# Define the file paths
input_file_path = 'json/flatfile.json'
output_file_path = 'json/flatfile.csv'

# Open the JSON file and load the data
with open(input_file_path, 'r') as json_file:
    data = json.load(json_file)

# Open the CSV file in write mode
with open(output_file_path, 'w', newline='') as csv_file:
    # If the JSON data is a list of dictionaries, we can automatically detect the headers
    if data and isinstance(data, list):
        headers = data[0].keys()
    else:
        # Alternatively, define headers manually if the structure is different
        headers = ['your', 'header', 'names']
    
    # Create a csv writer object and write the header
    csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
    csv_writer.writeheader()
    
    # Write the JSON data to the CSV file
    if isinstance(data, list):
        for row in data:
            csv_writer.writerow(row)
    else:
        # Handle different JSON structures here
        pass

print('JSON to CSV conversion completed.')
