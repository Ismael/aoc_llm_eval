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

def count_distinct_positions(map_data):
    start_pos, start_dir = find_guard_start(map_data)
    if start_pos is None:
        return 0
    visited = move_guard(map_data, start_pos, start_dir)
    return len(visited)

def main():
    map_data = read_input('input_test.txt')
    distinct_positions = count_distinct_positions(map_data)
    print(distinct_positions)

if __name__ == "__main__":
    main()
