def solve():
    with open("input.txt", "r") as f:
        heightmap = [list(map(int, line.strip())) for line in f]

    rows = len(heightmap)
    cols = len(heightmap[0])

    total_rating = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def count_paths(start_r, start_c):
           
      
        queue = [(start_r, start_c, 0, set([(start_r,start_c)]))]
        total_paths = 0
        while queue:
            r, c, current_height, visited = queue.pop(0)

            if heightmap[r][c] == 9:
                total_paths += 1
                continue
               
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighbors:
                 if is_valid(nr, nc) and heightmap[nr][nc] == current_height + 1 and (nr, nc) not in visited:
                  
                    queue.append((nr, nc, current_height + 1, visited.union([(nr, nc)])))
                
        return total_paths



    for r in range(rows):
        for c in range(cols):
            if heightmap[r][c] == 0:
                total_rating += count_paths(r, c)


    print(total_rating)

solve()
