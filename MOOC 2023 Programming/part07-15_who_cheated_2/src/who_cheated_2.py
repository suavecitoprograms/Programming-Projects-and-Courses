# Write your solution here

# Write your solution here
import csv
from datetime import *

def final_points():
    with open("start_times.csv", newline="") as new_file: 
        ## start_times.csv is in the format (name;hh:mm)
        start_times = {}
        for line in csv.reader(new_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            start_times[line[0]] = start_time
    
    with open("submissions.csv", newline="") as new_file:
        ## submission_data.csv is in the format (name;task;points;hh:mm)
        ## there are multiple tasks  + there may be resubmissions
        submission_data = {}
        for line in csv.reader(new_file, delimiter=";"):
            #submission_data[name] = {task 1 : points, (time)}
            sub_time = datetime.strptime(line[3], "%H:%M")
            name = line[0]
            task = line[1]
            points = line[2]
            time_limit = start_times[name] + timedelta(hours=3)
            
            if name not in submission_data:
                submission_data[name] = {task: (points, sub_time)}
            elif task in submission_data[name]: ## submission_data[name][task][1]
                if sub_time < time_limit:
                    if points > submission_data[name][task][0]:
                        submission_data[name][task] = (points, sub_time)
            else:
                submission_data[name][task] = (points, sub_time)
                
    points_database = {}
    
    for student1, time_start in start_times.items():
        time_limit = time_start + timedelta(hours=3)
        ## format of submission_data is {name: {task1: points;hh:mm, task2:}, name:...}
        look_up_student = submission_data[student1]
        task_total = 0
        for tasks, (points, timestamp) in look_up_student.items():
            task_total += int(points)
        points_database[student1] = task_total
        
    return points_database