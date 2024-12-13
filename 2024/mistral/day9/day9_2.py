def parse_input(file_path):
    with open(file_path, 'r') as file:
        disk_map = file.readline().strip()
    return disk_map

def simulate_compaction(disk_map):
    # Convert the disk map into a list of file lengths and free spaces
    files = []
    free_spaces = []
    i = 0
    file_id = 0
    while i < len(disk_map):
        length = int(disk_map[i])
        files.append((file_id, length))
        file_id += 1
        i += 1
        if i < len(disk_map):
            length = int(disk_map[i])
            free_spaces.append(length)
            i += 1

    # Sort files by decreasing file ID
    files.sort(key=lambda x: -x[0])

    # Create a list to represent the disk
    disk = []
    for file_id, length in files:
        disk.extend([file_id] * length)
        if free_spaces:
            disk.extend(['.'] * free_spaces.pop(0))

    # Move files to the leftmost span of free space
    for file_id, length in files:
        # Find the leftmost span of free space that can fit the file
        start_index = -1
        for i in range(len(disk) - length + 1):
            if all(disk[j] == '.' for j in range(i, i + length)):
                start_index = i
                break

        if start_index != -1:
            # Move the file to the found span
            file_indices = [i for i, x in enumerate(disk) if x == file_id]
            for i in range(length):
                disk[start_index + i] = file_id
                disk[file_indices[i]] = '.'

    return disk

def calculate_checksum(compacted_blocks):
    checksum = 0
    for position, file_id in enumerate(compacted_blocks):
        if file_id != '.':
            checksum += position * file_id
    return checksum

def main():
    disk_map = parse_input('input.txt')
    compacted_blocks = simulate_compaction(disk_map)
    checksum = calculate_checksum(compacted_blocks)
    print(f"The resulting filesystem checksum is: {checksum}")

if __name__ == "__main__":
    main()
