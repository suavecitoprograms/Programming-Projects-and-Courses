# Write your solution here

def new_person(name: str, age: int):
    if name == "" or " " not in name or len(name) > 40:
        raise ValueError("Invalid argument value for name: " + name)

    if age < 0 or age > 150:
        raise ValueError("Invalid argument value for age: " + str(age))
    
    return (name, age)
