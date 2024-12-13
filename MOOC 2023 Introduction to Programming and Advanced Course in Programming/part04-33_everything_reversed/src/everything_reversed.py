# Write your solution here

def everything_reversed(my_list : list):
    new_list = []
    for item in my_list:
        new_list.append(item[::-1])
    return new_list[::-1]
    
def main(my_list : list):
    my_list = everything_reversed(my_list)
    print(my_list)

if __name__ == "__main__":
    main(["Hi", "there", "example", "one more"])
    
