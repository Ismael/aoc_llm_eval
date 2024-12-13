def calculate_distance(left_list, right_list):
    """
    Calculate the total distance between two lists of numbers.

    Args:
        left_list (list): The left list of numbers.
        right_list (list): The right list of numbers.

    Returns:
        int: The total distance between the two lists.
    """
    # Sort both lists in ascending order
    left_list.sort()
    right_list.sort()

    # Initialize the total distance to 0
    total_distance = 0

    # Pair up the numbers from the left and right lists
    for left_num, right_num in zip(left_list, right_list):
        # Calculate the distance between the current pair of numbers
        distance = abs(left_num - right_num)
        # Add the distance to the total distance
        total_distance += distance

    return total_distance


def read_input_file(filename):
    """
    Read the input from a file and split it into two lists.

    Args:
        filename (str): The name of the input file.

    Returns:
        tuple: A tuple containing the left and right lists of numbers.
    """
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            # Split each line into two numbers
            left_num, right_num = map(int, line.split())
            # Add the numbers to their respective lists
            left_list.append(left_num)
            right_list.append(right_num)

    return left_list, right_list


def main():
    # Read the input from the file
    left_list, right_list = read_input_file('input.txt')

    # Calculate the total distance between the two lists
    total_distance = calculate_distance(left_list, right_list)

    # Print the result
    print("The total distance between the two lists is:", total_distance)


if __name__ == "__main__":
    main()