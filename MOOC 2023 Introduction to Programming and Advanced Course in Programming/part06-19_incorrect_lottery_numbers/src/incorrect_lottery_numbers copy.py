# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as new_file, open("correct_numbers.csv", "w") as correct_file:
        weeks = {}
        for line in new_file:
            correct = True
            
            row = line.split(";")
            week_no = (row[0].split()[1]) ## this isolates the week_number
            numbers = row[1].split(",") ## this will give us the 7 integers
            
            try:
                if int(week_no):
                    pass
            except ValueError:
                correct = False
                continue
            
            if week_no not in weeks:
                weeks[week_no] = "done"
            elif week_no in weeks:
                correct = False
                continue
            
            if len(numbers) != 7:
                correct = False
                continue
            
            numbers[6] = numbers[6].strip()
            for i in numbers:
                if numbers.count(i) > 1: ## the number appears more than once
                    correct = False
                    continue
                try:
                    if int(i) not in range(1, 40): ## not in the valid range
                        correct = False
                        continue
                except ValueError: ## numbers are not correct
                    correct = False
                    continue
            if correct:
                correct_file.write(f"{line}")
