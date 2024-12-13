def is_safe_report(report):
    # Convert the report string to a list of integers
    levels = list(map(int, report.split()))
    
    # Check if the report is empty or has only one level
    if len(levels) < 2:
        return True
    
    # Determine the direction of the sequence (increasing or decreasing)
    direction = None  # None means undetermined, 1 means increasing, -1 means decreasing
    
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        
        if diff == 0:
            return False  # No change between levels is not allowed
        
        if abs(diff) > 3:
            return False  # Difference between levels must be between 1 and 3
        
        if direction is None:
            direction = 1 if diff > 0 else -1
        else:
            if (direction == 1 and diff < 0) or (direction == -1 and diff > 0):
                return False  # Sequence must be consistently increasing or decreasing
    
    return True

def count_safe_reports(filename):
    safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            if is_safe_report(line.strip()):
                safe_count += 1
    
    return safe_count

# Specify the input file
input_filename = 'input.txt'

# Count and print the number of safe reports
safe_reports_count = count_safe_reports(input_filename)
print(f"Number of safe reports: {safe_reports_count}")