import re

def parse_mul_instructions(text):
    # Regular expression to match valid mul instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches
    matches = re.finditer(pattern, text)
    
    total = 0
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        result = x * y
        total += result
    
    return total

# Read the input from the file
with open('input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of all multiplication results
sum_of_results = parse_mul_instructions(corrupted_memory)

print(f"The sum of all multiplication results is: {sum_of_results}")
