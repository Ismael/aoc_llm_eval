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

def move_files(blocks):
    while True:
        # Find the last file block
        last_file_index = None
        for i in range(len(blocks) - 1, -1, -1):
            if blocks[i] != '.':
                last_file_index = i
                break
        if last_file_index is None:
            break

        # Find the leftmost free space
        leftmost_free_index = None
        for i in range(len(blocks)):
            if blocks[i] == '.':
                leftmost_free_index = i
                break
        if leftmost_free_index is None:
            break

        # Move the file block to the leftmost free space
        file_id = blocks[last_file_index]
        blocks[last_file_index] = '.'
        blocks[leftmost_free_index] = file_id

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
        move_files(blocks)
        print(f"Final blocks: {blocks}")
        checksum = calculate_checksum(blocks)
        print(f"Filesystem checksum: {checksum}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()