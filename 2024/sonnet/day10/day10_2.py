def read_map(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(topo_map):
    return [(i, j) for i in range(len(topo_map)) for j in range(len(topo_map[0])) if topo_map[i][j] == 0]

def calculate_rating(topo_map, start):
    rows, cols = len(topo_map), len(topo_map[0])
    paths = [[0 for _ in range(cols)] for _ in range(rows)]
    paths[start[0]][start[1]] = 1

    for height in range(1, 10):
        new_paths = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if topo_map[i][j] == height:
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols and topo_map[ni][nj] == height - 1:
                            new_paths[i][j] += paths[ni][nj]
        paths = new_paths

    return sum(sum(row) for row in paths)

def solve_puzzle(topo_map):
    trailheads = find_trailheads(topo_map)
    return sum(calculate_rating(topo_map, trailhead) for trailhead in trailheads)

# Main execution
topo_map = read_map('input.txt')
result = solve_puzzle(topo_map)
print(f"The sum of the ratings of all trailheads is: {result}")
