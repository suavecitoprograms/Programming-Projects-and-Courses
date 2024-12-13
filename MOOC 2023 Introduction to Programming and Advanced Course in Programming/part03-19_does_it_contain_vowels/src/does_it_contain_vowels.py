
string = input("Please type in a string: ")
vowels = "aeo"

index = 0

while len(vowels) > index:
    if vowels[index] in string:
        print(f"{vowels[index]} found")
    else:
        print(f"{vowels[index]} not found")
    index += 1