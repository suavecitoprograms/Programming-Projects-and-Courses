# Write your solution here

password = input("Password: ")

while True:
    confirm = input("Repeat password: ")
    if confirm == password:
        break
    print("They do not match!")

print("User account created!")