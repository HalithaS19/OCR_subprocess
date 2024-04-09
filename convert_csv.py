import json
import pandas as pd
import os

# Path to the JSON file
json_file = r'C:\Users\103378\Downloads\test\canal.result.json'
rows = []

with open(json_file, 'r') as file:
   
    current_name = None
    current_data = ''
 
    for line in file:
        line = line.strip() 
        if not line or line.startswith("Error decoding JSON:"):
            continue  
        
        if line.endswith('.txt'):
            
            if current_name and current_data:
                try:
                    data = json.loads(current_data)
                    # Extract fields from the JSON object
                    row = {'Name': os.path.basename(current_name)}
                    if data:  # Check if JSON object is not empty
                        for key, value in data.items():
                            row[key] = value
                    rows.append(row)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
           
            current_name = line
            current_data = ''
        else:
            current_data += line

df = pd.DataFrame(rows)

# Save the DataFrame to a CSV file
csv_file = r'C:/Users/103378/Downloads/test/canal_result.csv'
df.to_csv(csv_file, index=False)

print("CSV file created successfully.")




