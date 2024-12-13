# Write your solution here

stringa = input("Please type in string 1: ")
stringb = input("Please type in string 2: ")

if len(stringa) > len(stringb):
    print(f"{stringa} is longer")

elif len(stringa) < len(stringb):
    print(f"{stringb} is longer")

else: 
    print("The strings are equally long")