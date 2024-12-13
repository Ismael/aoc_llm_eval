def find_xmas_x(grid):
    """Finds all occurrences of "X-MAS" in a grid.

    Args:
      grid: A list of strings representing the word search grid.

    Returns:
      The number of times that two "MAS" in an X-shape appear in the grid.
    """

    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_mas(r,c, dr1, dc1, dr2,dc2):
        
        """Checks if "MAS" exists in two intersecting directions
        forming an X.
        
        Args:
            r: Center of X row index
            c: Center of X column index
            dr1: delta row for the first mas
            dc1: delta column for the first mas
            dr2: delta row for the second mas
            dc2: delta column for the second mas
            
        returns:
            True if MAS is found twice in an X-shape, false otherwise
        """
        
        mas1 =""
        mas2 = ""
        
        for i in [-1,0,1]:
           row = r+(i*dr1)
           col = c+(i*dc1)
           if 0<=row<rows and 0 <= col < cols:
            
            mas1+=grid[row][col]
           else:
             return False
        for i in [-1,0,1]:
           row = r+(i*dr2)
           col = c+(i*dc2)
           if 0<=row<rows and 0 <= col < cols:
            
            mas2+=grid[row][col]
           else:
            return False
        
        return (mas1 == "MAS" or mas1 == "SAM") and (mas2=="MAS" or mas2 =="SAM")
            

    for r in range(rows):
        for c in range(cols):
            
            # Check mas in all valid directions to form X
                
            if check_mas(r,c, -1, -1, -1,1):
                count +=1
            elif check_mas(r,c,-1,1, -1, -1):
                 count +=1
            elif check_mas(r,c, -1,1, 1, -1):
                count+=1
            elif check_mas(r,c,1,-1,-1,1):
                count +=1
    
    
    return count//2 # account for double counting


if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            grid = [line.strip() for line in file]

        xmas_count = find_xmas_x(grid)
        print(f"X-MAS appears {xmas_count} times.")

    except FileNotFoundError:
        print("Error: input.txt not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

