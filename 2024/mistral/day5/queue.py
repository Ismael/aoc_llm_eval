def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split('\n\n')
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates_section.split('\n')]
    return rules, updates

def is_valid_update(update, rules):
    page_set = set(update)
    for X, Y in rules:
        if X in page_set and Y in page_set:
            if update.index(X) > update.index(Y):
                return False
    return True

def find_middle_page(update):
    n = len(update)
    if n % 2 == 1:
        return update[n // 2]
    else:
        return (update[n // 2 - 1] + update[n // 2]) / 2

def sum_middle_pages(input_data):
    rules, updates = parse_input(input_data)
    total_sum = 0
    for update in updates:
        if is_valid_update(update, rules):
            total_sum += find_middle_page(update)
    return total_sum

# Example input
input_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# Calculate the sum of middle page numbers
result = sum_middle_pages(input_data)
print(result)  # Output should be 143

