# Write your solution here
while True:
    name = input("Editor: ")
    
    if name.lower() == "word" or name.lower() == "notepad":
        print("awful")
    elif name.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
                