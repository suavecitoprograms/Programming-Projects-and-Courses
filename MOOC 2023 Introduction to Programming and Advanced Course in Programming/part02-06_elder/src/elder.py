# Write your solution here
print("Person 1:")
namea = input("Name: ")
agea = int(input("Age: "))

print("Person 2:")
nameb = input("Name: ")
ageb = int(input("Age: "))

if agea > ageb:
    print(f"The elder is {namea}")

elif ageb > agea:
    print(f"The elder is {nameb}")

else:
    print(f"{namea} and {nameb} are the same age")