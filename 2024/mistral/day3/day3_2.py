import re

def sum_of_multiplications(corrupted_memory):
    # Regular expression to match valid mul instructions
    pattern_mul = r'mul\((\d{1,3}),(\d{1,3})\)'
    # Regular expression to match do() and don't() instructions
    pattern_do = r'do\(\)'
    pattern_dont = r'don\'t\(\)'

    # Find all matches in the corrupted memory
    matches_mul = re.finditer(pattern_mul, corrupted_memory)
    matches_do = re.finditer(pattern_do, corrupted_memory)
    matches_dont = re.finditer(pattern_dont, corrupted_memory)

    # Initialize the sum of results and the enabled flag
    total_sum = 0
    enabled = True

    # Combine all matches into a single list with their positions
    all_matches = []
    for match in matches_mul:
        all_matches.append((match.start(), 'mul', match.groups()))
    for match in matches_do:
        all_matches.append((match.start(), 'do', None))
    for match in matches_dont:
        all_matches.append((match.start(), 'dont', None))

    # Sort all matches by their positions
    all_matches.sort(key=lambda x: x[0])

    # Iterate through all matches and compute the multiplication if enabled
    for match in all_matches:
        position, instruction, groups = match
        if instruction == 'do':
            enabled = True
        elif instruction == 'dont':
            enabled = False
        elif instruction == 'mul' and enabled:
            x, y = map(int, groups)
            result = x * y
            total_sum += result

    return total_sum

# Read the corrupted memory from input.txt
with open('input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of all valid multiplications
result = sum_of_multiplications(corrupted_memory)
print(result)
