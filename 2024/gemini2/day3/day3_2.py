import re

def calculate_conditional_multiplications(memory):
    """
    Scans corrupted memory for valid 'mul', 'do', and 'don't' instructions.
    Calculates the sum of enabled 'mul' operation results based on conditionals.

    Args:
        memory (str): Corrupted memory with `mul`, `do`, and `don't` instructions.

    Returns:
        int: The sum of results from activated multiplications.
    """
    total_sum = 0
    enabled = True
    pattern = re.compile(r"mul\s*$$\s*(\d{1,3})\s*,\s*(\d{1,3})\s*$$|do\s*$$\s*$$|don't\s*$$\s*$$")
   

    for match in pattern.finditer(memory):
        instruction = match.group(0)
        if instruction.startswith("mul"):
            if enabled:
                num1 = int(match.group(1))
                num2 = int(match.group(2))
                total_sum += num1 * num2
        elif instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False

    return total_sum
    

if __name__ == "__main__":
    try:
        with open("input.txt", "r") as f:
            memory = f.read().strip()
        result = calculate_conditional_multiplications(memory)
        print(f"The sum of all enabled mul instructions is: {result}")
        
    except FileNotFoundError:
        print("Error: input.txt not found. Please create the file with the puzzle input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
