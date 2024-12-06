import json
import csv

def json_to_csv(json_file, csv_file):
    try:
        # Opens the JSON file and loads the data
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Opens the CSV file for writing
        with open(csv_file, 'w', newline='') as file:
            # Step 3: Create a CSV writer object
            writer = csv.writer(file)
            
            # Writes the header (keys of the JSON objects)
            if data and isinstance(data, list):
                header = data[0].keys()
                writer.writerow(header)
                
                # Writes the rows (values of the JSON objects)
                for row in data:
                    writer.writerow(row.values())
            else:
                print("JSON data is empty or not a list!")
        
        print(f"Successfully converted {json_file} to {csv_file}")
    except Exception as e:
        print(f"Error: {e}")

# File paths
input_json = 'test_data.json'   # Replace with your JSON file path
output_csv = 'output.csv'  # Replace with your desired CSV file path

# Convert JSON to CSV
json_to_csv(input_json, output_csv)
