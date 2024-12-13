def find_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(antennas, width, height):
    antinodes = set()
    
    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue  # Skip frequencies with only one antenna
        
        # Check horizontal lines
        for y in range(height):
            x_coords = [x for x, y_pos in positions if y_pos == y]
            if len(x_coords) >= 2:
                antinodes.update((x, y) for x in range(min(x_coords), max(x_coords) + 1))
        
        # Check vertical lines
        for x in range(width):
            y_coords = [y for x_pos, y in positions if x_pos == x]
            if len(y_coords) >= 2:
                antinodes.update((x, y) for y in range(min(y_coords), max(y_coords) + 1))
        
        # Check diagonal lines (top-left to bottom-right)
        for d in range(-height + 1, width):
            diag_coords = [(x, y) for x, y in positions if x - y == d]
            if len(diag_coords) >= 2:
                x_min, y_min = min(diag_coords)
                x_max, y_max = max(diag_coords)
                antinodes.update((x, x - d) for x in range(x_min, x_max + 1) if 0 <= x < width and 0 <= x - d < height)
        
        # Check diagonal lines (top-right to bottom-left)
        for d in range(width + height - 1):
            diag_coords = [(x, y) for x, y in positions if x + y == d]
            if len(diag_coords) >= 2:
                x_min, y_max = min(diag_coords)
                x_max, y_min = max(diag_coords)
                antinodes.update((x, d - x) for x in range(x_min, x_max + 1) if 0 <= x < width and 0 <= d - x < height)
    
    return antinodes

def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file]
    
    width, height = len(grid[0]), len(grid)
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, width, height)
    
    print(f"Number of unique locations containing an antinode: {len(antinodes)}")

if __name__ == "__main__":
    main()
