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

def calculate_antinodes(antennas, grid):
    antinodes = set()
    
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Check if they are aligned horizontally or vertically
                if x1 == x2:  # Vertical alignment
                    dy = y2 - y1
                    if dy % 3 == 0:
                        y3 = y1 + 2 * dy // 3
                        if 0 <= y3 < len(grid):
                            antinodes.add((x1, y3))
                        y4 = y1 + 4 * dy // 3
                        if 0 <= y4 < len(grid):
                            antinodes.add((x1, y4))
                elif y1 == y2:  # Horizontal alignment
                    dx = x2 - x1
                    if dx % 3 == 0:
                        x3 = x1 + 2 * dx // 3
                        if 0 <= x3 < len(grid[0]):
                            antinodes.add((x3, y1))
                        x4 = x1 + 4 * dx // 3
                        if 0 <= x4 < len(grid[0]):
                            antinodes.add((x4, y1))
    
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