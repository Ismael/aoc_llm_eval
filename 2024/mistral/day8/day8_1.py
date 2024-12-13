def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_antennas(grid):
    antennas = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char.isalnum():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    return antennas

def calculate_antinodes(antennas, grid_height, grid_width):
    antinodes = set()

    for frequency, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                # Calculate the midpoint
                mid_r = (r1 + r2) // 2
                mid_c = (c1 + c2) // 2

                # Calculate the antinodes
                antinode1 = (mid_r + (mid_r - r1), mid_c + (mid_c - c1))
                antinode2 = (mid_r - (mid_r - r1), mid_c - (mid_c - c1))

                # Check if antinodes are within bounds
                if 0 <= antinode1[0] < grid_height and 0 <= antinode1[1] < grid_width:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < grid_height and 0 <= antinode2[1] < grid_width:
                    antinodes.add(antinode2)

    return antinodes

def main():
    grid = read_input('input.txt')
    grid_height = len(grid)
    grid_width = len(grid[0])

    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, grid_height, grid_width)

    print(f"Number of unique antinodes: {len(antinodes)}")

if __name__ == "__main__":
    main()
