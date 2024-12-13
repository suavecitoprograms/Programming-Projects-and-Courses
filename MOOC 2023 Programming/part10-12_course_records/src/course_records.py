# tee ratkaisusi tänne
"""
idea
- create class for Courses
    -> should contain data attributes (course. grade, credits)
    -> when getting course data should show: name (x credits) grade x
 
- create class for CourseRecords
    -> must calculate total courses, credits, mean (average out of 5)
    -> and a visual distribution of grades:
        5 completed courses, a total of 29 credits
        mean 3.4
        grade distribution
        5: xx
        4: x
        3:
        2: x
        1: x
    
- create class for CourseRecordsApplication
"""

# tee ratkaisusi tänne

class Courses:
    def __init__(self, course:str, grade:int, credits:int) -> None:
        self.__course = course
        self.__grade = grade
        self.__credits = credits
    
    @property # no setter because we dont the name of the object to be mutable
    def course(self):
        return self.__course
    
    @property # no setter because we dont the credits of the object to be mutable
    def credits(self):
        return self.__credits
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade:int):
        if grade > self.__grade:
            self.__grade = grade
            
    def __str__(self) -> str:
        return f"{self.__course} ({self.__credits} cr) grade {self.__grade}"

class CourseRecords:
    def __init__(self):
        self.__records = {}
        
    def records(self):
        return self.__records
    
    def courses(self):
        return len(self.__records)
    
    def add_course(self, course: Courses):
        self.__records[course.course] = course
        
    def find_course(self, course: str):
        if not course in self.__records:
            return None
        return self.__records[course]
    
    def credits(self):
        total = 0
        if self.courses() == 0:
            return total
        for course in self.__records.values():
            total += course.credits
        return total
            
    def grade(self) -> tuple:
        total = 0
        distribution = [0, 0, 0, 0, 0]
        if self.courses() == 0:
            return total
        for course in self.__records.values():
            total += course.grade
            distribution[course.grade-1] += 1
            
        return total, distribution

    def __str__(self) -> str:
        f = ""
        for course in self.__records.values():
            f += f"{course} \n"
        return f

class CourseApplication:
    def __init__(self) -> None:
        self.__records = CourseRecords()
        
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("0 exit")
        
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        
        if course not in self.__records.records():
            course_object = Courses(course, grade, credits)
            self.__records.add_course(course_object)
        else:
            self.__records.records()[course].grade = grade
        
    def get_course(self):
        course = input("course: ")
        course_info = self.__records.find_course(course)
        
        if course_info == None:
            print(f"no entry for this course")
            return
        print(course_info)
        
    def statistics(self):
        completed_courses = self.__records.courses()
        total_credits = self.__records.credits()
        
        info = self.__records.grade()
        
        mean = info[0] / completed_courses
        distribution = info[1]
        
        print(f"{completed_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        
        for i in range(1, 6):
            print(f"{i}: " + "x" * distribution[i - 1])
            
    def execute(self):
        self.help()
        while True:
            command = int(input("command: "))
            if command == 1:
                self.add_course()
            elif command == 2:
                self.get_course()
            elif command == 3:
                self.statistics()
            elif command == 0:
                break
            else:
                print(f"You did not type in a valid command!")
                break
    

course_records = CourseApplication()
course_records.execute()