def main():
    import sys
    map_str = sys.stdin.read().strip()
    rows = map_str.split('\n')
    
    # Define directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Find starting position and direction
    start_row = 0
    start_col = 0
    for i, row in enumerate(rows):
        if '^' in row:
            start_row = i
            start_col = row.index('^')
            current_dir = 0  # Up
            break
        elif '>' in row:
            start_row = i
            start_col = row.index('>')
            current_dir = 1  # Right
            break
        elif 'v' in row:
            start_row = i
            start_col = row.index('v')
            current_dir = 2  # Down
            break
        elif '<' in row:
            start_row = i
            start_col = row.index('<')
            current_dir = 3  # Left
            break
    
    num_rows = len(rows)
    num_cols = len(rows[0])
    
    # Function to simulate guard's movement
    def simulates(map_copy, obstruction_row, obstruction_col):
        visited = set()
        row, col = start_row, start_col
        dir = current_dir
        while True:
            dr, dc = directions[dir]
            front_row = row + dr
            front_col = col + dc
            # Check if front position is within bounds
            if 0 <= front_row < num_rows and 0 <= front_col < num_cols:
                # Add new obstruction
                if front_row == obstruction_row and front_col == obstruction_col:
                    front_char = '#'
                else:
                    front_char = map_copy[front_row][front_col]
                if front_char == '#':
                    # Turn right
                    dir = (dir + 1) % 4
                else:
                    # Move forward
                    row = front_row
                    col = front_col
                    state = (row, col, dir)
                    if state in visited:
                        return True  # Loop detected
                    visited.add(state)
            else:
                # Guard has left the area
                return False
    
    # Find all positions to try placing the obstruction
    candidates = []
    for r in range(num_rows):
        for c in range(num_cols):
            if r != start_row or c != start_col:
                candidates.append((r, c))
    
    count = 0
    for r, c in candidates:
        # Create a copy of the map
        map_copy = [list(row) for row in rows]
        # Place the new obstruction
        map_copy[r] = map_copy[r][:c] + ['#'] + map_copy[r][c+1:]
        # Simulate movement
        if simulates(map_copy, r, c):
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()