import itertools

def evaluate_expression(numbers, operators):
    """Evaluate the expression formed by the given numbers and operators."""
    expression = str(numbers[0])
    for i in range(1, len(numbers)):
        if operators[i - 1] == '||':
            expression += str(numbers[i])
        else:
            expression += operators[i - 1] + str(numbers[i])
    return eval(expression)

def can_be_made_true(test_value, numbers):
    """Check if the test value can be obtained by any combination of operators."""
    num_operators = len(numbers) - 1
    operator_combinations = itertools.product(['+', '*', '||'], repeat=num_operators)
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def main():
    total_calibration_result = 0
    with open('input.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            test_value = int(parts[0])
            numbers = list(map(int, parts[1].split()))
            if can_be_made_true(test_value, numbers):
                total_calibration_result += test_value
    print(total_calibration_result)

if __name__ == "__main__":
    main()