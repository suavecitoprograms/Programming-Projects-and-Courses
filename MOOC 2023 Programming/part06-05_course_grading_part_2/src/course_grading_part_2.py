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
 
for id, name in student_database.items(): ## final printout
 
    print(student_database[id], check_grade(exam_database[id], exercise_database[id]))