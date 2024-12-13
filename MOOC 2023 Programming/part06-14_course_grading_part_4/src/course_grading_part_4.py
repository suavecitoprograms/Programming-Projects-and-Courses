# tee ratkaisu tänne

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_info = input("Course information: ")
    print(f"Results written to files results.txt and results.csv")

else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_info = "course1.txt"
    
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
        exercises = 0
        if line[0] == "id":
            continue
        for exercise in line[1:]:
            exercise.strip()
            exercises += int(exercise)
        exercise_database[line[0]] = exercises 
        
exam_database = {}

with open(exam_data) as new_file:
    for line in new_file:
        line = line.split(";")
        exams = 0
        if line[0] == "id":
            continue
        for exam in line[1:]:
            exam.strip()
            exams += int(exam)
        exam_database[line[0]] = exams 

def check_grade(iexam, iexercise):
    boundaries = [15, 18, 21, 24, 28]
    total = iexam + (iexercise // 4)
    a = 0
    while a < 5 and total >= boundaries[a]:
        a += 1
    return a

course_data = []

with open(course_info) as new_file:
    for line in new_file:
        line = line.split(":")
        course_data.append(line[1].strip())
 
with open("results.txt", "w") as new_file:
    header_section = f"{course_data[0]}, {course_data[1]} credits"
    divider = len(header_section) * "="
    
    new_file.write(f"{header_section}\n")
    new_file.write(f"{divider}\n")
    
    headers = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
    new_file.write(f"{headers[0]:30}{headers[1]:10}{headers[2]:10}{headers[3]:10}{headers[4]:10}{headers[5]:10}\n")

    for id, name in student_database.items(): ## final printout
        awarded = exercise_database[id] // 4
        total = awarded + exam_database[id]
        grade = check_grade(exam_database[id], exercise_database[id])

        new_file.write(f"{student_database[id]:30}{exercise_database[id]:<10}{awarded:<10}{exam_database[id]:<10}{total:<10}{grade:<10}\n")

with open("results.csv", "w") as new_file:
    for id, name in student_database.items():
        grade = check_grade(exam_database[id], exercise_database[id])
        new_file.write(f"{id};{name};{grade}\n")