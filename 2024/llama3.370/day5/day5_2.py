from collections import defaultdict, deque

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    rules = []
    updates = []
    parsing_rules = True
    for line in lines:
        if line.strip() == '':
            parsing_rules = False
            continue
        if parsing_rules:
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
        else:
            updates.append(list(map(int, line.strip().split(','))))
    return rules, updates

def is_correctly_ordered(update, rules):
    for x, y in rules:
        if x in update and y in update and update.index(y) < update.index(x):
            return False
    return True

def topological_sort(update, rules):
    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []
    while queue:
        page = queue.popleft()
        sorted_update.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update

def middle_page(update):
    return update[len(update) // 2]

def main():
    rules, updates = read_input('input.txt')
    incorrectly_ordered_updates = [update for update in updates if not is_correctly_ordered(update, rules)]
    correctly_ordered_updates = [topological_sort(update, rules) for update in incorrectly_ordered_updates]
    middle_pages = [middle_page(update) for update in correctly_ordered_updates]
    print(sum(middle_pages))

if __name__ == '__main__':
    main()