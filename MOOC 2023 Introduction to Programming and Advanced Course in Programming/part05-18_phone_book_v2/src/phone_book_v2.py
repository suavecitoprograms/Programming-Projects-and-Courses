# Write your solution here

    
def search(phone_book : dict):
    name = input("name: ")
    if name not in phone_book:
        print("no number")
    else:
        for number in phone_book[name]:
            print(number)
            
    
def add(phone_book):
    name = input("name: ")
    if name not in phone_book:
        phone_book[name] = []
    phone_book[name].append(input("number: "))
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