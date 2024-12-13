# Write your solution here

def smallest_average(person1: dict, person2: dict, person3: dict):
    directory = (person1, person2, person3)
    start = True
    for person in directory:
        total = 0
        for category, value in person.items():
            if category == "name":
                continue
            total += value
        if start or total < max:
            max = total
            winner = person
            start = False
    return winner


    
if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    person3 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}

    print(smallest_average(person1, person2, person3))