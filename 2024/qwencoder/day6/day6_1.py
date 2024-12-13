# Function to read the map from a file
def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

# Function to simulate the guard's movement
def simulate_guard_movement(grid):
    # Define the directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_names = ['up', 'right', 'down', 'left']
    
    # Find the initial position of the guard
    start_row, start_col = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                start_row, start_col = i, j
                break
        if start_row is not None:
            break
    
    if start_row is None:
        raise ValueError("Guard's starting position not found!")
    
    # Initialize the guard's position and direction
    row, col = start_row, start_col
    direction_index = 0  # Initially facing up
    
    # Set to keep track of visited positions
    visited_positions = set()
    visited_positions.add((row, col))
    
    while True:
        # Check the position in front of the guard
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        if (0 <= next_row < len(grid) and 0 <= next_col < len(grid[next_row]) and
            grid[next_row][next_col] != '#'):
            # Move forward
            row, col = next_row, next_col
        else:
            # Turn right
            direction_index = (direction_index + 1) % 4
        
        # Add the current position to visited positions
        visited_positions.add((row, col))
        
        # Check if the guard has exited the map
        if not (0 <= row < len(grid) and 0 <= col < len(grid[row])):
            break
    
    return len(visited_positions)

# Read the map from the file
grid = read_map('input.txt')

# Simulate the guard's movement and get the number of distinct positions visited
distinct_positions_visited = simulate_guard_movement(grid)

# Print the result
print(distinct_positions_visited)