def count_xmas(grid):
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (-1, 1), # up-right
        (0, -1), # left
        (-1, 0), # up
        (-1, -1),# up-left
        (1, -1)  # down-left
    ]
    
    word = "XMAS"
    word_length = len(word)
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if r + (word_length - 1) * dr < 0 or r + (word_length - 1) * dr >= rows:
                    continue
                if c + (word_length - 1) * dc < 0 or c + (word_length - 1) * dc >= cols:
                    continue
                
                found = True
                for i in range(word_length):
                    if grid[r + i * dr][c + i * dc] != word[i]:
                        found = False
                        break
                
                if found:
                    count += 1
    
    return count

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]
    return grid

if __name__ == "__main__":
    filename = 'input.txt'
    grid = read_grid_from_file(filename)
    result = count_xmas(grid)
    print(f"The word 'XMAS' appears {result} times in the word search.")