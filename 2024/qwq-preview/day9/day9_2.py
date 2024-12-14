def main():
    import sys
    disk_map = sys.stdin.read().strip()
    
    # Parse disk map
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
        files.append({'id': file_id, 'length': file_length, 'start': current_position})
        current_position += file_length + free_space_length
        file_id += 1
        i += 2
    
    # Create initial disk layout
    max_position = sum(int(c) for c in disk_map if c != '0')
    disk = [''] * max_position
    for file in files:
        for j in range(file['length']):
            disk[file['start'] + j] = str(file['id'])
        file['end'] = file['start'] + file['length'] - 1
        file['blocks'] = [file['start'] + j for j in range(file['length'])]
    
    # Find free spaces
    free_spaces = []
    pos = 0
    while pos < len(disk):
        if disk[pos] == '':
            start = pos
            while pos < len(disk) and disk[pos] == '':
                pos += 1
            free_spaces.append((start, pos - start))
        else:
            pos += 1
    
    # Sort files by ID descending
    files_sorted = sorted(files, key=lambda x: x['id'], reverse=True)
    
    # Move files
    for file in files_sorted:
        # Find leftmost free space that can fit the file
        for fs in free_spaces:
            if fs[1] >= file['length']:
                # Move file to this free space
                for j in range(file['length']):
                    disk[fs[0] + j] = str(file['id'])
                    disk[file['blocks'][j]] = ''
                # Update file blocks
                file['blocks'] = [fs[0] + j for j in range(file['length'])]
                # Update free spaces
                free_spaces.remove(fs)
                new_fs_start = fs[0] + file['length']
                new_fs_end = fs[0] + fs[1]
                if new_fs_start < new_fs_end:
                    free_spaces.append((new_fs_start, new_fs_end - new_fs_start))
                # Merge free spaces if adjacent
                free_spaces = merge_free_spaces(free_spaces)
                break
    
    # Calculate checksum
    checksum = 0
    for pos, block in enumerate(disk):
        if block != '':
            checksum += pos * int(block)
    print(checksum)

def merge_free_spaces(free_spaces):
    free_spaces = sorted(free_spaces, key=lambda x: x[0])
    merged = []
    current_start, current_length = free_spaces[0]
    for fs in free_spaces[1:]:
        if fs[0] == current_start + current_length:
            current_length += fs[1]
        else:
            merged.append((current_start, current_length))
            current_start, current_length = fs
    merged.append((current_start, current_length))
    return merged

if __name__ == "__main__":
    main()