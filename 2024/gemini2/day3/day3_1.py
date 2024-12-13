import re

def calculate_multiplications(memory):
    """
    Scans the corrupted memory for valid 'mul' instructions and calculates the sum of their results.

    Args:
        memory (str): The corrupted memory containing potential 'mul' instructions.

    Returns:
          int: The sum of the results of all valid multiplications.
    """
    total_sum = 0
    #regex will find mul(firstnum, secondnum) but also handle variations like mul (1, 2), or mul(123,4)
    pattern = re.compile(r"mul\s*$$\s*(\d{1,3})\s*,\s*(\d{1,3})\s*$$")
    
    for match in pattern.finditer(memory):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total_sum += num1 * num2
    return total_sum

if __name__ == "__main__":
    try:
        with open("input.txt", "r") as f:
            memory = f.read().strip()
        result = calculate_multiplications(memory)
        print(f"The sum of all valid mul instructions is: {result}")
    except FileNotFoundError:
        print("Error: input.txt not found. Please create the file with the puzzle input.")
    except Exception as e:
         print(f"An unexpected error occurred: {e}")
