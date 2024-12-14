import sys

# Read the map from standard input
inputs = sys.stdin.read().splitlines()
map = [list(map(int, list(line.strip()))) for line in inputs if line.strip()]

# Get the dimensions of the map
R = len(map)
C = len(map[0]) if R > 0 else 0

# Define directions for moving up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to perform DP from a given trailhead
def dp(start_row, start_col, map):
    paths = [[0 for _ in range(C)] for _ in range(R)]
    paths[start_row][start_col] = 1
    for height in range(0, 9):
        for r in range(R):
            for c in range(C):
                if map[r][c] == height:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C:
                            if map[nr][nc] == height + 1:
                                paths[nr][nc] += paths[r][c]
    # Sum paths for all cells with height 9
    return sum(paths[r][c] for r in range(R) for c in range(C) if map[r][c] == 9)

# Find all trailheads (positions with height 0)
trailheads = [(r, c) for r in range(R) for c in range(C) if map[r][c] == 0]

# Calculate the total rating by summing up ratings from all trailheads
total_rating = sum(dp(r, c, map) for r, c in trailheads)

# Output the result
print(total_rating)