def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    i = 0
    while i < len(disk_map):
        if i + 1 >= len(disk_map):
            raise ValueError(f"Invalid disk map: index {i} out of range. Disk map: {disk_map}")
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1])
        blocks.extend([file_id] * file_length)
        blocks.extend(['.'] * free_length)
        file_id += 1
        i += 2
    return blocks

def move_files_whole(blocks):
    # Create a dictionary to store the start and end indices of each file
    file_indices = {}
    for i, block in enumerate(blocks):
        if block != '.':
            if block not in file_indices:
                file_indices[block] = {'start': i, 'end': i}
            else:
                file_indices[block]['end'] = i

    # Sort file IDs in descending order
    file_ids = sorted(file_indices.keys(), reverse=True)

    for file_id in file_ids:
        file_start = file_indices[file_id]['start']
        file_end = file_indices[file_id]['end']
        file_length = file_end - file_start + 1

        # Find the leftmost span of free space that can fit the file
        for i in range(len(blocks) - file_length + 1):
            if all(blocks[j] == '.' for j in range(i, i + file_length)):
                # Move the file to the leftmost free space
                for j in range(file_length):
                    blocks[i + j] = file_id
                for j in range(file_start, file_end + 1):
                    blocks[j] = '.'
                break

def calculate_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        if block != '.':
            checksum += i * block
    return checksum

def main():
    with open('input.txt', 'r') as file:
        disk_map = file.readline().strip()
        print(f"Disk map: {disk_map}")

    try:
        blocks = parse_disk_map(disk_map)
        print(f"Initial blocks: {blocks}")
        move_files_whole(blocks)
        print(f"Final blocks: {blocks}")
        checksum = calculate_checksum(blocks)
        print(f"Filesystem checksum: {checksum}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()