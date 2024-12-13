# Write your solution here
from datetime import *

screen_time_database = {}

def input_from_user():
    filename = input("Filename: ")
    starting_date = input("Starting date: ")
    days_input = int(input("How many days: "))
    print(starting_date)
    s_date = datetime.strptime(starting_date, "%d.%m.%Y")
    
    print("Please type in screen time in minutes on each day (TV computer mobile): ")
    
    total = 0
    for day in range(days_input):
        individual_date = (s_date + timedelta(days=day)).strftime("%d.%m.%Y") 
        ## s_date + timedelta(days=day) will increment each day until it reaches the specifed date
        ## strftime will convert it to a string in the format "%D.%m.%Y"
        m_input = input(f"Screen time {individual_date}: ")
        
        screen_minutes = [int(x) for x in m_input.split()]
        total += sum(screen_minutes)
        
        screen_time_database[individual_date] = screen_minutes  ## we will be passing the date and the screen time
    
    average = total / len(screen_time_database)
    
    e_date = individual_date
    
    write_to_file(filename, s_date.strftime("%d.%m.%Y"), e_date, total, average) ## filename, starting date, ending date
    
    print(f"Data stored in file {filename}")
    
def write_to_file(filename : str, s_date : str, e_date : str, total , average):
    
    with open(filename, "w") as new_file:
        new_file.write(f"Time period: {s_date}-{e_date}\n") 
        new_file.write(f"Total minutes: {total}\n") 
        new_file.write(f"Average minutes: {average:.1f}\n") 
        
        for date, screentime in screen_time_database.items():
            minutes = str(screentime)
            minutes = minutes[1:len(minutes)-1].replace(",", "/")
            minutes = minutes.replace(" ", "")
            new_file.write(f"{date}: {minutes}\n")


def main():
    input_from_user()
    
main()