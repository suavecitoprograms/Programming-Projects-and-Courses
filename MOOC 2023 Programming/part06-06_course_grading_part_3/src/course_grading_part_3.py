if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    
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

headers = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
print(f"{headers[0]:30}{headers[1]:10}{headers[2]:10}{headers[3]:10}{headers[4]:10}{headers[5]:10}")

for id, name in student_database.items(): ## final printout
    awarded = exercise_database[id] // 4
    total = awarded + exam_database[id]
    grade = check_grade(exam_database[id], exercise_database[id])
   
    print(f"{student_database[id]:30}{exercise_database[id]:<10}{awarded:<10}{exam_database[id]:<10}{total:<10}{grade:<10}")
