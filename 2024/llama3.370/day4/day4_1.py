def find_xmas(grid):
    """
    Find all occurrences of "XMAS" in the given grid.

    Args:
    grid (list of str): The grid of letters.

    Returns:
    int: The number of times "XMAS" appears in the grid.
    """
    count = 0
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
        (-1, 0),  # up
        (-1, 1),  # up-right
        (-1, -1),  # up-left
        (0, -1)  # left
    ]

    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def is_xmas(x, y, dx, dy):
        chars = "XMAS"
        for i, char in enumerate(chars):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny]!= char:
                return False
        return True

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for dx, dy in directions:
                if is_xmas(i, j, dx, dy):
                    count += 1

    # Check for reversed "XMAS"
    reversed_grid = [row[::-1] for row in grid]
    for i in range(len(reversed_grid)):
        for j in range(len(reversed_grid[0])):
            for dx, dy in directions:
                if is_xmas(i, j, dx, dy):
                    count += 1

    return count

def main():
    with open("input.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]
    print(find_xmas(grid))

if __name__ == "__main__":
    main()