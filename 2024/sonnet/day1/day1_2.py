from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of numbers in the right list
    right_counter = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = sum(num * right_counter[num] for num in left_list)
    
    return similarity_score

def main():
    left_list = []
    right_list = []

    # Read input from file
    with open('input.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    # Calculate and print the similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"The similarity score between the lists is: {similarity_score}")

if __name__ == "__main__":
    main()
