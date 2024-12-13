# Write your solution here
import urllib.request
import json

def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = request.read()
    data = json.loads(data)
    retrieved = []
    for datum in data:
        if datum["enabled"] == True:
            retrieved.append((datum["fullName"],datum["name"], datum["year"], sum(datum["exercises"])))
    return retrieved

def retrieve_course(course_name: str):
    boilerplate = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    request = urllib.request.urlopen(boilerplate)
    datacourse = json.loads(request.read())

    attendance = []
    hours = 0
    exercises = 0
    
    for key, value in datacourse.items():
        attendance.append(datacourse[key]["students"])
        hours += datacourse[key]["hour_total"]
        exercises += datacourse[key]["exercise_total"]
    
    students = max(attendance)
        
    return {
        "weeks" : len(datacourse),
        "students" : students,
        "hours" : hours,
        "hours_average" : hours // students,
        "exercises" : exercises,
        "exercises_average" : exercises // students
    }

