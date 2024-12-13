import re

def parse_mul_instructions(input_string):
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, input_string)
    
    total_sum = 0
    for match in matches:
        # Convert the matched groups to integers and compute the product
        x, y = map(int, match)
        total_sum += x * y
    
    return total_sum

def main():
    # Read the input from the file
    with open('input.txt', 'r') as file:
        input_string = file.read()
    
    # Calculate the sum of all valid mul instructions
    result = parse_mul_instructions(input_string)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()