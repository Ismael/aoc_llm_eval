def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_guard_start(map_data):
    for y, row in enumerate(map_data):
        for x, cell in enumerate(row):
            if cell in '^>v<':
                return (x, y), cell
    return None, None

def move_guard(map_data, start_pos, start_dir):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    pos = start_pos
    dir = start_dir
    visited = set()
    visited.add(pos)

    while True:
        dx, dy = directions[dir]
        new_x, new_y = pos[0] + dx, pos[1] + dy

        if 0 <= new_y < len(map_data) and 0 <= new_x < len(map_data[new_y]):
            if map_data[new_y][new_x] == '#':
                dir = turn_right[dir]
            else:
                pos = (new_x, new_y)
                visited.add(pos)
        else:
            break

    return visited

def simulate_with_obstruction(map_data, obstruction_pos):
    start_pos, start_dir = find_guard_start(map_data)
    if start_pos is None:
        return False

    # Create a copy of the map with the new obstruction
    new_map = [list(row) for row in map_data]
    ox, oy = obstruction_pos
    new_map[oy][ox] = '#'

    # Simulate the guard's movement with the new obstruction
    visited = set()
    pos = start_pos
    dir = start_dir
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    while True:
        dx, dy = directions[dir]
        new_x, new_y = pos[0] + dx, pos[1] + dy

        if 0 <= new_y < len(new_map) and 0 <= new_x < len(new_map[new_y]):
            if new_map[new_y][new_x] == '#':
                dir = turn_right[dir]
            else:
                pos = (new_x, new_y)
                if pos in visited:
                    return True  # Loop detected
                visited.add(pos)
        else:
            break

    return False

def count_obstruction_positions(map_data):
    start_pos, _ = find_guard_start(map_data)
    if start_pos is None:
        return 0

    obstruction_positions = 0
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if (x, y) != start_pos and map_data[y][x] != '#':
                if simulate_with_obstruction(map_data, (x, y)):
                    obstruction_positions += 1

    return obstruction_positions

def main():
    map_data = read_input('input.txt')
    obstruction_positions = count_obstruction_positions(map_data)
    print(obstruction_positions)

if __name__ == "__main__":
    main()
