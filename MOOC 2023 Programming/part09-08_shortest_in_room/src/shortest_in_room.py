# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self) -> None:
        self.room = []
        self.total_height = 0
    
    def add(self, person: Person):
        self.room.append(person)
        self.total_height += person.height
    
    def is_empty(self) -> bool:
        return len(self.room) == 0
    
    def print_contents(self):
        print(f"There are {len(self.room)} persons in the room, and their combined height is {self.total_height} cm")
        
        for person in self.room:
            print(f"{person.name} ({person.height} cm)")
            
    def shortest(self):
        if self.is_empty():
            return None
        shortest = self.room[0]
        for person in self.room:
            if person.height < shortest.height:
                shortest = person
        return shortest
    
    def remove_shortest(self):
        short_person = self.shortest()
        if short_person:
            self.room.remove(short_person)
        return short_person


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()