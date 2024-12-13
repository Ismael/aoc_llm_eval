import re

def parse_instructions(input_string):
    # Regular expressions to match valid mul, do, and don't instructions
    mul_pattern = r'mul\((\d+),(\d+)\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Initialize the state and total sum
    mul_enabled = True
    total_sum = 0
    
    # Combine all patterns into one to find all instructions in order
    combined_pattern = re.compile(f'({mul_pattern}|{do_pattern}|{dont_pattern})')
    matches = combined_pattern.finditer(input_string)
    
    for match in matches:
        instruction = match.group(0)
        
        if instruction.startswith('mul('):
            # It's a mul instruction
            if mul_enabled:
                # Extract the numbers and compute the product
                x, y = map(int, match.groups())
                total_sum += x * y
        elif instruction == 'do()':
            # Enable future mul instructions
            mul_enabled = True
        elif instruction == "don't()":
            # Disable future mul instructions
            mul_enabled = False
    
    return total_sum

def main():
    # Read the input from the file
    with open('input.txt', 'r') as file:
        input_string = file.read()
    
    # Calculate the sum of all enabled mul instructions
    result = parse_instructions(input_string)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()