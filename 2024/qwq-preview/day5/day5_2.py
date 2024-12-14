def main():
    import sys
    # Read input from a file or standard input
    data = sys.stdin.read().splitlines()

    # Find the separation between rules and updates
    sep = data.index('')
    rules_lines = data[:sep]
    updates_lines = data[sep+1:]

    # Parse rules and build the graph
    graph = {}
    rules = []
    for line in rules_lines:
        X, Y = line.split('|')
        X, Y = int(X), int(Y)
        rules.append((X, Y))
        if X not in graph:
            graph[X] = []
        graph[X].append(Y)

    # Parse updates
    updates = []
    for line in updates_lines:
        pages = list(map(int, line.split(',')))
        updates.append(pages)

    # Function to check if an update is correctly ordered
    def is_correctly_ordered(update, rules):
        pages_set = set(update)
        for X, Y in rules:
            if X in pages_set and Y in pages_set:
                idx_X = update.index(X)
                idx_Y = update.index(Y)
                if idx_X >= idx_Y:
                    return False
        return True

    # Function for topological sort
    def topological_sort(graph, nodes):
        from collections import deque
        indegree = {node: 0 for node in nodes}
        for node in nodes:
            for neighbor in graph.get(node, []):
                if neighbor in nodes:
                    indegree[neighbor] += 1
        queue = deque(sorted([node for node in nodes if indegree[node] == 0]))
        sorted_list = []
        while queue:
            node = queue.popleft()
            sorted_list.append(node)
            for neighbor in graph.get(node, []):
                if neighbor in nodes:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        if len(sorted_list) != len(nodes):
            raise ValueError("Cycle detected in the subgraph")
        return sorted_list

    # Initialize sum of middle pages
    total_sum = 0

    # Process each update
    for update in updates:
        if not is_correctly_ordered(update, rules):
            corrected_order = topological_sort(graph, update)
            n = len(corrected_order)
            if n % 2 == 1:
                middle = corrected_order[n // 2]
                total_sum += middle

    # Output the result
    print(total_sum)

if __name__ == "__main__":
    main()