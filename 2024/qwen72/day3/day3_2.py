import re

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def find_mul_instructions(memory):
    # Regular expression to find valid mul instructions
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, memory)
    return matches

def handle_conditions(memory, matches):
    enabled = True
    results = []
    
    # Regular expression to find do() and don't() instructions
    condition_pattern = re.compile(r'do\(\)|don\'t\(\)')
    condition_matches = condition_pattern.finditer(memory)
    
    # Initialize the positions of the next condition and the next mul
    next_condition = None
    next_mul = 0
    
    for match in matches:
        mul_start = memory.find(f'mul({match[0]},{match[1]})', next_mul)
        
        # Find the next condition after the current mul
        for condition in condition_matches:
            if condition.start() > mul_start:
                next_condition = condition
                break
        
        # Check the state of the enabled flag
        if enabled:
            x, y = map(int, match)
            results.append(x * y)
        
        # Update the enabled flag based on the next condition
        if next_condition and next_condition.start() > mul_start:
            if next_condition.group() == 'do()':
                enabled = True
            else:
                enabled = False
        
        # Update the position for the next mul
        next_mul = mul_start + len(f'mul({match[0]},{match[1]})')
    
    return results

def compute_sum_of_multiplications(results):
    return sum(results)

def main():
    # Read the input from the file
    memory = parse_input('input.txt')
    
    # Find all valid mul instructions
    matches = find_mul_instructions(memory)
    
    # Handle the conditions and compute the results of the enabled multiplications
    results = handle_conditions(memory, matches)
    
    # Compute the sum of the results of the enabled multiplications
    result = compute_sum_of_multiplications(results)
    
    print(f"The sum of the results of the enabled multiplications is: {result}")

if __name__ == "__main__":
    main()