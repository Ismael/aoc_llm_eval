import re
import sys

def main():
    # Define the regex pattern for matching mul instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Initialize sum
    total = 0
    
    # Read all lines from stdin and concatenate them into one string
    data = ''.join(sys.stdin.readlines())
    
    # Find all matches of the pattern in the data
    matches = re.findall(pattern, data)
    
    # Process each match
    for match in matches:
        # Extract X and Y from the match
        x = int(match[0])
        y = int(match[1])
        
        # Calculate the product
        product = x * y
        
        # Add the product to the total sum
        total += product
    
    # Print the total sum
    print(total)

if __name__ == "__main__":
    main()