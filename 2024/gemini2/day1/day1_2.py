def calculate_similarity_score(left_list, right_list):
    """Calculates the similarity score between two lists of numbers.

    Args:
        left_list: A list of integers.
        right_list: A list of integers.

    Returns:
        The total similarity score.
    """
    similarity_score = 0
    for num in left_list:
        count = right_list.count(num)
        similarity_score += num * count
    return similarity_score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score between the lists is: {similarity_score}")
