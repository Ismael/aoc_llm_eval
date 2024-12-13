from collections import defaultdict

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    rules = []
    updates = []
    
    i = 0
    while lines[i]:
        rules.append(lines[i])
        i += 1
    
    i += 1  # Skip the blank line
    while i < len(lines):
        updates.append(lines[i].split(','))
        i += 1
    
    return rules, updates

def build_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        x, y = map(int, rule.split('|'))
        graph[x].append(y)
    return graph

def is_valid_order(update, graph):
    positions = {page: i for i, page in enumerate(update)}
    for page in update:
        for next_page in graph[page]:
            if next_page in positions and positions[page] >= positions[next_page]:
                return False
    return True

def find_middle_page(update):
    n = len(update)
    if n % 2 == 1:
        return int(update[n // 2])
    else:
        return None  # No middle page for even-length updates

def solve(file_path):
    rules, updates = parse_input(file_path)
    graph = build_graph(rules)
    
    middle_pages_sum = 0
    for update in updates:
        if is_valid_order(update, graph):
            middle_page = find_middle_page(update)
            if middle_page is not None:
                middle_pages_sum += middle_page
    
    return middle_pages_sum

# Run the solution
result = solve('input.txt')
print(f"The sum of the middle page numbers of the correctly-ordered updates is: {result}")