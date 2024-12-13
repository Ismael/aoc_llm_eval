def parse_disk_map(disk_map_str):
    """Parse the disk map string into a list of file and free space lengths."""
    return [int(x) for x in disk_map_str]

def construct_disk_map(disk_map):
    """Construct the initial disk map with file blocks and free spaces."""
    n = len(disk_map)
    file_id = 0
    position = 0
    result = ['.'] * sum(disk_map)
    
    for i in range(0, n, 2):
        file_length = disk_map[i]
        free_length = disk_map[i + 1] if i + 1 < n else 0
        
        # Place the file blocks
        for _ in range(file_length):
            result[position] = str(file_id)
            position += 1
        
        # Skip the free space
        position += free_length
        
        file_id += 1
    
    return result

def find_leftmost_free_space(compact_map, file_length):
    """Find the leftmost span of free space that can fit the file."""
    n = len(compact_map)
    for start in range(n):
        if all(compact_map[start:start + file_length] == ['.'] * file_length):
            return start
    return -1

def move_files(compact_map, disk_map):
    """Move files to the leftmost available span of free space."""
    n = len(disk_map)
    file_id = (n // 2) - 1  # Start with the highest file ID
    
    for i in range(0, n, 2):
        file_length = disk_map[i]
        free_length = disk_map[i + 1] if i + 1 < n else 0
        
        # Find the leftmost free space that can fit the file
        start = find_leftmost_free_space(compact_map, file_length)
        
        if start != -1:
            # Move the file to the leftmost free space
            for j in range(file_length):
                compact_map[start + j] = str(file_id)
            
            # Remove the file from its original position
            original_start = compact_map.index(str(file_id))
            for j in range(file_length):
                compact_map[original_start + j] = '.'
        
        file_id -= 1
    
    return compact_map

def calculate_checksum(compact_map):
    """Calculate the filesystem checksum."""
    checksum = 0
    position = 0
    
    for block in compact_map:
        if block != '.':
            checksum += position * int(block)
        position += 1
    
    return checksum

def main():
    # Read the disk map from the input file
    with open('input.txt', 'r') as file:
        disk_map_str = file.readline().strip()
    
    # Parse the disk map
    disk_map = parse_disk_map(disk_map_str)
    
    # Construct the initial disk map
    compact_map = construct_disk_map(disk_map)
    
    # Move files to the leftmost available span of free space
    compact_map = move_files(compact_map, disk_map)
    
    # Calculate the checksum
    checksum = calculate_checksum(compact_map)
    
    print(f"The resulting filesystem checksum is: {checksum}")

if __name__ == "__main__":
    main()