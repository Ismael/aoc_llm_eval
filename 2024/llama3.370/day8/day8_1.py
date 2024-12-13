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

        # Iterate over each pair of locations
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                # Calculate the midpoint between the two locations
                mid_x = (x1 + x2) // 2
                mid_y = (y1 + y2) // 2

                # Check if the midpoint is an antinode
                if (x1 - x2) * (y1 - y2) == 0:  # Check if the two locations are in the same row or column
                    # Calculate the locations of the antinodes
                    antinode1_x = x1 + (x2 - x1) * 2
                    antinode1_y = y1 + (y2 - y1) * 2
                    antinode2_x = x2 + (x1 - x2) * 2
                    antinode2_y = y2 + (y1 - y2) * 2

                    # Check if the antinodes are within the bounds of the grid
                    if (0 <= antinode1_x < len(grid[0]) and 0 <= antinode1_y < len(grid)):
                        antinodes.add((antinode1_x, antinode1_y))
                    if (0 <= antinode2_x < len(grid[0]) and 0 <= antinode2_y < len(grid)):
                        antinodes.add((antinode2_x, antinode2_y))

    return antinodes


def main():
    with open('input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    antinodes = calculate_antinodes(grid)
    print(f"Number of unique locations with an antinode: {len(antinodes)}")


if __name__ == "__main__":
    main()