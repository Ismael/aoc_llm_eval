from collections import defaultdict, deque

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
    in_degree = defaultdict(int)
    
    for rule in rules:
        x, y = map(int, rule.split('|'))
        graph[x].append(y)
        in_degree[y] += 1
    
    return graph, in_degree

def topological_sort(update, graph, in_degree):
    order = []
    queue = deque([page for page in update if in_degree[page] == 0])
    
    while queue:
        page = queue.popleft()
        order.append(page)
        
        for next_page in graph[page]:
            in_degree[next_page] -= 1
            if in_degree[next_page] == 0:
                queue.append(next_page)
    
    return order

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
    graph, in_degree = build_graph(rules)
    
    middle_pages_sum = 0
    for update in updates:
        update = list(map(int, update))
        if not is_valid_order(update, graph):
            correct_order = topological_sort(update, graph, in_degree.copy())
            middle_page = find_middle_page(correct_order)
            if middle_page is not None:
                middle_pages_sum += middle_page
    
    return middle_pages_sum

# Run the solution
result = solve('input.txt')
print(f"The sum of the middle page numbers of the correctly-ordered updates is: {result}")