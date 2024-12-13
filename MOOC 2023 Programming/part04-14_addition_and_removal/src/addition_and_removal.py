# Write your solution here
def add_remove():
    list = []
    while True:
        print(f"The list is now {list}")
        choice = input("a(d)d, (r)emove or e(x)it: ")
        
        if choice == "d":
            list.append(len(list)+1)
            
        if choice == "r":
            list.pop(len(list) - 1)
            
        if choice == "x":
            print("Bye!")
            break

add_remove()