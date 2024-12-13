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

def calculate_similarity_score(left_list, right_list):
    similarity_score = 0
    for number in left_list:
        count = right_list.count(number)
        similarity_score += number * count
    return similarity_score

def main():
    left_list, right_list = read_input('input.txt')
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score between the lists is: {similarity_score}")

if __name__ == "__main__":
    main()
