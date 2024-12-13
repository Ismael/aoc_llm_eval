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

def simulate_guard(grid):
    x, y, direction = find_start(grid)
    visited = set([(x, y)])

    while True:
        next_x, next_y = move(x, y, direction)
        
        if not is_valid(next_x, next_y, grid):
            break
        
        if grid[next_y][next_x] == '#':
            direction = (direction + 1) % 4
        else:
            x, y = next_x, next_y
            visited.add((x, y))

    return len(visited)

# Read input and solve the puzzle
grid = read_input('input.txt')
result = simulate_guard(grid)
print(f"The guard will visit {result} distinct positions before leaving the mapped area.")
