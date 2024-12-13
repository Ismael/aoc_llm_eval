def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    equations = []
    for line in lines:
        test_value, numbers_str = line.strip().split(':')
        test_value = int(test_value)
        numbers = list(map(int, numbers_str.split()))
        equations.append((test_value, numbers))
    return equations

def generate_combinations(numbers):
    from itertools import product
    n = len(numbers) - 1
    operators = ['+', '*']
    for ops in product(operators, repeat=n):
        yield ops

def evaluate_expression(numbers, operators):
    expression = str(numbers[0])
    for i in range(len(operators)):
        expression += f" {operators[i]} {numbers[i + 1]}"
    return eval(expression)

def can_be_true(test_value, numbers):
    for ops in generate_combinations(numbers):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def total_calibration_result(equations):
    total = 0
    for test_value, numbers in equations:
        if can_be_true(test_value, numbers):
            total += test_value
    return total

if __name__ == "__main__":
    equations = read_input('input.txt')
    result = total_calibration_result(equations)
    print(f"The total calibration result is: {result}")