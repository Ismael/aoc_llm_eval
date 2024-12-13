def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_xmas(x, y):
        # Check the X pattern
        if (in_bounds(x-1, y-1) and in_bounds(x-1, y+1) and in_bounds(x+1, y-1) and in_bounds(x+1, y+1) and
            grid[x-1][y-1] == 'M' and grid[x-1][y+1] == 'A' and grid[x+1][y-1] == 'S' and grid[x+1][y+1] == 'M' and
            grid[x][y] == 'A'):
            return True
        if (in_bounds(x-1, y-1) and in_bounds(x-1, y+1) and in_bounds(x+1, y-1) and in_bounds(x+1, y+1) and
            grid[x-1][y-1] == 'S' and grid[x-1][y+1] == 'A' and grid[x+1][y-1] == 'M' and grid[x+1][y+1] == 'S' and
            grid[x][y] == 'A'):
            return True
        return False

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if check_xmas(i, j):
                count += 1

    return count

def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    file_path = 'input.txt'
    grid = read_grid(file_path)
    count = find_xmas(grid)
    print(f"The word 'X-MAS' occurs {count} times in the grid.")

if __name__ == "__main__":
    main()
