def calculate_distance(list1, list2):
    list1.sort()
    list2.sort()
    total_distance = 0
    for a, b in zip(list1, list2):
        total_distance += abs(a - b)
    return total_distance

def main():
    import sys
    data = sys.stdin.read()
    lines = data.split('\n')
    list1 = []
    list2 = []
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            continue  # Skip invalid lines
        try:
            num1 = int(parts[0])
            num2 = int(parts[1])
            list1.append(num1)
            list2.append(num2)
        except ValueError:
            print(f"Skipping invalid line: {line}")
    if len(list1) != len(list2):
        print("Error: lists have different lengths!")
        sys.exit(1)
    distance = calculate_distance(list1, list2)
    print(distance)

if __name__ == "__main__":
    main()