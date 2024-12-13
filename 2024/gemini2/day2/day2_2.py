def is_safe(report):
    """Checks if a report is safe based on the given rules."""
    if len(report) <= 1:
        return True  # A single level or empty report is considered safe
    
    increasing = None  # None, True, or False
    
    for i in range(len(report) - 1):
      diff = report[i+1] - report[i]

      if diff == 0:
        return False

      if increasing is None:
          increasing = diff > 0
      elif (diff > 0) != increasing:
        return False

      if abs(diff) < 1 or abs(diff) > 3:
        return False

    return True


def is_safe_with_dampener(report):
    """Checks if a report is safe, allowing for one level removal."""
    if is_safe(report): # Report is already safe so dampener is not needed
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(filename):
    """Reads reports from a file and counts the safe ones using the dampener rule."""
    safe_count = 0
    with open(filename, 'r') as f:
        for line in f:
            levels = [int(x) for x in line.strip().split()]
            if is_safe_with_dampener(levels):
                safe_count += 1
    return safe_count

if __name__ == "__main__":
    safe_count = count_safe_reports_with_dampener("input.txt")
    print(f"Number of safe reports (with dampener): {safe_count}")
