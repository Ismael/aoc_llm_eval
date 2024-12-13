from collections import deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(topographic_map):
    trailheads = []
    for r in range(len(topographic_map)):
        for c in range(len(topographic_map[r])):
            if topographic_map[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid(r, c, topographic_map, visited):
    return 0 <= r < len(topographic_map) and 0 <= c < len(topographic_map[0]) and not visited[r][c]

def bfs(start, topographic_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = [[False] * len(topographic_map[0]) for _ in range(len(topographic_map))]
    visited[start[0]][start[1]] = True
    score = 0

    while queue:
        r, c = queue.popleft()
        current_height = topographic_map[r][c]

        if current_height == 9:
            score += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, topographic_map, visited) and topographic_map[nr][nc] == current_height + 1:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return score

def main():
    topographic_map = read_input('input.txt')
    trailheads = find_trailheads(topographic_map)
    total_score = 0

    for trailhead in trailheads:
        score = bfs(trailhead, topographic_map)
        total_score += score

    print(total_score)

if __name__ == "__main__":
    main()
