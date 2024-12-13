# Write your solution here

string = input("Please type in a string: ")
number = len(string)

while 0 < number:
    number -= 1
    print(string[number:len(string)])
