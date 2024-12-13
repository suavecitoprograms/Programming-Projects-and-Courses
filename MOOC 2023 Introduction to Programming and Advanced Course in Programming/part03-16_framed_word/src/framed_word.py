# Write your solution here

word = input("Word: ")

print("*" * 30)

leftspace = (28 - len(word)) // 2
rightspace = leftspace

if leftspace + rightspace + len(word) < 28:
    leftspace += 1

print("*" + leftspace * " " + word + rightspace * " " + "*")

print("*" * 30)