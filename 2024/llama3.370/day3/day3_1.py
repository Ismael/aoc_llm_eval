import re

def calculate_multiplications(input_str):
    """
    Scan the corrupted memory for uncorrupted mul instructions and calculate the sum of their results.

    Args:
    input_str (str): The corrupted memory string.

    Returns:
    int: The sum of the results of all valid multiplications.
    """
    # Regular expression pattern to match valid mul instructions
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    # Find all valid mul instructions
    matches = re.findall(pattern, input_str)
    
    # Initialize the sum of results
    total = 0
    
    # Calculate the result of each valid mul instruction and add it to the total
    for match in matches:
        # Extract the operands from the match
        operands = match[4:-1].split(',')
        num1 = int(operands[0])
        num2 = int(operands[1])
        
        # Calculate the result of the multiplication and add it to the total
        total += num1 * num2
    
    return total

def main():
    # Read the puzzle input from the file
    with open('input.txt', 'r') as file:
        input_str = file.read()
    
    # Calculate the sum of the results of all valid multiplications
    result = calculate_multiplications(input_str)
    
    print(f"The sum of the results of all valid multiplications is: {result}")

if __name__ == "__main__":
    main()