# Write your solution here

sentence = input("Please type in a sentence: ")
counter = 0

while counter < len(sentence):
    print(sentence[counter])
    while sentence[counter] != " ":
        counter += 1
        if counter >= len(sentence):
            break
    counter += 1