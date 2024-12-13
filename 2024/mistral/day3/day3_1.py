import re

def sum_of_multiplications(corrupted_memory):
    # Regular expression to match valid mul instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)

    # Initialize the sum of results
    total_sum = 0

    # Iterate through all matches and compute the multiplication
    for match in matches:
        x, y = map(int, match)
        result = x * y
        total_sum += result

    return total_sum

# Read the corrupted memory from input.txt
with open('input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of all valid multiplications
result = sum_of_multiplications(corrupted_memory)
print(result)
