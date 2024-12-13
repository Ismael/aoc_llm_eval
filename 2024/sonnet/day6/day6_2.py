def read_input(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def find_start(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return x, y, 0  # x, y, direction (0: up, 1: right, 2: down, 3: left)

def move(x, y, direction):
    if direction == 0: return x, y - 1
    if direction == 1: return x + 1, y
    if direction == 2: return x, y + 1
    if direction == 3: return x - 1, y

def is_valid(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def simulate_guard(grid, obstruction=None):
    x, y, direction = find_start(grid)
    visited = set([(x, y)])
    path = [(x, y)]

    while True:
        next_x, next_y = move(x, y, direction)
        
        if not is_valid(next_x, next_y, grid):
            return False, len(visited)
        
        if grid[next_y][next_x] == '#' or (next_x, next_y) == obstruction:
            direction = (direction + 1) % 4
        else:
            x, y = next_x, next_y
            if (x, y) in visited:
                return True, len(visited)
            visited.add((x, y))
            path.append((x, y))

    return False, len(visited)

def find_loop_positions(grid):
    loop_positions = []
    start_x, start_y, _ = find_start(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.' and (x, y) != (start_x, start_y):
                is_loop, _ = simulate_guard(grid, obstruction=(x, y))
                if is_loop:
                    loop_positions.append((x, y))

    return loop_positions

# Read input and solve the puzzle
grid = read_input('input.txt')
loop_positions = find_loop_positions(grid)
print(f"There are {len(loop_positions)} different positions where a new obstruction would cause the guard to get stuck in a loop.")
