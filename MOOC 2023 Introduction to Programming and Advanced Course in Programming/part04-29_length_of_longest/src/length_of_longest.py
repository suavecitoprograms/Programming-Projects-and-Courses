# Write your solution here
def length_of_longest(my_list : list):
    longest = 0 # The initial value depends on the situation
    for item in my_list:
        if len(item) > longest:
            longest = len(item)
    return longest

def main(longest):
    if length_of_longest():
        print(longest)
        
if __name__ == "__main__":
    main()
