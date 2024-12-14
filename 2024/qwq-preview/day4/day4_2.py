import sys

def main():
    import sys
    grid = [line.strip() for line in sys.stdin.readlines()]
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0
    count = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 'A':
                # Check diagonal: top-left to bottom-right
                if (i - 1 >= 0 and j - 1 >= 0 and i + 1 < num_rows and j + 1 < num_cols):
                    char1 = grid[i - 1][j - 1]
                    char2 = grid[i + 1][j + 1]
                    diagonal_valid = (char1 == 'M' and char2 == 'S') or (char1 == 'S' and char2 == 'M')
                else:
                    diagonal_valid = False

                # Check anti-diagonal: top-right to bottom-left
                if (i - 1 >= 0 and j + 1 < num_cols and i + 1 < num_rows and j - 1 >= 0):
                    char1 = grid[i - 1][j + 1]
                    char2 = grid[i + 1][j - 1]
                    anti_diagonal_valid = (char1 == 'M' and char2 == 'S') or (char1 == 'S' and char2 == 'M')
                else:
                    anti_diagonal_valid = False

                # If both sequences are valid, it's an X-MAS
                if diagonal_valid and anti_diagonal_valid:
                    count += 1

    print(count)

if __name__ == "__main__":
    main()