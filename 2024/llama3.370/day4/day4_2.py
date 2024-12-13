def find_xmas(grid):
    """
    Find all occurrences of the X-MAS shape in the given grid.

    Args:
    grid (list of str): The grid of letters.

    Returns:
    int: The number of times the X-MAS shape appears in the grid.
    """
    count = 0
    directions = [
        (1, 1),  # down-right
        (1, -1),  # down-left
        (-1, -1),  # up-left
        (-1, 1)  # up-right
    ]

    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def is_mas(x, y, dx, dy):
        chars = "MAS"
        for i, char in enumerate(chars):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny]!= char:
                return False
        return True

    def is_mas_reversed(x, y, dx, dy):
        chars = "SAM"
        for i, char in enumerate(chars):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny]!= char:
                return False
        return True

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if is_mas(i, j, dx, dy) and is_mas(i + dx, j + dy, -dx, -dy):
                    count += 1
                if is_mas_reversed(i, j, dx, dy) and is_mas_reversed(i + dx, j + dy, -dx, -dy):
                    count += 1

    return count

def main():
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]
    print(find_xmas(grid))

if __name__ == "__main__":
    main()