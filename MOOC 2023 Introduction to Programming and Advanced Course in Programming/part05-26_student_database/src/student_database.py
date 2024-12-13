# Write your solution here
# work in  progress
def add_student(students, my_student:str):
    students[my_student] = {}
    return students

def add_course(students, my_student:str, my_course:tuple): ## my_course is a tuple (course, grade)
    completed_courses = students[my_student]
    course_name = my_course[0]
    course_grade = my_course[1]
    
    if my_course[1] == 0: ## ignore when the grade is 0
        return students
    
    if course_name in completed_courses:
        if completed_courses[course_name][1] > course_grade:
            return
    
    students[my_student] = my_course

def summary(students):
    courses = 0
    most = ""
    average = 0
    best = ""
    
    for student in students:
        cumulative = 0
        for item in students[student]:
            cumulative += students[student][item][1]

        if cumulative / (len(students[student])) > average:
            average = cumulative / (len(students[student]))
            best = student
        
        if len(students[student]) > courses:
            courses = len(students[student])
            most = student


    print(f"students {len(students)}")
    print(f"most courses completed", courses, most)
    print(f"best average grade", average, best)
    

def print_student(students, my_student : str):
    if my_student not in students:
        print(f"{my_student}: no such person in the database")
    else:
        cumulative = 0
        print(f"{my_student}:")
        if students[my_student] != {}:
            print(f" {len(students[my_student])} completed courses:")
            for courses in students[my_student]:
                cumulative += courses[1]
                print("  " + courses[0], courses[1])
            print(f" average grade {cumulative/len(students[my_student])}")
        else:
            print(" no completed courses")
    
def main():
    students = {}
    add_student(students, "")
    
    return students


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    print_student(students, "Peter")
