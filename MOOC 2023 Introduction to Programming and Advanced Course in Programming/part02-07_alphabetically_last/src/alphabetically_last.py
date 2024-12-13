# Write your solution here

worda = input("Please type in the 1st word: ")
wordb = input("Please type in the 2nd word: ")

if worda > wordb:
    print(f"{worda} comes alphabetically last.")
elif wordb > worda:
    print(f"{wordb} comes alphabetically last.")
else:
    print("You gave the same word twice.")