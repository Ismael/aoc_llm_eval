def compact_disk(disk_map):
    files = []
    file_sizes = []
    current_file = 0
    for i, length in enumerate(disk_map):
        if i % 2 == 0:  # File
            length = int(length)
            files.extend([current_file] * length)
            file_sizes.append((current_file, length))
            current_file += 1
        else:  # Free space
            files.extend(['.'] * int(length))
    return files, file_sizes

def move_files_whole(files, file_sizes):
    n = len(files)
    for file_id, size in sorted(file_sizes, key=lambda x: x[0], reverse=True):
        # Find the leftmost span of free space that can fit the file
        start = -1
        count = 0
        for i in range(n):
            if files[i] == '.':
                if start == -1:
                    start = i
                count += 1
                if count == size:
                    break
            else:
                start = -1
                count = 0
        
        if count == size:
            # Move the file
            file_end = next(i for i in range(n-1, -1, -1) if files[i] == file_id) + 1
            files[start:start+size] = [file_id] * size
            files[file_end-size:file_end] = ['.'] * size

    return files

def calculate_checksum(files):
    return sum(i * file_id for i, file_id in enumerate(files) if file_id != '.')

# Read input from file
with open('input.txt', 'r') as file:
    disk_map = file.read().strip()

# Compact the disk
files, file_sizes = compact_disk(disk_map)

# Move files
compacted_files = move_files_whole(files, file_sizes)

# Calculate checksum
checksum = calculate_checksum(compacted_files)

print(f"The resulting filesystem checksum is: {checksum}")
