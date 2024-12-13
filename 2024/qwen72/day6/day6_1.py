def read_map(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def simulate_guard_path(map):
    # Define the directions: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0  # Start facing up

    # Find the starting position of the guard
    start_row, start_col = None, None
    for i, row in enumerate(map):
        if '^' in row:
            start_row, start_col = i, row.index('^')
            break

    if start_row is None or start_col is None:
        raise ValueError("Guard's starting position not found")

    visited = set()
    visited.add((start_row, start_col))

    current_row, current_col = start_row, start_col

    while True:
        # Check if the next position is out of bounds or an obstacle
        next_row = current_row + directions[direction_index][0]
        next_col = current_col + directions[direction_index][1]

        if (0 <= next_row < len(map) and 0 <= next_col < len(map[0]) and map[next_row][next_col] != '#'):
            current_row, current_col = next_row, next_col
            visited.add((current_row, current_col))
        else:
            # Turn right 90 degrees
            direction_index = (direction_index + 1) % 4

        # Check if the guard has left the mapped area
        if not (0 <= current_row < len(map) and 0 <= current_col < len(map[0])):
            break

    return len(visited)

def main():
    map = read_map('input.txt')
    result = simulate_guard_path(map)
    print(f"The guard will visit {result} distinct positions.")

if __name__ == "__main__":
    main()