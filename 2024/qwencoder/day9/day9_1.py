def parse_disk_map(disk_map_str):
    """Parse the disk map string into a list of file and free space lengths."""
    return [int(x) for x in disk_map_str]

def compact_files(disk_map):
    """Compact the files in the disk map."""
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
    
    # Compact the files
    compact_map = compact_files(disk_map)
    
    # Calculate the checksum
    checksum = calculate_checksum(compact_map)
    
    print(f"The resulting filesystem checksum is: {checksum}")

if __name__ == "__main__":
    main()