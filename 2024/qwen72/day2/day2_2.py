def is_safe(report):
    # Convert the report string to a list of integers
    levels = list(map(int, report.split()))
    
    # Helper function to check if a list of levels is safe
    def is_safe_list(lst):
        is_increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
        is_decreasing = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
        if is_increasing or is_decreasing:
            for i in range(len(lst) - 1):
                if not (1 <= abs(lst[i] - lst[i + 1]) <= 3):
                    return False
            return True
        return False
    
    # Check if the original report is safe
    if is_safe_list(levels):
        return True
    
    # Check if removing any single level makes the report safe
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_list(new_levels):
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