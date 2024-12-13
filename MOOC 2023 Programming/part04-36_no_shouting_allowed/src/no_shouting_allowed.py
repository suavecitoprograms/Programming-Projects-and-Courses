# Write your solution here
def no_shouting(my_list : list):
    new_list = []
    
    for item in my_list:
        if not item.isupper():
            new_list.append(item)
    return new_list
    
def main(my_list):
    my_list = no_shouting(my_list)
    print(my_list)
    
if __name__ == "__main__":
    main(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"])
