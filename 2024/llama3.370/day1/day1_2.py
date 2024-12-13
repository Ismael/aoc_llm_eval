def calculate_similarity_score(left_list, right_list):
    """
    Calculate the similarity score between two lists of numbers.

    Args:
        left_list (list): The left list of numbers.
        right_list (list): The right list of numbers.

    Returns:
        int: The similarity score between the two lists.
    """
    # Count the occurrences of each number in the right list
    right_counts = {}
    for num in right_list:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1

    # Initialize the similarity score to 0
    similarity_score = 0

    # Calculate the similarity score
    for num in left_list:
        if num in right_counts:
            similarity_score += num * right_counts[num]

    return similarity_score


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

    # Calculate the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)

    # Print the result
    print("The similarity score between the two lists is:", similarity_score)


if __name__ == "__main__":
    main()