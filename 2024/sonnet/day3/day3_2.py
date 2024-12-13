import re

def parse_mul_instructions(text):
    # Regular expressions to match valid instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Find all matches
    mul_matches = list(re.finditer(mul_pattern, text))
    do_matches = list(re.finditer(do_pattern, text))
    dont_matches = list(re.finditer(dont_pattern, text))
    
    # Combine and sort all matches by their start position
    all_matches = sorted(mul_matches + do_matches + dont_matches, key=lambda x: x.start())
    
    total = 0
    enabled = True  # mul instructions are initially enabled
    
    for match in all_matches:
        if match.re.pattern == mul_pattern and enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            result = x * y
            total += result
        elif match.re.pattern == do_pattern:
            enabled = True
        elif match.re.pattern == dont_pattern:
            enabled = False
    
    return total

# Read the input from the file
with open('input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of all enabled multiplication results
sum_of_results = parse_mul_instructions(corrupted_memory)

print(f"The sum of all enabled multiplication results is: {sum_of_results}")
