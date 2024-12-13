import os

def is_safe(report):
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    if not (increasing or decreasing):
        return False
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3):
            return False
    return True

def count_safe_reports(data):
    safe_count = 0
    for report in data:
        if is_safe(report):
            safe_count += 1
    return safe_count

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [list(map(int, line.split())) for line in lines]
    return data

# Example usage
file_path = 'input.txt'
if os.path.exists(file_path):
    data = read_data_from_file(file_path)
    safe_reports = count_safe_reports(data)
    print(f"Number of safe reports: {safe_reports}")
else:
    print(f"File not found: {file_path}")
