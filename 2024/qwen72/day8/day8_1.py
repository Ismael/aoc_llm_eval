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

def calculate_antinodes(antennas):
    antinodes = set()
    for frequency, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx = x2 - x1
                dy = y2 - y1
                # Calculate the two antinodes
                antinode1 = (x1 + dx // 2, y1 + dy // 2)
                antinode2 = (x2 + dx // 2, y2 + dy // 2)
                # Check if the antinodes are within the bounds of the grid
                if 0 <= antinode1[0] < len(grid[0]) and 0 <= antinode1[1] < len(grid):
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < len(grid[0]) and 0 <= antinode2[1] < len(grid):
                    antinodes.add(antinode2)
    return antinodes

def count_antinodes(antinodes):
    return len(antinodes)

def main():
    grid = read_input('input.txt')
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas)
    unique_antinodes_count = count_antinodes(antinodes)
    print(f"Number of unique antinode locations: {unique_antinodescount}")

if __name__ == "__main__":
    main()