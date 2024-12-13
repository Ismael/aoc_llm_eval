from itertools import product

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_line(line):
    test_value, numbers = line.split(':')
    test_value = int(test_value.strip())
    numbers = list(map(int, numbers.strip().split()))
    return test_value, numbers

def generate_equations(numbers):
    operators = ['+', '*', '||']
    num_operators = len(numbers) - 1
    for ops in product(operators, repeat=num_operators):
        equation = ''
        for i in range(len(numbers)):
            equation += str(numbers[i])
            if i < num_operators:
                equation += ops[i]
        yield equation

def evaluate_equation(equation):
    try:
        # Replace '||' with string concatenation
        equation = equation.replace('||', '')
        return int(equation)
    except:
        return None

def solve_puzzle(file_path):
    lines = read_input(file_path)
    total_calibration = 0

    for line in lines:
        test_value, numbers = parse_line(line)
        valid = False
        for equation in generate_equations(numbers):
            if evaluate_equation(equation) == test_value:
                valid = True
                break
        if valid:
            total_calibration += test_value

    return total_calibration

# Run the solution
file_path = 'input.txt'
result = solve_puzzle(file_path)
print(f"The total calibration result is: {result}")
