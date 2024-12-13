def compact_disk(disk_map):
    files = []
    current_file = 0
    for i, length in enumerate(disk_map):
        if i % 2 == 0:  # File
            files.extend([current_file] * int(length))
            current_file += 1
        else:  # Free space
            files.extend(['.'] * int(length))
    return files

def move_files(files):
    n = len(files)
    for i in range(n - 1, -1, -1):
        if files[i] != '.':
            for j in range(i):
                if files[j] == '.':
                    files[j], files[i] = files[i], files[j]
                    break
    return files

def calculate_checksum(files):
    return sum(i * file_id for i, file_id in enumerate(files) if file_id != '.')

# Read input from file
with open('input.txt', 'r') as file:
    disk_map = file.read().strip()

# Compact the disk
files = compact_disk(disk_map)

# Move files
compacted_files = move_files(files)

# Calculate checksum
checksum = calculate_checksum(compacted_files)

print(f"The resulting filesystem checksum is: {checksum}")
