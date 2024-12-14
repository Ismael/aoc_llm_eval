import sys

def main():
    # Read input from a file or standard input
    data = sys.stdin.read().splitlines()

    # Find the separation between rules and updates
    sep = data.index('')
    rules_lines = data[:sep]
    updates_lines = data[sep+1:]

    # Parse rules
    rules = []
    for line in rules_lines:
        X, Y = line.split('|')
        rules.append((int(X), int(Y)))

    # Parse updates
    updates = []
    for line in updates_lines:
        pages = list(map(int, line.split(',')))
        updates.append(pages)

    # Initialize sum of middle pages
    total_sum = 0

    # Check each update
    for update in updates:
        pages_set = set(update)
        is_correct = True
        for X, Y in rules:
            if X in pages_set and Y in pages_set:
                idx_X = update.index(X)
                idx_Y = update.index(Y)
                if idx_X >= idx_Y:
                    is_correct = False
                    break
        if is_correct:
            n = len(update)
            if n % 2 == 1:
                middle = update[n // 2]
                total_sum += middle

    # Output the result
    print(total_sum)

if __name__ == "__main__":
    main()