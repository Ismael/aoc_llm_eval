def solve():
    with open("input.txt", "r") as file:
        grid = [list(line.strip()) for line in file]
    
    rows = len(grid)
    cols = len(grid[0])

    # Find initial guard position and direction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "^v<>":
                guard_start_r, guard_start_c = r, c
                direction = grid[r][c]
                grid[r][c] = '.'
                break
        else:
            continue
        break
    
    directions = "^>v<"
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    loop_positions = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) == (guard_start_r, guard_start_c):
                continue
            
            # Temporary grid with added obstacle
            temp_grid = [row[:] for row in grid]
            temp_grid[r][c] = "#"
            
            guard_r, guard_c = guard_start_r, guard_start_c
            current_direction = direction
            
            visited = set([(guard_r, guard_c, current_direction)])
            
            looped = False
            steps = 0
            max_steps = rows*cols*5
            
            while steps < max_steps:
                 # Get current direction index
                current_dir_index = directions.index(current_direction)
                
                # Check if forward move is valid
                next_r = guard_r + dr[current_dir_index]
                next_c = guard_c + dc[current_dir_index]
                
                if 0 <= next_r < rows and 0 <= next_c < cols and temp_grid[next_r][next_c] != '#':
                
                    # Valid forward move, move guard
                    guard_r = next_r
                    guard_c = next_c
                   
                    
                else:
                    #Obstacle, turn right
                    current_dir_index = (current_dir_index + 1) % 4
                    current_direction = directions[current_dir_index]
            
                if (guard_r, guard_c, current_direction) in visited:
                    looped = True
                    break
                
                visited.add((guard_r, guard_c, current_direction))
                steps += 1
            
            if looped:
                loop_positions.add((r, c))
    print(len(loop_positions))


solve()
