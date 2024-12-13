# Write your solution here
story = ""
entry = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or entry == word:
        break
    entry = word
    story += word + " "

print(story)