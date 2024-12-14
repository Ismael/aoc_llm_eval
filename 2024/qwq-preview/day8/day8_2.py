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
    
    # Function to generate positions on the line between two positions
    def line_positions(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        positions = []
        if x1 == x2:
            # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                positions.append((x1, y))
        elif y1 == y2:
            # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                positions.append((x, y1))
        elif abs(y2 - y1) == abs(x2 - x1):
            # Diagonal line
            x_step = 1 if x2 > x1 else -1
            y_step = 1 if y2 > y1 else -1
            x, y = x1, y1
            while True:
                positions.append((x, y))
                if x == x2 and y == y2:
                    break
                x += x_step
                y += y_step
        return positions
    
    # Collect all unique antinode positions
    antinode_set = set()
    for freq, positions in antennas.items():
        for pos1, pos2 in combinations(positions, 2):
            positions_on_line = line_positions(pos1, pos2)
            for position in positions_on_line:
                antinode_set.add(position)
    
    # Count the number of unique antinode positions
    print(len(antinode_set))

if __name__ == "__main__":
    main()