import os
import csv

def count_rows_in_csv_files():
    # Get all CSV files in the current directory
    csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return
    
    # Output CSV filename
    output_filename = "csv_row_counts.csv"
    
    # Process each CSV file and write results to output CSV
    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        # Write headers
        writer.writerow(["CSV File", "Number of Rows (excluding header)"])
        
        for csv_file in csv_files:
            try:
                with open(csv_file, 'r', newline='', encoding='utf-8') as infile:
                    reader = csv.reader(infile)
                    # Count rows excluding header
                    row_count = sum(1 for row in reader) - 1
                    writer.writerow([csv_file, row_count])
                    print(f"Processed {csv_file}: {row_count} rows")
            except Exception as e:
                print(f"Error processing {csv_file}: {str(e)}")
                writer.writerow([csv_file, f"Error: {str(e)}"])
    
    print(f"\nResults saved to {output_filename}")

if __name__ == "__main__":
    count_rows_in_csv_files()