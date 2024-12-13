# Write your solution here
import csv
from datetime import *

def cheaters():
    with open("start_times.csv", newline="") as new_file: 
        ## start_times.csv is in the format (name;hh:mm)
        start_times = {}
        for line in csv.reader(new_file, delimiter=";"):
            start_times[line[0]] = line[1]
    
    with open("submissions.csv", newline="") as new_file:
        ## submission_data.csv is in the format (name;task;points;hh:mm)
        ## there are multiple tasks  + there may be resubmissions
        submission_data = {}
        for line in csv.reader(new_file, delimiter=";"):
            #submission_data[name] = {task 1 : points, (time)}
            if line[0] not in submission_data:
                submission_data[line[0]] = {line[1]: (line[2], line[3])}
            elif line[1] in submission_data[line[0]]:
                sub_time = datetime.strptime(line[3], "%H:%M")
                existing_time = datetime.strptime(submission_data[line[0]][line[1]][1], "%H:%M") ## submission_data[name][task][1]
                if sub_time > existing_time:
                    submission_data[line[0]][line[1]] = (line[2], line[3])
            else:
                submission_data[line[0]][line[1]] = (line[2], line[3])
                

    cheat_list = []
    
    for student1, time_start in start_times.items():
        start = datetime.strptime(time_start, "%H:%M")
        
        time_limit = start + timedelta(hours=3)
        
        ## format of submission_data is {name: {task1: points;hh:mm, task2:}, name:...}

        for tasks, (points, timestamp) in submission_data[student1].items():
            sub = datetime.strptime(timestamp, "%H:%M")
            print(sub, time_limit)
            if sub > time_limit:
                if student1 not in cheat_list:
                    cheat_list.append(student1)
                    break
    
    return cheat_list
                