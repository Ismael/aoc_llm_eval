import sys
from collections import deque

# Read the map from standard input
inputs = sys.stdin.read().splitlines()
map = [list(map(int, list(line.strip()))) for line in inputs if line.strip()]

# Get the dimensions of the map
R = len(map)
C = len(map[0]) if R > 0 else 0

# Define directions for moving up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to perform BFS from a given trailhead
def bfs(start_row, start_col, map):
    visited = set()
    queue = deque()
    queue.append((start_row, start_col))
    count = 0
    while queue:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if map[row][col] == 9:
            count += 1
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row < R and 0 <= new_col < C:
                if map[new_row][new_col] == map[row][col] + 1:
                    queue.append((new_row, new_col))
    return count

# Find all trailheads (positions with height 0)
trailheads = [(r, c) for r in range(R) for c in range(C) if map[r][c] == 0]

# Calculate the total score by summing up scores from all trailheads
total_score = sum(bfs(r, c, map) for r, c in trailheads)

# Output the result
print(total_score)