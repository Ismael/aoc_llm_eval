def find_xmas(grid):
    """Finds all occurrences of "XMAS" in a grid.

    Args:
      grid: A list of strings representing the word search grid.

    Returns:
      The number of times "XMAS" appears in the grid.
    """

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def check_word(r, c, dr, dc):
      """Checks if "XMAS" exists in the given direction.
      
      Args:
        r: Starting row index
        c: Starting column index
        dr: Change in row per character
        dc: Change in column per character

      Returns:
        True if "XMAS" is found, False otherwise
      """
      word = ""
      for i in range(4):
        row = r + i * dr
        col = c + i * dc
        if 0 <= row < rows and 0 <= col < cols:
          word += grid[row][col]
        else:
          return False
      return word == "XMAS"

    for r in range(rows):
        for c in range(cols):
            # Check all 8 directions
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue # skip no change
                    if check_word(r, c, dr, dc):
                        count +=1
    return count


if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            grid = [line.strip() for line in file]

        xmas_count = find_xmas(grid)
        print(f"XMAS appears {xmas_count} times.")

    except FileNotFoundError:
        print("Error: input.txt not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
