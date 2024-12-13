def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    
    return total_distance

def main():
    left_list = []
    right_list = []

    # Read input from file
    with open('input.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    # Calculate and print the total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"The total distance between the lists is: {total_distance}")

if __name__ == "__main__":
    main()
