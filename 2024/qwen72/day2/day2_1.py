def is_safe(report):
    # Convert the report string to a list of integers
    levels = list(map(int, report.split()))
    
    # Check if the levels are all increasing or all decreasing
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    
    # Check if the levels differ by at least 1 and at most 3
    if is_increasing or is_decreasing:
        for i in range(len(levels) - 1):
            if not (1 <= abs(levels[i] - levels[i + 1]) <= 3):
                return False
        return True
    return False

def count_safe_reports(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            report = line.strip()
            if is_safe(report):
                safe_count += 1
    return safe_count

# Example usage
filename = 'input.txt'
safe_reports = count_safe_reports(filename)
print(f"Number of safe reports: {safe_reports}")