def is_safe(report):
    increasing = decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
        if abs(diff) > 3 or diff == 0:
            return False

    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if len(new_report) > 1 and is_safe(new_report):
            return True

    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

def main():
    with open('input.txt', 'r') as f:
        reports = [[int(level) for level in line.split()] for line in f.readlines()]
    print(count_safe_reports(reports))

if __name__ == "__main__":
    main()