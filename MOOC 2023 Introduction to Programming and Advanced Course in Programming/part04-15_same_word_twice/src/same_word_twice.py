# Write your solution here

def same_word():
    list = []
    while True:
        add = input("Word: ")
        
        if add in list:
            break
        
        list.append(add)
    print(f"You typed in {len(list)} different words")
    
same_word()
