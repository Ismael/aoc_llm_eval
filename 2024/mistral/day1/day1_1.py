def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    return total_distance

def main():
    left_list, right_list = read_input('input.txt')
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"The total distance between the lists is: {total_distance}")

if __name__ == "__main__":
    main()
