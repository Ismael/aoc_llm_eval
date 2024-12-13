def solve():
    with open("input.txt", "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "^>v<":
                start_row = r
                start_col = c
                start_dir = grid[r][c]
                grid[r][c] = "."
                break
        else:
          continue
        break
    
    visited = set()
    current_row = start_row
    current_col = start_col
    current_dir = start_dir
    visited.add((current_row,current_col))
    
    
    def move_forward(row, col, direction):
      if direction == '^':
        return row - 1, col
      elif direction == '>':
        return row, col + 1
      elif direction == 'v':
        return row + 1, col
      elif direction == '<':
        return row, col - 1

    def turn_right(direction):
      if direction == '^':
        return '>'
      elif direction == '>':
        return 'v'
      elif direction == 'v':
        return '<'
      elif direction == '<':
        return '^'

    
    while True:
        next_row, next_col = move_forward(current_row, current_col, current_dir)
        
        if not (0 <= next_row < rows and 0 <= next_col < cols):
           break     

        if grid[next_row][next_col] == '#':
            current_dir = turn_right(current_dir)
        
        else:
          current_row = next_row
          current_col = next_col
          visited.add((current_row, current_col))
    
    
    print(len(visited))


solve()
