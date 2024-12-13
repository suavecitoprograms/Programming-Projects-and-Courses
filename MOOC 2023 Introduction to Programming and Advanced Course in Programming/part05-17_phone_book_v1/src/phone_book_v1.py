# Write your solution here
    
def search(phone_book : dict):
    name = input("name: ")
    if name not in phone_book:
        print("no number")
    else:
        print(phone_book[name])
            
    
def add(phone_book):
    name = input("name: ")
    phone_book[name] = input("number: ")
    print("ok!")


def main():
    phone_book = {}
    while True:
        choice = int(input("command (1 search, 2 add, 3 quit): "))
        if choice == 1:
            search(phone_book)
        elif choice == 2:
            add(phone_book)
        else:
            print("quitting...")
            break

main()
            
    


'''
As you can see above, each name can be attached to a single number only.
If a new entry with the same name is added, the number attached to the
old entry is replaced with the new number.
command (1 search, 2 add, 3 quit): 2
name: peter
number: 09-22223333
ok!
command (1 search, 2 add, 3 quit): 1
name: peter
09-22223333
command (1 search, 2 add, 3 quit): 3
quitting...

phone_book = {}
while True:
    choice = int(input("command (1 search, 2 add, 3 quit): "))
    
    if choice == 1:
        name = input("name: ")
        if name not in phone_book:
            print("no number")
        else:
            print(phone_book[name])
            
    elif choice == 2:
        name = input("name: ")
        if name not in phone_book:
            phone_book[name] = 0
        phone_book[name] = input("number: ")
        print("ok!")
    
    else:
        print("quitting...")
        break
            

'''