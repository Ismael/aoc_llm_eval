def read_lists_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        left_list = list(map(int, lines[0].strip().split()))
        right_list = list(map(int, lines[1].strip().split()))
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    return total_distance

def main():
    filename = 'input.txt'
    left_list, right_list = read_lists_from_file(filename)
    print(left_list, right_list)
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"The total distance between the lists is: {total_distance}")

if __name__ == "__main__":
    main()