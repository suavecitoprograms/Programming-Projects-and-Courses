def processing():
    with open("grades.csv") as new_file:
        database = {}
        for line in new_file:
            line = line.replace("\n", "")
            row = line.split(";")
            name = row[0]
            
            database[name] = []
            
            for grades in row[1:]:
                database[name].append(int(grades))
        print(database)
        
        for name, grades in database.items():
            best = max(grades)
            average = sum(grades) / len(grades)
            print(f"{name}: best grade {best}, average {average:.2f}")
            
processing()
'''

This following program creates a dictionary grades based
on the contents of the file. The keys are the names of the
students, and the value attached to each key is the list
of grades attained by the student. The program converts
the grades to integer values, so they can be processed easier.

{'Paul': [5, 4, 5, 3, 4, 5, 5, 4, 2, 4],
'Beth': [3, 4, 2, 4, 4, 2, 3, 1, 3, 3],
'Ruth': [4, 5, 5, 4, 5, 5, 4, 5, 4, 4]}

'''