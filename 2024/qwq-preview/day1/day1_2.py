from collections import Counter

def main():
    import sys
    data = sys.stdin.read()
    lines = data.split('\n')
    list1 = []
    list2 = []
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        parts = line.split()
        if len(parts) != 2:
            print(f"Skipping invalid line: {line}")
            continue
        try:
            num1 = int(parts[0])
            num2 = int(parts[1])
            list1.append(num1)
            list2.append(num2)
        except ValueError:
            print(f"Skipping invalid line: {line}")
    # Count frequency of each number in list2
    freq = Counter(list2)
    # Calculate similarity score
    similarity_score = 0
    for num in list1:
        similarity_score += num * freq[num]
    print(similarity_score)

if __name__ == "__main__":
    main()