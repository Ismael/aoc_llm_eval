def is_valid_order(pages, rules):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if f"{pages[j]}|{pages[i]}" in rules:
                return False
    return True

def find_middle_page(pages):
    return pages[len(pages) // 2]

# Read input from file
with open('input.txt', 'r') as file:
    content = file.read().strip().split('\n\n')

# Parse rules
rules = set(content[0].split('\n'))

# Parse updates
updates = [list(map(int, update.split(','))) for update in content[1].split('\n')]

# Process updates
valid_updates = []
for update in updates:
    if is_valid_order(update, rules):
        valid_updates.append(update)

# Calculate sum of middle pages
middle_sum = sum(find_middle_page(update) for update in valid_updates)

print(f"Sum of middle pages from correctly-ordered updates: {middle_sum}")
