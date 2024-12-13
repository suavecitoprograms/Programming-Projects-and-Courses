# Write your solution here

number = int(input("Please type in a number: "))

i = 1

while i + 1 <= number:
    print(i + 1)
    print(i)
    i += 2

if i <= number:
    print(i)