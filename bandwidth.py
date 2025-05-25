import pandas as pd

def calculate_network_bandwidth(input_file, output_file=None):
    """
    Calculate total network bandwidth by summing client throughputs at each timestamp.
    
    Args:
        input_file (str): Path to input CSV file with columns [client_id, time, value]
        output_file (str, optional): Path to save results. If None, results won't be saved.
    
    Returns:
        pd.DataFrame: DataFrame with time and total bandwidth
    """
    # Read the input file
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading input file: {e}")
        return None
    
    # Validate required columns
    required_columns = ['client_id', 'time', 'value']
    if not all(col in df.columns for col in required_columns):
        print("Error: Input file must contain columns: client_id, time, value")
        return None
    
    # Group by time and sum the throughput values
    bandwidth_df = df.groupby('time')['value'].sum().reset_index()
    bandwidth_df.columns = ['time', 'total_bandwidth']
    
    # Sort by time if needed
    bandwidth_df = bandwidth_df.sort_values('time')
    
    # Save to file if output path provided
    if output_file:
        try:
            bandwidth_df.to_csv(output_file, index=False)
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error saving results: {e}")
    
    return bandwidth_df

# Example usage
if __name__ == "__main__":
    input_csv = "throughput.csv"  # Replace with your input file path
    output_csv = "bandwidth.csv"  # Optional output file
    
    result = calculate_network_bandwidth(input_csv, output_csv)
    
    if result is not None:
        print("\nNetwork Bandwidth Calculation Results:")
        print(result.head())