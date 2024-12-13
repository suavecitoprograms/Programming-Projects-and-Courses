# Write your solution here
from datetime import datetime, timedelta

def input_from_user(database : dict):
    filename = input("Filename: ")
    date = input("Starting date: ")
    days = int(input("How many days: "))
    
    date_dt = datetime.strptime(date, "%d.%m.%Y")
    starting_date = date_dt.strftime("%d.%m.%Y")
    
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    
    total = 0
    for day in range(days):
        each_day = date_dt + timedelta(days=day)
        individual_date = datetime.strftime(each_day, "%d.%m.%Y")
        screen_time = input(f"Screen time {individual_date}: ")
        
        database[individual_date] = [int(x) for x in screen_time.split()]
        total += sum(database[individual_date])
        
    average = total/len(database)
    
    write_to_file(database, filename, starting_date, datetime.strftime(each_day, "%d.%m.%Y"), total, average)
    
    print(f"Data stored in file {filename}")
    
    
def write_to_file(database : dict, filename : str, starting_date : str, each_day : str, total, average):
    with open(filename, "w") as new_file:
        new_file.write(f"Time period: {starting_date}-{each_day}\n")
        new_file.write(f"Total minutes: {total}\n")
        new_file.write(f"Average minutes: {average}\n")
        
        for date, screen_time in database.items():
            tv = screen_time[0]
            comp = screen_time[1]
            mobile = screen_time[2]
            new_file.write(f"{date}: {tv}/{comp}/{mobile}\n")
            

def main():
    screen_time_database = {}
    input_from_user(screen_time_database)
    
main()