import itertools

def evaluate_expression(expression):
    """
    Evaluate an expression from left to right.
    """
    result = expression[0]
    for i in range(1, len(expression), 2):
        operator = expression[i]
        operand = expression[i + 1]
        if operator == '+':
            result += operand
        elif operator == '*':
            result *= operand
        elif operator == '||':
            result = int(str(result) + str(operand))
    return result

def solve_equation(test_value, numbers):
    """
    Try all possible combinations of operators to see if any of them produce the test value.
    """
    operators = ['+', '*', '||']
    for ops in itertools.product(operators, repeat=len(numbers) - 1):
        expression = [numbers[0]]
        for i, op in enumerate(ops):
            expression.append(op)
            expression.append(numbers[i + 1])
        if evaluate_expression(expression) == test_value:
            return True
    return False

def main():
    total_calibration_result = 0
    with open('input.txt', 'r') as f:
        for line in f:
            test_value, _, numbers = line.strip().partition(':')
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            if solve_equation(test_value, numbers):
                total_calibration_result += test_value
    print(total_calibration_result)

if __name__ == "__main__":
    main()