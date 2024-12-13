# Write your solution here
def remove_smallest(numbers: list):

    smallest = min(numbers)
    numbers.remove(smallest)
    
def main(numbers: list):
    print(remove_smallest(numbers))

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)

