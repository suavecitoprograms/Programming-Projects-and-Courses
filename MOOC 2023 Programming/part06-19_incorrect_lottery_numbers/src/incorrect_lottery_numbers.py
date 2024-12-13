# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as new_file, open("correct_numbers.csv", "w") as correct_file:
        weeks = {}
        for line in new_file:
            correct = True
            numero = {}
            
            row = line.split(";")
            week_no = (row[0].split()[1]) ## this isolates the week_number
            numbers = row[1].split(",") ## this will give us the 7 integers
            
            try:     
                if int(week_no):
                    pass
                    
                if len(numbers) != 7:
                    correct = False
                    continue
                    
                numbers[6] = numbers[6].strip()
                for i in numbers:
                    if i not in numero and int(i) in range(1,40): ## in the valid range and no duplicates
                        numero[i] = int(i)
     
                    else: ## the number appears more than once or number is invalid
                        correct = False
                        continue

            except:
                correct = False
                continue
                
            if correct:
                correct_file.write(f"{line}")