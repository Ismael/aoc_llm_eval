def count_xmas(grid):
    directions = [
        (1, 1),  # diagonal down-right
        (1, -1), # diagonal down-left
        (-1, 1), # diagonal up-right
        (-1, -1) # diagonal up-left
    ]
    
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':
                for dr, dc in directions:
                    # Check if the indices for the pattern are within bounds
                    if (0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] in ['M', 'S'] and
                        0 <= r + 2 * dr < rows and 0 <= c + 2 * dc < cols and grid[r + 2 * dr][c + 2 * dc] in ['M', 'S']):
                        if (grid[r + dr][c + dc] == 'M' and grid[r + 2 * dr][c + 2 * dc] == 'S') or \
                           (grid[r + dr][c + dc] == 'S' and grid[r + 2 * dr][c + 2 * dc] == 'M'):
                            count += 1
    
    return count

# Define the grid
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

# Count the occurrences of X-MAS
result = count_xmas(grid)
print(result)
