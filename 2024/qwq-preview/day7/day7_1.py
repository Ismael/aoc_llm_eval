import sys
import itertools

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split(':')
        if len(parts) != 2:
            continue
        test_value_str, numbers_str = parts
        test_value = int(test_value_str.strip())
        numbers = list(map(int, numbers_str.split()))
        if len(numbers) < 1:
            continue
        if len(numbers) == 1:
            # Single number case
            if numbers[0] == test_value:
                total += test_value
            continue
        # Generate all possible operator combinations
        operators_combinations = list(itertools.product(['+', '*'], repeat=len(numbers)-1))
        for ops in operators_combinations:
            if evaluate_expression(numbers, ops) == test_value:
                total += test_value
                break  # No need to check further for this equation
    print(total)

if __name__ == "__main__":
    main()