def count_xmas(grid):
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (1, -1), # diagonal down-left
        (0, -1), # left
        (-1, 0), # up
        (-1, 1), # diagonal up-right
        (-1, -1) # diagonal up-left
    ]
    
    word = "XMAS"
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(len(word)):
                    nr, nc = r + dr * i, c + dc * i
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                        found = False
                        break
                if found:
                    count += 1
    
    return count

# Read the grid from the file
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Count the occurrences of "XMAS"
result = count_xmas(grid)
print(result)
