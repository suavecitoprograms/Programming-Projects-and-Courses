# Write your solution here
from json import *

def print_persons(filename: str):
    with open(filename) as new_file:
        data = new_file.read()
    database = loads(data)
    
    for person in database:
        hobbies = ", ".join(person['hobbies'])
        print(f"{person['name']} {person['age']} years ({hobbies})")
    