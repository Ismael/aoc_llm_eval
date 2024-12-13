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

def find_free_space(disk_blocks, file_size):
  """Find the leftmost free space that is large enough to fit the file if one is found. Otherwise, return None"""
  
  current_free_size = 0 
  
  
  start_index = -1
  
  for i, block in enumerate(disk_blocks):
    if block == ".":
      if current_free_size == 0:
         start_index = i
      current_free_size +=1
      
      if current_free_size == file_size:
         return start_index
     
    else:
       current_free_size = 0
       start_index = -1
    
    
  return None
    

def compact_disk_by_file(disk_blocks, file_info):
    """Compacts the disk blocks by moving whole files to the left."""
    
    
    
    
    files = []
    for file_id, length in file_info:
      
       if file_id is not None:
          files.append((file_id, length))
    
    
        
    
    for file_id, file_len in sorted(files, key = lambda item: item[0], reverse = True):
        start_index = -1
        
        
        
        
        for i in range(len(disk_blocks)):
          if disk_blocks[i] == file_id:
            start_index = i
            break
          
        
            
        
        if start_index == -1:
          continue
        
        end_index = start_index + file_len -1
        
        
        free_space_index = find_free_space(disk_blocks[:start_index],file_len)
        
        if free_space_index is None:
          continue
          
        
        
        
        
        
        
        
        
        
        for i in range(free_space_index, free_space_index + file_len):
            disk_blocks[i]=file_id
        
        for i in range(start_index, end_index + 1):
           disk_blocks[i] = "."
       
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
compacted_disk = compact_disk_by_file(disk_blocks, file_info)


checksum = calculate_checksum(compacted_disk)


print(f"Filesystem checksum: {checksum}")
