from collections import deque

def read_map(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(topo_map):
    return [(i, j) for i in range(len(topo_map)) for j in range(len(topo_map[0])) if topo_map[i][j] == 0]

def calculate_score(topo_map, start):
    rows, cols = len(topo_map), len(topo_map[0])
    visited = set()
    queue = deque([(start, 0)])
    score = 0

    while queue:
        (x, y), height = queue.popleft()
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        if topo_map[x][y] == 9:
            score += 1
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and topo_map[nx][ny] == height + 1:
                queue.append(((nx, ny), height + 1))

    return score

def solve_puzzle(topo_map):
    trailheads = find_trailheads(topo_map)
    return sum(calculate_score(topo_map, trailhead) for trailhead in trailheads)

# Main execution
topo_map = read_map('input.txt')
result = solve_puzzle(topo_map)
print(f"The sum of the scores of all trailheads is: {result}")
