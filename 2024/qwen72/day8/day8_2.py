def read_input(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_antennas(grid):
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                if grid[y][x] not in antennas:
                    antennas[grid[y][x]] = []
                antennas[grid[y][x]].append((x, y))
    return antennas

def calculate_antinodes(antennas, grid_width, grid_height):
    antinodes = set()
    for frequency, positions in antennas.items():
        if len(positions) < 2:
            continue
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx = x2 - x1
                dy = y2 - y1
                gcd = abs(dx) if dx != 0 else abs(dy)
                if dx != 0:
                    gcd = abs(dx)
                if dy != 0:
                    gcd = abs(dy)
                if dx != 0 and dy != 0:
                    gcd = abs(dx) if abs(dx) < abs(dy) else abs(dy)
                step_x = dx // gcd
                step_y = dy // gcd
                x, y = x1, y1
                while (x, y) != (x2, y2):
                    if 0 <= x < grid_width and 0 <= y < grid_height:
                        antinodes.add((x, y))
                    x += step_x
                    y += step_y
                if 0 <= x2 < grid_width and 0 <= y2 < grid_height:
                    antinodes.add((x2, y2))
    return antinodes

def count_antinodes(antinodes):
    return len(antinodes)

def main():
    grid = read_input('input.txt')
    grid_height = len(grid)
    grid_width = len(grid[0])
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, grid_width, grid_height)
    unique_antinodes_count = count_antinodes(antinodes)
    print(f"Number of unique antinode locations: {unique_antinodes_count}")

if __name__ == "__main__":
    main()