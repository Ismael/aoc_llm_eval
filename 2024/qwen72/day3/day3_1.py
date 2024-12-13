import re

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_mul_instructions(memory):
    # Regular expression to find valid mul instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, memory)
    return matches

def compute_sum_of_multiplications(matches):
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    return total

def main():
    # Read the input from the file
    memory = parse_input('input.txt')
    
    # Find all valid mul instructions
    matches = find_mul_instructions(memory)
    
    # Compute the sum of the results of the multiplications
    result = compute_sum_of_multiplications(matches)
    
    print(f"The sum of the results of the multiplications is: {result}")

if __name__ == "__main__":
    main()