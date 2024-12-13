def is_safe(report):
    """
    Check if a report is safe.
    
    A report is safe if its levels are either all increasing or all decreasing,
    and any two adjacent levels differ by at least one and at most three.
    
    Args:
        report (list): A list of integers representing the levels in the report.
    
    Returns:
        bool: True if the report is safe, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        
        # Check if the difference is within the allowed range
        if diff < 1 or diff > 3:
            return False
        
        # Check if the levels are increasing or decreasing
        if report[i] < report[i + 1]:
            decreasing = False
        elif report[i] > report[i + 1]:
            increasing = False
    
    # A report is safe if it's either all increasing or all decreasing
    return increasing or decreasing

def count_safe_reports(reports):
    """
    Count the number of safe reports.
    
    Args:
        reports (list): A list of lists, where each sublist represents a report.
    
    Returns:
        int: The number of safe reports.
    """
    safe_count = 0
    
    for report in reports:
        if is_safe(report):
            safe_count += 1
    
    return safe_count

def read_reports_from_file(filename):
    """
    Read reports from a file.
    
    Args:
        filename (str): The name of the file containing the reports.
    
    Returns:
        list: A list of lists, where each sublist represents a report.
    """
    reports = []
    
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            reports.append(report)
    
    return reports

def main():
    filename = 'input.txt'
    reports = read_reports_from_file(filename)
    safe_count = count_safe_reports(reports)
    
    print(f'Number of safe reports: {safe_count}')

if __name__ == '__main__':
    main()