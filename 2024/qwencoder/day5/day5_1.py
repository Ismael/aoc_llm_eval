def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Split the input into the rules and updates
    rules = []
    updates = []
    in_updates = False

    for line in lines:
        line = line.strip()
        if not line:
            in_updates = True
            continue

        if not in_updates:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates

def is_correct_order(ordering_rules, update):
    # Create a set of rules that apply to the pages in this update
    applicable_rules = set()
    for x, y in ordering_rules:
        if x in update and y in update:
            applicable_rules.add((x, y))

    # Check if the update respects all applicable rules
    for x, y in applicable_rules:
        if update.index(x) > update.index(y):
            return False

    return True

def find_middle_page_number(update):
    return update[len(update) // 2]

def main():
    rules, updates = parse_input('input.txt')
    middle_page_sum = 0

    for update in updates:
        if is_correct_order(rules, update):
            middle_page_number = find_middle_page_number(update)
            middle_page_sum += middle_page_number

    print(middle_page_sum)

if __name__ == "__main__":
    main()