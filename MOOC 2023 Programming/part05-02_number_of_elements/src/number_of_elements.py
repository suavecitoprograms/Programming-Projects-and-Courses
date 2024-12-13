# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                count += 1
    return count
                

def main(my_matrix: list, element: int):
    print(count_matching_elements(my_matrix, element))
    
if __name__ == "__main__":
    main([[1, 2, 1], [0, 3, 4], [1, 0, 0]], 1)
    