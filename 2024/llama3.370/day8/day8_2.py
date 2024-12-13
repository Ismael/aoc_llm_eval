def calculate_antinodes(grid):
    """
    Calculate the locations of the antinodes in the grid.

    Args:
        grid (list of lists): A 2D grid representing the map of antennas.

    Returns:
        set: A set of unique locations that contain an antinode.
    """
    antinodes = set()

    # Iterate over each frequency (character) in the grid
    for frequency in set(''.join([''.join(row) for row in grid])):
        # Find all locations of the frequency in the grid
        locations = [(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == frequency]

        # If there is only one location with this frequency, skip it
        if len(locations) < 2:
            continue

        # Iterate over each location
        for x, y in locations:
            # Check all four directions (up, down, left, right)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                count = 0
                nx, ny = x + dx, y + dy
                while 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    if grid[ny][nx] == frequency:
                        count += 1
                    nx += dx
                    ny += dy
                if count > 0:
                    antinodes.add((x, y))
                    break

            # Also check if this location is an antinode because it's on the same horizontal or vertical line as two other antennas
            for other_x, other_y in locations:
                if (x, y) == (other_x, other_y):
                    continue
                if x == other_x:
                    for o_x, o_y in locations:
                        if (x, y)!= (o_x, o_y) and (other_x, other_y)!= (o_x, o_y) and x == o_x:
                            antinodes.add((x, y))
                            break
                elif y == other_y:
                    for o_x, o_y in locations:
                        if (x, y)!= (o_x, o_y) and (other_x, other_y)!= (o_x, o_y) and y == o_y:
                            antinodes.add((x, y))
                            break

    return antinodes


def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    antinodes = calculate_antinodes(grid)
    print(f"Number of unique locations with an antinode: {len(antinodes)}")


if __name__ == "__main__":
    main()