import csv
 
def analyze_csv_data(input_file, output_file):
    # Initialize dictionaries to store column statistics
    column_sums = {}
    column_counts = {}
    column_min = {}
    column_max = {}
 
    # Read the CSV file
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Skip the header row
 
        # Initialize column statistics dictionaries
        for col in header:
            column_sums[col] = 0
            column_counts[col] = 0
            column_min[col] = float('inf')
            column_max[col] = float('-inf')
 
        # Process each row
        for row in csvreader:
            for col, value in zip(header, row):
                if col != 'City':  # Skip non-numeric columns
                    numeric_value = float(value)
                    column_sums[col] += numeric_value
                    column_counts[col] += 1
                    column_min[col] = min(column_min[col], numeric_value)
                    column_max[col] = max(column_max[col], numeric_value)
 
    # Calculate averages
    averages = {col: column_sums[col] / column_counts[col] for col in header if col != 'City'}
 
    # Write results to a new CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Metric', 'Value'])
        writer.writerow(['Number of data points', len(column_counts)])
        for col in header:
            if col != 'City':
                writer.writerow([f'Average of {col}', averages[col]])
                writer.writerow([f'Minimum of {col}', column_min[col]])
                writer.writerow([f'Maximum of {col}', column_max[col]])
 
# Example usage
input_file = 'C:\\Python_practice\\python_practice\\Exercise\\inflow.txt'
output_file = 'outflow.txt'
analyze_csv_data(input_file, output_file)