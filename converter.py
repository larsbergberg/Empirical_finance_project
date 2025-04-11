

import os
import pandas as pd

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set input and output folder (same as script directory)
input_folder = script_dir
output_folder = script_dir  # Save CSV files in the same directory

# Loop through all Excel files in the folder
for file in os.listdir(input_folder):
    if file.endswith(".xlsx") and not file.startswith("~$"):  # Ignore temporary Excel files
        file_path = os.path.join(input_folder, file)
        
        # Read Excel file
        df = pd.read_excel(file_path)
        
        # Convert to CSV
        csv_file = os.path.join(output_folder, file.replace(".xlsx", ".csv"))
        df.to_csv(csv_file, index=False)

        print(f"Converted: {file} -> {csv_file}")

print("All Excel files converted to CSV!")
