# Write your solution here
def read_dictionary():
    dictionary = []
    
    with open("dictionary.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            dictionary.append(tuple(line.split(";")))
    return dictionary
    
def add_word(dictionary: list):
    finnish = input("The word in Finnish: ")
    english = input("The word in English: ")
    dictionary.append((finnish, english))
    
    with open("dictionary.txt", "a") as new_file:
        new_file.write(f"{finnish};{english}\n")
    
def search_word(dictionary: list):
    search = input("Search term: ")
    
    for finnish, english in dictionary:
        if search in finnish or search in english:
            print(f"{finnish} - {english}")

dictionary = read_dictionary()

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = int(input("Function: "))
    
    if choice == 1:
        add_word(dictionary)
        print("Dictionary entry added")
    
    elif choice == 2:
        search_word(dictionary)
    else:
        print("Bye!")
        break
