# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    
student_database = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.split(";")
        if line[0] == "id":
            continue
        student_database[line[0]] = f"{line[1]} {line[2].strip()}"
 
exercise_database = {}  
   
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.split(";")
        exercises = []
        if line[0] == "id":
            continue
        for exercise in line[1:]:
            exercise.strip()
            exercises.append(int(exercise))
        exercise_database[line[0]] = exercises 

for id, name in student_database.items(): ## final printout

    print(f"{student_database[id]} {sum(exercise_database[id])}")
