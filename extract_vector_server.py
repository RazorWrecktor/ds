import csv
import re
from collections import defaultdict
import time

def process_large_rtt_file(input_file, output_csv, vectors_to_extract):
    # Compile regex patterns once
    vector_pattern = re.compile(r'^vector\s+(\d+)\s+.*?conn-(\d+).*?(\w+):vector')
    data_pattern = re.compile(r'^(\d+)\s+\d+\s+([\d.]+)\s+([\d.]+)')
    
    # Dictionary to store connection_id for each vector_id
    vector_info = {}
    
    # Dictionary to store data (connection_id -> list of (time, value))
    data_store = defaultdict(list)
    
    print("Starting processing...")
    start_time = time.time()
    
    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            # Progress reporting
            if line_num % 10_000_000 == 0:
                elapsed = time.time() - start_time
                print(f"Processed {line_num:,} lines in {elapsed:.2f} seconds")
            
            # Process vector definition lines
            if line.startswith('vector'):
                match = vector_pattern.match(line)
                if match:
                    vector_id, conn_id, vector_name = match.groups()
                    if vector_name in vectors_to_extract:
                        vector_info[vector_id] = conn_id
            
            # Process data lines
            elif line[0].isdigit():
                match = data_pattern.match(line)
                if match:
                    vector_id, time_val, value = match.groups()
                    if vector_id in vector_info:
                        conn_id = vector_info[vector_id]
                        data_store[conn_id].append((float(time_val), float(value)))
    
    print(f"Finished reading file. Sorting data...")
    
    # Sort each connection's data by time and write to CSV incrementally
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['connection_id', 'time', 'value'])
        
        # Process connections in sorted order
        for conn_id in sorted(data_store.keys(), key=int):
            # Sort this connection's data by time
            sorted_data = sorted(data_store[conn_id], key=lambda x: x[0])
            
            # Write sorted data to CSV
            for time_val, value in sorted_data:
                writer.writerow([conn_id, time_val, value])
    
    total_time = time.time() - start_time
    print(f"Processing completed in {total_time:.2f} seconds")
    print(f"Data saved to {output_csv}")

if __name__ == "__main__":
    input_file = 'ssthresh.vec'
    output_csv = 'ssthresh.csv'
    vectors_to_extract = ['ssthresh']
    
    process_large_rtt_file(input_file, output_csv, vectors_to_extract)
