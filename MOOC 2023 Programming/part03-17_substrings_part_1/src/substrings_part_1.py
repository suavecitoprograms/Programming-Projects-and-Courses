# Write your solution here

string = input("Please type in a string: ")
number = 1

while len(string) >= number:
    print(string[:number])
    number += 1

