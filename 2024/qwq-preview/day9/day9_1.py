def main():
    import sys
    disk_map = sys.stdin.read().strip()
    
    files = []
    file_id = 0
    current_position = 0
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        if file_length == 0:
            i += 2
            continue
        free_space_length = int(disk_map[i+1]) if i+1 < len(disk_map) else 0
        files.append({'id': file_id, 'length': file_length, 'original_positions': list(range(current_position, current_position + file_length))})
        current_position += file_length + free_space_length
        file_id += 1
        i += 2
    
    # Assign compacted positions
    current_position = 0
    for file in files:
        file['compacted_positions'] = list(range(current_position, current_position + file['length']))
        current_position += file['length']
    
    # Calculate checksum
    checksum = 0
    for file in files:
        for pos in file['compacted_positions']:
            checksum += pos * file['id']
    
    print(checksum)

if __name__ == "__main__":
    main()