import itertools
import operator

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        else:  # op == '*'
            result *= numbers[i+1]
    return result

def can_equation_be_true(test_value, numbers):
    for ops in itertools.product([operator.add, operator.mul], repeat=len(numbers)-1):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def solve_puzzle(filename):
    total_calibration = 0
    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            test_value = int(parts[0])
            numbers = list(map(int, parts[1].split()))
            
            if can_equation_be_true(test_value, numbers):
                total_calibration += test_value
    
    return total_calibration

# Solve the puzzle
result = solve_puzzle('input.txt')
print(f"The total calibration result is: {result}")
