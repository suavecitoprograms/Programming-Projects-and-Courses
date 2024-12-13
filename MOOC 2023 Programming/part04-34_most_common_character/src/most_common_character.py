# Write your solution here
def most_common_character(my_str : str):
    most_common = my_str[0]
    for item in my_str:
        if my_str.count(item) > my_str.count(most_common):
            most_common = item
    return most_common
        
    
def main(my_str : str):
    my_str = most_common_character(my_str)
    print(my_str)
    
if __name__ == "__main__":
    main("abcdbd")
