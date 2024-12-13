def is_safe(levels):
    if len(levels) < 2:
        return True
    
    def check_sequence(seq):
        if len(seq) < 2:
            return True
        diff = seq[1] - seq[0]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        increasing = diff > 0
        for i in range(2, len(seq)):
            new_diff = seq[i] - seq[i-1]
            if (increasing and new_diff <= 0) or (not increasing and new_diff >= 0):
                return False
            if abs(new_diff) < 1 or abs(new_diff) > 3:
                return False
        return True
    
    # Check if the original sequence is safe
    if check_sequence(levels):
        return True
    
    # Check if removing any single level makes the sequence safe
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if check_sequence(new_levels):
            return True
    
    return False

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
print(f"Number of safe reports with Problem Dampener: {result}")
