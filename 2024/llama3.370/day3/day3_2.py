import re

def calculate_multiplications(input_str):
    """
    Scan the corrupted memory for uncorrupted mul instructions and calculate the sum of their results.
    Also handle do() and don't() instructions to determine which mul instructions are enabled.

    Args:
    input_str (str): The corrupted memory string.

    Returns:
    int: The sum of the results of all enabled multiplications.
    """
    # Regular expression patterns to match valid instructions
    mul_pattern = r'mul\(\d{1,3},\d{1,3}\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"

    # Initialize the sum of results and the enable flag
    total = 0
    enabled = True

    # Split the input string into parts to handle instructions in order
    parts = re.split(f'({mul_pattern}|{do_pattern}|{dont_pattern})', input_str)

    # Process each part
    for part in parts:
        # Check if the part is a valid instruction
        if re.fullmatch(mul_pattern, part):
            # If mul instructions are enabled, calculate the result and add it to the total
            if enabled:
                # Extract the operands from the match
                operands = part[4:-1].split(',')
                num1 = int(operands[0])
                num2 = int(operands[1])
                
                # Calculate the result of the multiplication and add it to the total
                total += num1 * num2
        elif re.fullmatch(do_pattern, part):
            # Enable future mul instructions
            enabled = True
        elif re.fullmatch(dont_pattern, part):
            # Disable future mul instructions
            enabled = False

    return total

def main():
    # Read the input from the file
    with open('input.txt', 'r') as file:
        input_str = file.read()

    # Calculate the sum of the results of all enabled multiplications
    result = calculate_multiplications(input_str)

    print(f"The sum of the results of all enabled multiplications is: {result}")

if __name__ == "__main__":
    main()