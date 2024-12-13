# Write your solution here

word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)

if len(word) > index + 2:
    print(word[index:index+3])
