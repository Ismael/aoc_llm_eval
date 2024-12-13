def calculate_distance(left_list, right_list):
    """Calculates the total distance between two lists of numbers.

    Args:
        left_list: A list of integers.
        right_list: A list of integers.

    Returns:
        The total distance between the two lists.
    """

    left_list.sort()
    right_list.sort()
    total_distance = 0
    for i in range(len(left_list)):
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
    return total_distance


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    total_distance = calculate_distance(left_list, right_list)
    print(f"The total distance between the lists is: {total_distance}")
