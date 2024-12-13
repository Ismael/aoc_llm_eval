def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def check_mas(x, y, dx, dy):
        if 0 <= x + 2*dx < rows and 0 <= y + 2*dy < cols:
            return (grid[x][y] == 'M' and grid[x+dx][y+dy] == 'A' and grid[x+2*dx][y+2*dy] == 'S') or \
                   (grid[x][y] == 'S' and grid[x+dx][y+dy] == 'A' and grid[x+2*dx][y+2*dy] == 'M')
        return False

    def check_x_mas(x, y):
        directions = [
            ((1, 1), (-1, 1)),  # down-right and up-right
            ((1, -1), (-1, -1)),  # down-left and up-left
        ]
        for d1, d2 in directions:
            if check_mas(x, y, d1[0], d1[1]) and check_mas(x, y, d2[0], d2[1]):
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if check_x_mas(i, j):
                count += 1

    return count

# Read input from file
with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

# Count X-MAS occurrences
result = count_x_mas(grid)

print(f"X-MAS appears {result} times in the word search.")
