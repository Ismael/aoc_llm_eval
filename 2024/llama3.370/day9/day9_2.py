def compact_disk(disk_map):
    """
    Compact the disk by moving whole files to the leftmost span of free space blocks.

    Args:
    disk_map (str): The disk map representing the layout of files and free space.

    Returns:
    list: The compacted disk as a list of blocks.
    """
    # Initialize the disk as a list of blocks
    disk = []
    file_id = 0

    # Parse the disk map and create the initial disk
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1])
        disk.extend([file_id] * file_length)
        disk.extend(['.'] * free_length)
        file_id += 1

    # Compact the disk
    for file_id in range(file_id - 1, -1, -1):
        # Find the first occurrence of the file
        try:
            first_occurrence = disk.index(file_id)
        except ValueError:
            # If the file is not found, it's already been moved
            continue

        # Find the last occurrence of the file
        last_occurrence = len(disk) - 1 - disk[::-1].index(file_id)

        # Find the length of the file
        file_length = last_occurrence - first_occurrence + 1

        # Find the leftmost span of free space blocks that could fit the file
        for i in range(len(disk)):
            if disk[i:i + file_length].count('.') == file_length:
                # Move the file to the leftmost span of free space blocks
                disk[i:i + file_length] = disk[first_occurrence:last_occurrence + 1]
                disk[first_occurrence:last_occurrence + 1] = ['.'] * file_length
                break

    return disk

def calculate_checksum(disk):
    """
    Calculate the filesystem checksum.

    Args:
    disk (list): The compacted disk as a list of blocks.

    Returns:
    int: The filesystem checksum.
    """
    checksum = 0
    for i, block in enumerate(disk):
        if block!= '.':
            checksum += i * block
    return checksum

def main():
    # Read the puzzle input from a file
    with open('input.txt', 'r') as f:
        disk_map = f.read().strip()

    # Compact the disk and calculate the checksum
    compacted_disk = compact_disk(disk_map)
    checksum = calculate_checksum(compacted_disk)

    print(f"The resulting filesystem checksum is: {checksum}")

if __name__ == "__main__":
    main()