def find_xmas_pattern(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_xmas_pattern(x, y):
        # Check for the pattern:
        # M . S
        # . A .
        # S . M
        positions = [
            (x-1, y-1), (x-1, y+1),  # Top row
            (x+1, y-1), (x+1, y+1)   # Bottom row
        ]
        # Ensure the positions are within bounds and contain the correct characters
        if (in_bounds(x-1, y-1) and grid[x-1][y-1] in {'M', 'S'} and
            in_bounds(x-1, y+1) and grid[x-1][y+1] in {'M', 'S'} and
            in_bounds(x+1, y-1) and grid[x+1][y-1] in {'M', 'S'} and
            in_bounds(x+1, y+1) and grid[x+1][y+1] in {'M', 'S'}):
            print(f"cazzo at ({x+1}, {y+1})")
            print(grid[x-1][y-1], grid[x-1][y+1], grid[x+1][y-1], grid[x+1][y+1])
            # Check for both configurations of the pattern
            if ((grid[x-1][y-1] == 'M' and grid[x+1][y+1] == 'S' and
                 grid[x+1][y-1] == 'S' and grid[x-1][y+1] == 'M') or
                (grid[x-1][y-1] == 'S' and grid[x+1][y+1] == 'M' and
                 grid[x+1][y-1] == 'M' and grid[x-1][y+1] == 'S') or
                (grid[x-1][y-1] == 'S' and grid[x+1][y+1] == 'M' and
                 grid[x+1][y-1] == 'S' and grid[x-1][y+1] == 'M') or
                (grid[x-1][y-1] == 'M' and grid[x+1][y+1] == 'S' and
                 grid[x+1][y-1] == 'M' and grid[x-1][y+1] == 'S')):
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A' and check_xmas_pattern(i, j):
                count += 1
                print(f"Found X-MAS pattern at ({i+1}, {j+1})")  # Debugging information

    return count

def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    file_path = 'input.txt'
    grid = read_grid(file_path)
    print(grid)
    count = find_xmas_pattern(grid)
    print(f"The X-MAS pattern occurs {count} times in the grid.")

if __name__ == "__main__":
    main()
