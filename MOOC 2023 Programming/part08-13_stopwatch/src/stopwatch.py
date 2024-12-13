# Write your solution here:
from datetime import *

class Stopwatch:
    def __init__(self):
        self.seconds = 00
        self.minutes = 00
        
        time = f"{self.minutes}:{self.seconds}"
        time_format = datetime.strptime(time, "%M:%S")
        self.time = time_format
        
    def __str__(self) -> str:
        return self.time.strftime("%M:%S")
    
    def tick(self):
        self.time += timedelta(seconds=1)
        
if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()