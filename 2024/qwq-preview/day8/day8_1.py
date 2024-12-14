import sys
from itertools import combinations

def main():
    import sys
    map_data = sys.stdin.read().splitlines()
    
    # Remove empty lines and trim lines
    map_data = [line.strip() for line in map_data if line.strip()]
    
    # Determine the number of rows and columns
    num_rows = len(map_data)
    num_cols = max(len(row) for row in map_data)
    
    # Parse positions of antennas
    antennas = {}
    for row in range(num_rows):
        for col in range(num_cols):
            if col < len(map_data[row]) and map_data[row][col] != '.':
                freq = map_data[row][col]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((col, row))
    
    # Function to calculate antinode positions for a pair of positions
    def get_antinode_positions(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        dx = x2 - x1
        dy = y2 - y1
        positions = []
        # t = 2
        x = 2 * x2 - x1
        y = 2 * y2 - y1
        positions.append((x, y))
        # t = 2/3
        if (x1 + 2 * x2) % 3 == 0 and (y1 + 2 * y2) % 3 == 0:
            x = (x1 + 2 * x2) // 3
            y = (y1 + 2 * y2) // 3
            positions.append((x, y))
        # t = 1/3
        if (2 * x1 + x2) % 3 == 0 and (2 * y1 + y2) % 3 == 0:
            x = (2 * x1 + x2) // 3
            y = (2 * y1 + y2) // 3
            positions.append((x, y))
        # t = -1
        x = 2 * x1 - x2
        y = 2 * y1 - y2
        positions.append((x, y))
        return positions
    
    # Function to check if a position is within bounds
    def is_within_bounds(x, y):
        return 0 <= x < num_cols and 0 <= y < num_rows
    
    # Collect all unique antinode positions
    antinode_set = set()
    for freq, positions in antennas.items():
        for pos1, pos2 in combinations(positions, 2):
            for antinode in get_antinode_positions(pos1, pos2):
                x, y = antinode
                if is_within_bounds(x, y):
                    antinode_set.add((x, y))
    
    # Count the number of unique antinode positions
    print(len(antinode_set))

if __name__ == "__main__":
    main()