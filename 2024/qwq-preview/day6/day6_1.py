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
    
    # Set of visited positions
    visited = set()
    visited.add((start_row, start_col))
    
    current_row = start_row
    current_col = start_col
    
    num_rows = len(rows)
    num_cols = len(rows[0])
    
    while True:
        dr, dc = directions[current_dir]
        front_row = current_row + dr
        front_col = current_col + dc
        
        # Check if front position is within bounds
        if 0 <= front_row < num_rows and 0 <= front_col < num_cols:
            front_char = rows[front_row][front_col]
            if front_char == '#':
                # Turn right
                current_dir = (current_dir + 1) % 4
            else:
                # Move forward
                current_row = front_row
                current_col = front_col
                visited.add((current_row, current_col))
        else:
            # Guard has left the area
            break
    
    print(len(visited))

if __name__ == "__main__":
    main()