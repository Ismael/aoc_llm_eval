import sys

def extract_word(i, j, dr, dc, grid, length=4):
    word = ""
    current_i = i
    current_j = j
    for _ in range(length):
        if 0 <= current_i < grid_height and 0 <= current_j < grid_width:
            word += grid[current_i][current_j]
            current_i += dr
            current_j += dc
        else:
            return None
    return word

if __name__ == "__main__":
    grid = sys.stdin.read().splitlines()
    grid_height = len(grid)
    grid_width = len(grid[0]) if grid_height > 0 else 0
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    count = 0
    for i in range(grid_height):
        for j in range(grid_width):
            for dr, dc in directions:
                word = extract_word(i, j, dr, dc, grid)
                if word == "XMAS":
                    count += 1
    print(count)