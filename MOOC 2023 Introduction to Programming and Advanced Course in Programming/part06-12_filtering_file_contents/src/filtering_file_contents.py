# Write your solution here
def filter_solutions():
    with open("solutions.csv") as new_file, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for line in new_file:
            pieces = line.split(";")
            
            expression = pieces[1]
            result = pieces[2]
            
            if "+" in expression:
                numbers = expression.split("+")
                correct = int(numbers[0]) + int(numbers[1]) == int(result)
            else:
                numbers = expression.split("-")
                correct = int(numbers[0]) - int(numbers[1]) == int(result)
        
            if correct:
                correct_file.write(line)
            else:
                incorrect_file.write(line)