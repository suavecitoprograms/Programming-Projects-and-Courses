# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)

while index + 2 < len(word):
        if word[index] == character:
            print(word[index:index + 3])
        index += 1