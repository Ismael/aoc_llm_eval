import math

def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def find_antennas(grid):
    antennas = {}
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    return antennas

def dist(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def is_valid(r,c,grid):
  return r >=0 and r < len(grid) and c >= 0 and c < len(grid[0])

def calculate_antinodes(grid, antennas):
    antinodes = set()
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
              
                p1 = positions[i]
                p2= positions[j]
                d = dist(p1,p2)
                
                dx= p2[0]-p1[0]
                dy=p2[1]-p1[1]

                
                
                
                ap1x = int(round(p1[0] - dx))
                ap1y = int(round(p1[1] - dy))

                if is_valid(ap1x,ap1y,grid):
                    antinodes.add((ap1x,ap1y))

                
                ap2x = int(round(p2[0] + dx))
                ap2y = int(round(p2[1] + dy))
                

                if is_valid(ap2x,ap2y,grid):
                  antinodes.add((ap2x,ap2y))


    return antinodes

if __name__ == "__main__":
    grid = read_input("input.txt")
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(grid, antennas)
    print(len(antinodes))
