from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts:list) -> reduce:
    return reduce(lambda acc, attempt: acc + attempt.credits, attempts, 0)
#reduce function, series, initial value
def credit_summer(attempt:CourseAttempt):
    if attempt.grade > 0:
        return True
    return False

def sum_of_passed_credits(attempts:list) -> reduce:
    course_attempts = filter(credit_summer, attempts)
    return reduce(lambda acc, attempt : acc + attempt.credits, course_attempts, 0)

def average(attempts:list):
    course_attempts = list(filter(credit_summer, attempts))
    sum = reduce(lambda acc, attempt : acc + attempt.grade, course_attempts, 0)
    return sum/len(course_attempts)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)