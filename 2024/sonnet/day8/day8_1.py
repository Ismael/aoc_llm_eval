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
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i+1:]:
                dx, dy = x2 - x1, y2 - y1
                
                # Calculate antinodes on both sides
                for multiplier in [-1, 2]:
                    x = x1 + multiplier * dx
                    y = y1 + multiplier * dy
                    if 0 <= x < width and 0 <= y < height:
                        antinodes.add((x, y))
    
    # Add antenna positions that overlap with antinodes
    for positions in antennas.values():
        for x, y in positions:
            if (x, y) in antinodes:
                antinodes.add((x, y))
    
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
