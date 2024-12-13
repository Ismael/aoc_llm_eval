def parse_disk_map(disk_map_str):
    """Parses the disk map string into a list of (file_id, length) tuples."""
    
    file_info = []
    file_id = 0
    i = 0
    
    while i < len(disk_map_str):
        file_len = int(disk_map_str[i])
        i+=1
        
        file_info.append((file_id, file_len))
        file_id+=1
    
        
        if i < len(disk_map_str):
            free_len = int(disk_map_str[i])
            i+=1
            file_info.append((None, free_len))
            
    return file_info


def create_disk_blocks(file_info):
    """Creates a list of disk blocks."""
    disk_blocks = []
    for file_id, length in file_info:
        if file_id is not None:
             disk_blocks.extend([file_id] * length)
        else:
          disk_blocks.extend(["."] * length)
    return disk_blocks
  

def compact_disk(disk_blocks):
    """Compacts the disk blocks by moving file blocks to the left."""
    
    
    
    
    num_files = sum(1 for file_id, _ in parse_disk_map(disk_map_str) if file_id is not None)
    file_blocks = []
    for f in disk_blocks:
      if f != ".":
        file_blocks.append(f)
    
    
    num_blocks = len(disk_blocks)
    
    
    
    
    
    
    
    first_free = -1
    
    
    
    
    
    for i in range(-1, len(disk_blocks)):
          
      
        if disk_blocks[i] == ".":
          first_free = i
          break
      
    
    i = len(disk_blocks) -1
    while i>=0:
      if first_free == -1:
        break
      
      if disk_blocks[i] != ".":
         
        disk_blocks[first_free]= disk_blocks[i]
        disk_blocks[i] = "."
        
        first_free= -1
        for j in range(len(disk_blocks)):
          if disk_blocks[j] == ".":
           
           first_free=j
           break
      i-=1
    
    
    
    

    

    return disk_blocks

def calculate_checksum(disk_blocks):
    """Calculates the filesystem checksum."""
    checksum = 0
    
    for i, block in enumerate(disk_blocks):
        if block != ".":
            checksum += i * block
    return checksum



with open('input.txt', 'r') as f:
    disk_map_str = f.readline().strip()


file_info = parse_disk_map(disk_map_str)
disk_blocks = create_disk_blocks(file_info)


compacted_disk = compact_disk(disk_blocks)



checksum = calculate_checksum(compacted_disk)


print(f"Filesystem checksum: {checksum}")
