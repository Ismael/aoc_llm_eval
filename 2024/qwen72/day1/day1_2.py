from collections import Counter

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    right_list_counts = Counter(right_list)
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_list_counts[number]
    return similarity_score

def main():
    filename = 'input.txt'
    left_list, right_list = read_input(filename)
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score between the lists is: {similarity_score}")

if __name__ == "__main__":
    main()