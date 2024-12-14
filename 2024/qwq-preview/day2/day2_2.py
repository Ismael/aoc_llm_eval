import sys

def is_safe(levels):
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    if all(1 <= d <= 3 for d in differences):
        return True  # all increasing by 1-3
    elif all(-3 <= d <= -1 for d in differences):
        return True  # all decreasing by 1-3
    else:
        return False

def is_safe_with_dampener(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False

# Read all reports from standard input
reports = sys.stdin.read().strip().split('\n')

safe_count = 0

for report in reports:
    levels = list(map(int, report.strip().split()))
    if is_safe_with_dampener(levels):
        safe_count += 1

print(safe_count)