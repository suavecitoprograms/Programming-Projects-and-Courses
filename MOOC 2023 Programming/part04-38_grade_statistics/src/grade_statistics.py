# Write your solution here

def input_from_user():
    scores_str = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        scores_str += user_input.split()
    
    scores = []
    for i in scores_str:
        scores.append(int(i))
        
    return scores

def points_average(scores):
    cumulative = 0
    
    for item in scores[0: len(scores): 2]:
        cumulative += item
    
    for item in scores[1: len(scores): 2]:
        cumulative += (item // 10)
        
    return cumulative / (len(scores) / 2)

def individual_grade(scores):
    grades = []
    boundaries = [0, 14, 17, 20, 23, 27, 30]  
    
    for i in range(0, len(scores), 2):
        exam = scores[i]
        exercise = scores[i+1]
        
        if exam < 10:
            grades.append(0)
            
        else:
            total = exam + (exercise // 10)
            
            for j in range(0, len(boundaries)):
                if boundaries[j] <= total <= boundaries[j+1]:
                    grades.append(j)
                    break
                
    return grades
    
def grade_distribution(grades):
    print("Grade distribution:")
    
    for i in range(5, -1, -1):
        stars = "*" * grades.count(i)
        print(f"{i:>2}: " + stars)
        
def pass_percentage(grades):
    passed = 0
    for item in grades:
        if item != 0:
            passed += 1
            
    percentage = passed / len(grades)
    percentage *= 100
    return percentage
    
def main():
    scores = input_from_user()
    cumulative = points_average(scores)
    grades = individual_grade(scores)
    percentage = pass_percentage(grades)
    
    print("Statistics: ")
    print(f"Points average: {cumulative:.1f}")
    print(f"Pass percentage: {percentage:.1f}")
    grade_distribution(grades)
    
main()

