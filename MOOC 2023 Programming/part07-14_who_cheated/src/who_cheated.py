# Write your solution here
import csv
from datetime import *

def cheaters():
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
            if name not in submission_data:
                submission_data[name] = {task: (points, sub_time)}
            elif task in submission_data[name]: ## submission_data[name][task][1]
                if sub_time > submission_data[name][task][1]:
                    submission_data[name][task] = (points, sub_time)
            else:
                submission_data[name][task] = (points, sub_time)
                
    cheat_list = []
    
    for student1, time_start in start_times.items():
        time_limit = time_start + timedelta(hours=3)
        ## format of submission_data is {name: {task1: points;hh:mm, task2:}, name:...}
        look_up_student = submission_data[student1]
        for tasks, (points, timestamp) in look_up_student.items():
            if timestamp > time_limit:
                if student1 not in cheat_list:
                    cheat_list.append(student1)
                    break
    
    return cheat_list