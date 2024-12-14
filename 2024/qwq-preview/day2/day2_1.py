import sys

def is_safe(levels):
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    if all(1 <= d <= 3 for d in differences):
        return True  # all increasing by 1-3
    elif all(-3 <= d <= -1 for d in differences):
        return True  # all decreasing by 1-3
    else:
        return False

# Read all reports from standard input
reports = sys.stdin.read().strip().split('\n')

safe_count = 0

for report in reports:
    levels = list(map(int, report.strip().split()))
    if is_safe(levels):
        safe_count += 1

print(safe_count)