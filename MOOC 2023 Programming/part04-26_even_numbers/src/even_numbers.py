# Write your solution here
def even_numbers(my_list : list):
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

def main(my_list, new_list):
    if even_numbers():
        print("original", my_list)
        print("new", new_list)
        
if __name__ == "__main__":
    main()
    