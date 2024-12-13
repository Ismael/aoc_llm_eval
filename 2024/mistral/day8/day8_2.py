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

                # Calculate the direction vector
                dr = r2 - r1
                dc = c2 - c1

                # Normalize the direction vector to unit steps
                gcd = abs(dr) if dc == 0 else abs(dc) if dr == 0 else abs(gcd(dr, dc))
                dr //= gcd
                dc //= gcd

                # Mark all points on the line
                r, c = r1, c1
                while 0 <= r < grid_height and 0 <= c < grid_width:
                    antinodes.add((r, c))
                    r += dr
                    c += dc

                # Mark the endpoint
                antinodes.add((r2, c2))

    return antinodes

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    grid = read_input('input.txt')
    grid_height = len(grid)
    grid_width = len(grid[0])

    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, grid_height, grid_width)

    print(f"Number of unique antinodes: {len(antinodes)}")

if __name__ == "__main__":
    main()
