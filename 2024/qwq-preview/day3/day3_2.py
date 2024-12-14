import re
import sys

def main():
    # Define the regex patterns for matching mul, do(), and don't() instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    total = 0
    enabled = True  # Start with mul instructions enabled
    
    data = ''.join(sys.stdin.readlines())
    
    # Find all instructions (mul, do, don't) and sort them by their start position
    mul_matches = [(m.start(), 'mul', m.group(1), m.group(2)) for m in re.finditer(mul_pattern, data)]
    do_matches = [(m.start(), 'do') for m in re.finditer(do_pattern, data)]
    dont_matches = [(m.start(), "dont") for m in re.finditer(dont_pattern, data)]
    
    # Combine and sort all matches by their start position
    all_matches = sorted(mul_matches + do_matches + dont_matches, key=lambda x: x[0])
    
    for match in all_matches:
        if match[1] == 'mul':
            if enabled:
                x = int(match[2])
                y = int(match[3])
                product = x * y
                total += product
        elif match[1] == 'do':
            enabled = True
        elif match[1] == "dont":
            enabled = False
    
    print(total)

if __name__ == "__main__":
    main()