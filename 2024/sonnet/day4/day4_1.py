def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1), (1, 0), (1, 1), (-1, 1),  # right, down, diagonal down-right, diagonal up-right
        (0, -1), (-1, 0), (-1, -1), (1, -1)  # left, up, diagonal up-left, diagonal down-left
    ]
    count = 0

    def check_xmas(x, y, dx, dy):
        if 0 <= x + 3*dx < rows and 0 <= y + 3*dy < cols:
            return grid[x][y] == 'X' and grid[x+dx][y+dy] == 'M' and \
                   grid[x+2*dx][y+2*dy] == 'A' and grid[x+3*dx][y+3*dy] == 'S'
        return False

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_xmas(i, j, dx, dy):
                    count += 1

    return count

# Read input from file
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

# Count XMAS occurrences
result = count_xmas(grid)

print(f"XMAS appears {result} times in the word search.")
