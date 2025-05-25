def count_lines(file_path):
    """
    Count the number of lines in a large text file efficiently.
    
    Args:
        file_path (str): Path to the text file to be counted.
    
    Returns:
        int: Number of lines in the file.
    """
    line_count = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
        print(f"The file '{file_path}' contains {line_count} lines.")
        return line_count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1

# Example usage (modify the file path as needed)
file_to_count = 'endToEndDelay.vec'  # Replace with your file path
count_lines(file_to_count)