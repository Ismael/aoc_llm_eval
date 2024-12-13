def read_grid(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_xmas(r, c):
        # Check the pattern
        if (r + 2 < rows and c + 2 < cols and
            grid[r][c] == 'M' and grid[r + 1][c + 1] == 'A' and grid[r + 2][c] == 'M' and grid[r][c + 2] == 'M'):
            return True
        return False

    for r in range(rows):
        for c in range(cols):
            if is_xmas(r, c):
                count += 1

    return count

def main():
    grid = read_grid('input.txt')
    count = find_xmas(grid)
    print(f"The X-MAS pattern appears {count} times in the word search.")

if __name__ == "__main__":
    main()