from collections import deque

def read_map(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def get_neighbors(x, y, rows, cols):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny

def bfs_trailhead_score(map, start_x, start_y):
    rows, cols = len(map), len(map[0])
    visited = set()
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    reachable_nines = 0
    
    while queue:
        x, y = queue.popleft()
        if map[x][y] == 9:
            reachable_nines += 1
        for nx, ny in get_neighbors(x, y, rows, cols):
            if (nx, ny) not in visited and map[nx][ny] == map[x][y] + 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return reachable_nines

def calculate_total_scores(map):
    rows, cols = len(map), len(map[0])
    total_score = 0
    
    for x in range(rows):
        for y in range(cols):
            if map[x][y] == 0:
                total_score += bfs_trailhead_score(map, x, y)
    
    return total_score

# Read the map from the input file
map = read_map('input.txt')

# Calculate the total score of all trailheads
total_score = calculate_total_scores(map)

# Print the result
print(total_score)