def read_map(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def simulate_guard_path(map, obstruction=None):
    # Define the directions: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0  # Start facing up

    # Find the startingPosition
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

        if (0 <= next_row < len(map) and 0 <= next_col < len(map[0]) and (map[next_row][next_col] != '#' and (next_row, next_col) != obstruction)):
            current_row, current_col = next_row, next_col
            visited.add((current_row, current_col))
        else:
            # Turn right 90 degrees
            direction_index = (direction_index + 1) % 4

        # Check if the guard has left the mapped area
        if not (0 <= current_row < len(map) and 0 <= current_col < len(map[0])):
            return False, visited

        # Check if the guard is in a loop
        if len(visited) > 10000:  # Arbitrary large number to detect a loop
            return True, visited

def find_possible_obstructions(map):
    possible_obstructions = set()

    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == '.' and (row, col) != (start_row, start_col):
                new_map = [list(row) for row in map]
                new_map[row] = new_map[row][:col] + '#' + new_map[row][col + 1:]
                loop_detected, _ = simulate_guard_path(new_map, (row, col))

                if loop_detected:
                    possible_obstructions.add((row, col))

    return len(possible_obstructions)

def main():
    map = read_map('input.txt')
    result = find_possible_obstructions(map)
    print(f"There are {result} different positions where you could place an obstruction to get the guard stuck in a loop.")

if __name__ == "__main__":
    main()