import json
import pandas as pd
import os
from pathlib import Path
import glob

def combine_json_files():
    # Find all JSON files in the output directory
    json_files = sorted(glob.glob('output/*.json'))
    
    if not json_files:
        print("No JSON files found in output directory")
        return
    
    print(f"Found {len(json_files)} JSON files to process")
    print()
    
    # Initialize an empty list to store DataFrames
    dfs = []
    
    # Process each JSON file
    for file_path in json_files:
        try:
            print(f"Processing {os.path.basename(file_path)}...")
            print()
            
            # Read the JSON file
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Print a sample of the data structure
            print("Sample of data structure:")
            print(json.dumps(data, indent=2)[:500] + "...")
            print()
            
            # Extract the year from the filename
            year = int(os.path.basename(file_path).split('_')[1].split('.')[0])
            
            # Convert the points data to a DataFrame
            points_df = pd.DataFrame(data['points'])
            
            # Add the year column
            points_df['year'] = year
            
            # Append to the list of DataFrames
            dfs.append(points_df)
            
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            continue
    
    if not dfs:
        print("No data was successfully processed")
        return
    
    # Combine all DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Print basic statistics about the dataset
    print("\nDataset Statistics:")
    print(f"Total rows: {len(combined_df)}")
    print(f"Columns: {', '.join(combined_df.columns)}")
    print(f"Years covered: {combined_df['year'].min()} to {combined_df['year'].max()}")
    print()
    
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Save the combined DataFrame to a CSV file
    combined_df.to_csv('output/combined_wind_data.csv', index=False)
    print("Combined data saved to output/combined_wind_data.csv")
    
    # Create directory for detailed location files
    os.makedirs('output/detailed_locations', exist_ok=True)

    print("Starting to save detailed location files...")
    
    # Group by latitude and longitude and save each group as a JSON file
    for (lat, lon), group in combined_df.groupby(['lat', 'lon']):
        # Create a filename based on the coordinates
        filename = f"output/detailed_locations/location_{lat:.6f}_{lon:.6f}.json"
        
        # Convert the group to a dictionary with year as key and value as value
        location_data = {
            'lat': lat,
            'lon': lon,
            'data': dict(zip(group['year'], group['value']))
        }
        
        # Save to a JSON file
        with open(filename, 'w') as f:
            json.dump(location_data, f, indent=2)
    
    print("Detailed location files saved to output/detailed_locations")

if __name__ == "__main__":
    combine_json_files() 