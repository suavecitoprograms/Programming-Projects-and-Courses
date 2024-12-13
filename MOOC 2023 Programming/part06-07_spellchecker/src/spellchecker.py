# write your solution here
if True:
    spell_check = input("Write text: ")
else:
    spell_check = "This is acually a good and usefull program"

word_list = []
    
with open("wordlist.txt") as new_file:
    for line in new_file:
        word_list.append(line.strip())

for word in spell_check.split():
    if word.lower() not in word_list:
        print(f" *{word}*", end="")
    else:
        print(f" {word}", end="")