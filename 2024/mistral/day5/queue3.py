from collections import defaultdict, deque

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

def topological_sort(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for X, Y in rules:
        if X in update and Y in update:
            graph[X].append(Y)
            in_degree[Y] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        page = queue.popleft()
        sorted_pages.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_pages) == len(update):
        return sorted_pages
    else:
        return None  # Cycle detected or not all pages included

def sum_middle_pages_incorrect_updates(input_data):
    rules, updates = parse_input(input_data)
    total_sum = 0

    for update in updates:
        if not is_valid_update(update, rules):
            sorted_update = topological_sort(update, rules)
            if sorted_update:
                total_sum += find_middle_page(sorted_update)

    return total_sum

# Read input from file
with open('input.txt', 'r') as file:
    input_data = file.read()

# Calculate the sum of middle page numbers for incorrectly-ordered updates
result = sum_middle_pages_incorrect_updates(input_data)
print(result)

