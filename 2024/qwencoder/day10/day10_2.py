from collections import defaultdict

def read_map(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def get_neighbors(x, y, rows, cols):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny

def dfs_trailhead_rating(map, start_x, start_y, memo):
    rows, cols = len(map), len(map[0])
    stack = [(start_x, start_y)]
    visited = set()
    rating = 0
    
    while stack:
        x, y = stack.pop()
        if map[x][y] == 9:
            rating += 1
            continue
        for nx, ny in get_neighbors(x, y, rows, cols):
            if map[nx][ny] == map[x][y] + 1:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
                else:
                    # If already visited, use memoization to avoid redundant calculations
                    if (nx, ny) in memo:
                        rating += memo[(nx, ny)]
    
    # Store the result in memoization dictionary
    memo[(start_x, start_y)] = rating
    return rating

def calculate_total_ratings(map):
    rows, cols = len(map), len(map[0])
    total_rating = 0
    memo = defaultdict(int)
    
    for x in range(rows):
        for y in range(cols):
            if map[x][y] == 0:
                total_rating += dfs_trailhead_rating(map, x, y, memo)
    
    return total_rating

# Read the map from the input file
map = read_map('input.txt')

# Calculate the total rating of all trailheads
total_rating = calculate_total_ratings(map)

# Print the result
print(total_rating)