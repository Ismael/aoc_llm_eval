def solve():
    with open("input.txt", "r") as f:
        heightmap = [list(map(int, line.strip())) for line in f]

    rows = len(heightmap)
    cols = len(heightmap[0])

    total_score = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def find_paths(start_r, start_c):
        paths = 0
        queue = [(start_r, start_c, 0)]

        while queue:
            r, c, current_height = queue.pop(0)


            if heightmap[r][c] == 9:
                paths += 1
                continue

            # Check neighbors
            neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in neighbors:
                if is_valid(nr, nc) and heightmap[nr][nc] == current_height + 1:
                    queue.append((nr,nc, current_height + 1))
            
        return paths

    for r in range(rows):
        for c in range(cols):
            if heightmap[r][c] == 0:
                total_score += find_paths(r, c)

    print(total_score)

solve()
