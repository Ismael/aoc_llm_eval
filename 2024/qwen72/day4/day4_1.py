def read_grid(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),  # horizontal and vertical
        (1, 1), (1, -1), (-1, 1), (-1, -1) # diagonal
    ]
    count = 0

    def is_word(r, c, dr, dc):
        for i in range(len(word)):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if is_word(r, c, dr, dc):
                    count += 1

    return count

def main():
    grid = read_grid('input.txt')
    word = "XMAS"
    count = find_word(grid, word)
    print(f"The word '{word}' appears {count} times in the word search.")

if __name__ == "__main__":
    main()