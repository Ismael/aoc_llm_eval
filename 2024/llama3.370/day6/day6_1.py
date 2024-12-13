def load_map(filename):
    """Load the map from a file."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def find_guard(map):
    """Find the initial position and direction of the guard."""
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == '^':
                return (x, y, 'up')
            elif cell == 'v':
                return (x, y, 'down')
            elif cell == '<':
                return (x, y, 'left')
            elif cell == '>':
                return (x, y, 'right')
    raise ValueError("Guard not found")

def move_guard(x, y, direction, map):
    """Move the guard according to the protocol."""
    if direction == 'up':
        dx, dy = 0, -1
    elif direction == 'down':
        dx, dy = 0, 1
    elif direction == 'left':
        dx, dy = -1, 0
    elif direction == 'right':
        dx, dy = 1, 0

    new_x, new_y = x + dx, y + dy

    if (new_x < 0 or new_x >= len(map[0]) or
            new_y < 0 or new_y >= len(map) or
            map[new_y][new_x] == '#'):
        # Turn right and try again
        if direction == 'up':
            direction = 'right'
        elif direction == 'right':
            direction = 'down'
        elif direction == 'down':
            direction = 'left'
        elif direction == 'left':
            direction = 'up'
        return (x, y, direction)
    else:
        return (new_x, new_y, direction)

def predict_path(map):
    """Predict the path of the guard and calculate the number of distinct positions visited."""
    x, y, direction = find_guard(map)
    visited = {(x, y)}
    while 0 <= x < len(map[0]) and 0 <= y < len(map):
        x, y, direction = move_guard(x, y, direction, map)
        if (x, y) not in visited:
            visited.add((x, y))
    return len(visited)

def main():
    map = load_map('input.txt')
    print(predict_path(map))

if __name__ == '__main__':
    main()