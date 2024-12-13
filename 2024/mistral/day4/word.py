def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    count = 0

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x, y, dx, dy):
        word = "XMAS"
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1

    return count

def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    file_path = 'input.txt'
    grid = read_grid(file_path)
    count = find_xmas(grid)
    print(f"The word 'XMAS' occurs {count} times in the grid.")

if __name__ == "__main__":
    main()
