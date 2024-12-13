def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    return antennas

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_antinodes(antennas, grid):
    antinodes = set()
    
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Calculate the differences
                dx = x2 - x1
                dy = y2 - y1
                
                # Get the greatest common divisor
                g = gcd(dx, dy)
                
                # Calculate the step values
                sx = dx // g
                sy = dy // g
                
                # Add all points on the line between (x1, y1) and (x2, y2)
                x, y = x1, y1
                while (x, y) != (x2, y2):
                    antinodes.add((x, y))
                    x += sx
                    y += sy
                antinodes.add((x2, y2))
    
    return antinodes

def count_unique_antinodes(grid):
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, grid)
    return len(antinodes)

# Read the map from the input file
grid = read_map('input.txt')

# Count the number of unique antinodes
unique_antinodes_count = count_unique_antinodes(grid)
print(unique_antinodes_count)