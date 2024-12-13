# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = int(input("Function: "))
    
    if choice == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        with open("dictionary.txt", "a") as new_file:
            new_file.write(f"{finnish};{english}\n")
        print("Dictionary entry added")
            
    
    elif choice == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as new_file:
            for line in new_file:
                line = line.split(";")
                line[1] = line[1].strip()
                if line[0].startswith(search) or line[1].startswith(search):
                    print(f"{line[0]} - {line[1].strip()}")
        
    else:
        print("Bye!")
        break