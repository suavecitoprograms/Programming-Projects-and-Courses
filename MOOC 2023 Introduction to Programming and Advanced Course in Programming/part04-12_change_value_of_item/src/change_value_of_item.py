# Write your solution here
def change_value():
    list = [1,2,3,4,5]
    while True:
        index = int(input("Index: "))
        if index < 0 or index > 4:
            break
        new = int(input("New value: "))
        if new == -1:
            break
        list[index] = new
        print(list) 
        
change_value()