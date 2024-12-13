def read_input(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid

def find_guard(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in "^v><":
                return (i, j), cell
    return None, None

def turn_right(direction):
    if direction == '^': return '>'
    if direction == '>': return 'v'
    if direction == 'v': return '<'
    if direction == '<': return '^'

def move_forward(position, direction):
    x, y = position
    if direction == '^': return (x - 1, y)
    if direction == 'v': return (x + 1, y)
    if direction == '>': return (x, y + 1)
    if direction == '<': return (x, y - 1)

def is_outside(grid, position):
    x, y = position
    return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])

def simulate_patrol(grid):
    # Initialize the guard's position and direction
    position, direction = find_guard(grid)
    visited = set()
    
    # Start the simulation loop
    while not is_outside(grid, position):
        # Mark the current position as visited
        visited.add(position)
        
        # Compute the position in front of the guard
        next_position = move_forward(position, direction)
        
        # Check if there's an obstacle
        if is_outside(grid, next_position) or grid[next_position[0]][next_position[1]] == '#':
            # Turn right if there's an obstacle
            direction = turn_right(direction)
        else:
            # Move forward if there's no obstacle
            position = next_position

    return len(visited)

if __name__ == "__main__":
    # Read the input from the file
    grid = read_input('input.txt')
    
    # Simulate the patrol and print the number of distinct positions visited
    result = simulate_patrol(grid)
    print(result)
