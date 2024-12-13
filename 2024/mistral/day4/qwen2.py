def count_xmas_patterns(grid):
    directions = [
        (1, 1),  # diagonal down-right
        (-1, -1), # diagonal up-left
        (1, -1), # diagonal down-left
        (-1, 1)  # diagonal up-right
    ]
    
    word1 = "MAS"
    word2 = "SAM"
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check for MAS in one direction and SAM in the opposite direction
                found1 = True
                found2 = True
                for i in range(len(word1)):
                    nr1, nc1 = r + dr * i, c + dc * i
                    nr2, nc2 = r - dr * i, c - dc * i
                    if nr1 < 0 or nr1 >= rows or nc1 < 0 or nc1 >= cols or grid[nr1][nc1] != word1[i]:
                        found1 = False
                    if nr2 < 0 or nr2 >= rows or nc2 < 0 or nc2 >= cols or grid[nr2][nc2] != word2[i]:
                        found2 = False
                if found1 or found2:
                    count += 1
    
    return count

# Read the grid from the file
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Count the occurrences of X-MAS patterns
result = count_xmas_patterns(grid)
print(result)
