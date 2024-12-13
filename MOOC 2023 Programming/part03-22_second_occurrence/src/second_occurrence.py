# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = string.find(substring)
occurrence = 0
length = len(substring)

while index < len(string):
    if string[index:index + length] == substring:
        occurrence += 1
        if occurrence == 2:
            break
        index += length
    else:
        index += 1
    
if occurrence == 2:
    print(f"The second occurrence of the substring is at index {index}.")
else:
    print("The substring does not occur twice in the string.")
