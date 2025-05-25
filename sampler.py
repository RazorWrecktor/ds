import pandas as pd
import os

def filter_large_csv(input_folder, output_folder, time_column='time', threshold=60):
    """
    Process large CSV files in a folder, filtering rows where time <= threshold.
    Creates new files with filtered data in the output folder.
    
    Args:
        input_folder: Path to folder containing input CSV files
        output_folder: Path to folder where filtered files will be saved
        time_column: Name of the time column to filter on
        threshold: Maximum time value to include (in seconds)
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"60s_{filename}")
            
            print(f"Processing {filename}...")
            
            # Use chunking to process the large file in parts
            chunk_size = 10000000  # Adjust based on your system memory
            first_chunk = True
            
            for chunk in pd.read_csv(input_path, chunksize=chunk_size):
                # Filter rows where time <= threshold
                filtered = chunk[chunk[time_column] <= threshold]
                
                # Write to output file
                if first_chunk:
                    # Write header for the first chunk
                    filtered.to_csv(output_path, mode='w', index=False)
                    first_chunk = False
                else:
                    # Append without header for subsequent chunks
                    filtered.to_csv(output_path, mode='a', index=False, header=False)
            
            print(f"Finished processing {filename}. Results saved to {output_path}")

if __name__ == "__main__":
    # Configure these paths
    input_folder = os.getcwd()
    output_folder = "sample"
    
    filter_large_csv(input_folder, output_folder)