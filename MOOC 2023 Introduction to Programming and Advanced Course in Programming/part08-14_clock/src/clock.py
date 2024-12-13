# Write your solution here:
from datetime import *

class Clock:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.time = datetime.strptime(f"{hours}:{minutes}:{seconds}", "%H:%M:%S")
        
    def __str__(self) -> str:
        return self.time.strftime("%H:%M:%S")
    
    def tick(self):
        self.time += timedelta(seconds=1)
        
    def set(self, hours:int, minutes:int):
        self.time = datetime.strptime(f"{hours}:{minutes}:00", "%H:%M:%S")
        
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)