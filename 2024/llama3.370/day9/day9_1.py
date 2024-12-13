def parse_input(file_path):
    with open(file_path, 'r') as file:
        disk_map = file.readline().strip()
    return disk_map

def simulate_compaction(disk_map):
    # Convert the disk map into a list of file lengths and free spaces
    blocks = []
    file_id = 0
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        blocks.extend([file_id] * file_length)
        file_id += 1
        i += 1
        if i < len(disk_map):
            free_length = int(disk_map[i])
            blocks.extend(['.'] * free_length)
            i += 1

    # Compact the blocks
    compacted_blocks = []
    for block in blocks:
        if block == '.':
            continue
        compacted_blocks.append(block)

    return compacted_blocks

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
