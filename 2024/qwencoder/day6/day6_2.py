# Function to read the map from a file
def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

# Function to simulate the guard's movement with an obstruction at a specific position
def simulate_guard_movement_with_obstruction(grid, obstruction_position):
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
    
    # Set to keep track of the last few positions to detect loops
    last_positions = []
    
    while True:
        # Check the position in front of the guard
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        if (0 <= next_row < len(grid) and 0 <= next_col < len(grid[next_row]) and
            grid[next_row][next_col] != '#' and (next_row, next_col) != obstruction_position):
            # Move forward
            row, col = next_row, next_col
        else:
            # Turn right
            direction_index = (direction_index + 1) % 4
        
        # Add the current position to visited positions
        visited_positions.add((row, col))
        last_positions.append((row, col))
        
        # Check if the guard has exited the map
        if not (0 <= row < len(grid) and 0 <= col < len(grid[row])):
            break
        
        # Check for loops
        if len(last_positions) > 100:  # Arbitrary large number to detect loops
            if last_positions[-1] in last_positions[:-1]:
                return True  # Loop detected
    
    return False

# Function to find all positions where placing an obstruction causes a loop
def find_obstruction_positions(grid):
    obstruction_positions = []
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                # Check if placing an obstruction at (i, j) causes a loop
                if simulate_guard_movement_with_obstruction(grid, (i, j)):
                    obstruction_positions.append((i, j))
    
    return obstruction_positions

# Read the map from the file
grid = read_map('input.txt')

# Find all positions where placing an obstruction causes a loop
obstruction_positions = find_obstruction_positions(grid)

# Print the number of valid obstruction positions
print(len(obstruction_positions))