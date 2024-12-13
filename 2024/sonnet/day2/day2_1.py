def is_safe(levels):
    if len(levels) < 2:
        return True
    
    diff = levels[1] - levels[0]
    if abs(diff) < 1 or abs(diff) > 3:
        return False
    
    increasing = diff > 0
    
    for i in range(2, len(levels)):
        new_diff = levels[i] - levels[i-1]
        if (increasing and new_diff <= 0) or (not increasing and new_diff >= 0):
            return False
        if abs(new_diff) < 1 or abs(new_diff) > 3:
            return False
    
    return True

def count_safe_reports(filename):
    safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            if is_safe(levels):
                safe_count += 1
    
    return safe_count

# Solve the puzzle
input_file = 'input.txt'
result = count_safe_reports(input_file)
print(f"Number of safe reports: {result}")
