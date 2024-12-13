# Write your solution here

def add_to_list():
    number = int(input("How many items: "))
    list = []
    while number > len(list):
        new = int(input(f"Item {len(list) + 1}: "))
        list.append(new)
    print(list)
    
add_to_list()
        