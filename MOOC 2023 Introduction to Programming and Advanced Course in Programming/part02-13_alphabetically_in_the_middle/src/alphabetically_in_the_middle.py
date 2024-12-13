# Write your solution here

a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

middle = ""

if a > b and a > c:
    if b > c:
        middle = b
    else:
        middle = c

if b > a and b > c:
    if a > c:
        middle = a
    else:
        middle = c

if c > b and c > a:
    if a > b:
        middle = a
    else:
        middle = b

print(f"The letter in the middle is {middle}")
