for id, name in student_database.items(): ## final printout
    name = student_database[id]
    if id in student_database:
        total = sum(exercise_database[id])
        print(f"{name} {sum}")
    else:
        print(f"{name} 0")