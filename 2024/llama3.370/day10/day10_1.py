def read_input(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]


def is_valid_move(x, y, prev_height, grid):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y] == prev_height + 1
    return False


def find_trails(x, y, grid, visited):
    if grid[x][y] == 9:
        return 1
    count = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, grid[x][y], grid) and (nx, ny) not in visited:
            visited.add((nx, ny))
            count += find_trails(nx, ny, grid, visited)
            visited.remove((nx, ny))
    return count


def find_trailheads(grid):
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                visited = set()
                visited.add((i, j))
                trailheads.append(find_trails(i, j, grid, visited))
    return trailheads


def main():
    grid = read_input('input.txt')
    trailheads = find_trailheads(grid)
    print(sum(trailheads))


if __name__ == "__main__":
    main()