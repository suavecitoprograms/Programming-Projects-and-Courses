# Write your solution here

def formatted(my_list : list):
    new_list = []
    for item in my_list:
        item = f"{item:.2f}"
        new_list.append(item)
    my_list = new_list
    return my_list

def main(my_list : list):
    my_list = formatted(my_list)
    
    print(my_list)

if __name__ == "__main__":
    main([1.234, 0.3333, 0.11111, 3.446])
