def parse_input(filename):
    with open(filename, 'r') as file:
        map = [list(map(int, line.strip())) for line in file]
    return map

def find_trailheads(map):
    trailheads = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(map, x, y, current_height):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return False
    if map[x][y] != current_height + 1:
        return False
    return True

def explore_trail(map, x, y, current_height, visited, paths):
    if map[x][y] == 9:
        paths.append((x, y))
        return
    visited.add((x, y))
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited and is_valid_move(map, nx, ny, current_height):
            explore_trail(map, nx, ny, current_height + 1, visited, paths)
    visited.remove((x, y))

def calculate_rating(map, trailhead):
    x, y = trailhead
    visited = set()
    paths = []
    explore_trail(map, x, y, 0, visited, paths)
    return len(set(paths))

def sum_of_ratings(map):
    trailheads = find_trailheads(map)
    total_rating = 0
    for trailhead in trailheads:
        total_rating += calculate_rating(map, trailhead)
    return total_rating

def main():
    map = parse_input('input.txt')
    total_rating = sum_of_ratings(map)
    print(f"The sum of the ratings of all trailheads is: {total_rating}")

if __name__ == "__main__":
    main()