# Write your solution here
from difflib import *

spell_check = input("write text: ")

word_list = []
    
with open("wordlist.txt") as new_file:
    for line in new_file:
        word_list.append(line.strip())
wrong_words = {}

for word in spell_check.split():
    if word.lower() not in word_list:
        print(f" *{word}*", end="")
        wrong_words[word] = get_close_matches(word, word_list)
    else:
        print(f" {word}", end="")
print()
for word, suggestions in wrong_words.items():
    word_list = ", ".join(suggestions)
    print(f"{word}: {word_list}")
    

