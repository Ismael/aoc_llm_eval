def count_xmas_x(grid):
    orientations = [
        [(0, 0), (1, -1), (2, 0)],  # Forward and Backward
        [(0, 0), (1, 1), (2, 0)],   # Forward and Forward
        [(0, 0), (1, 1), (2, -1)],  # Backward and Forward
        [(0, 0), (1, -1), (2, -1)]  # Backward and Backward
    ]
    
    word = "MAS"
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            for orientation in orientations:
                # Check if the orientation fits within the grid
                valid = True
                for dr, dc in orientation:
                    if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                        valid = False
                        break
                if not valid:
                    continue
                
                # Check the orientation
                valid_orientation = True
                for i, (dr, dc) in enumerate(orientation):
                    if grid[r + dr][c + dc] != word[i]:
                        valid_orientation = False
                        break
                
                if valid_orientation:
                    count += 1
    
    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid

if __name__ == "__main__":
    filename = 'input.txt'
    grid = read_grid_from_file(filename)
    result = count_xmas_x(grid)
    print(f"The X-MAS pattern appears {result} times in the word search.")