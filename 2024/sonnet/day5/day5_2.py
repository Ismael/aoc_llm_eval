from itertools import permutations

def is_valid_order(pages, rules):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if f"{pages[j]}|{pages[i]}" in rules:
                return False
    return True

def find_middle_page(pages):
    return pages[len(pages) // 2]

def correct_order(pages, rules):
    for perm in permutations(pages):
        if is_valid_order(perm, rules):
            return list(perm)
    return None  # This should not happen if the input is valid

# Read input from file
with open('input.txt', 'r') as file:
    content = file.read().strip().split('\n\n')

# Parse rules
rules = set(content[0].split('\n'))

# Parse updates
updates = [list(map(int, update.split(','))) for update in content[1].split('\n')]

# Process updates
invalid_updates = []
for update in updates:
    if not is_valid_order(update, rules):
        invalid_updates.append(update)

# Correct the order of invalid updates and find middle pages
corrected_middle_pages = []
for update in invalid_updates:
    corrected_update = correct_order(update, rules)
    if corrected_update:
        corrected_middle_pages.append(find_middle_page(corrected_update))

# Calculate sum of middle pages from corrected invalid updates
middle_sum = sum(corrected_middle_pages)

print(f"Sum of middle pages from corrected invalid updates: {middle_sum}")
