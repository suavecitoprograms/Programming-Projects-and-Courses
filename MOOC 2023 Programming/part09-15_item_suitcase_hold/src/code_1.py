# Write your solution here:
class Item():
    def __init__(self, name:str, weight:int) -> None:
        if name != "":
            self.__name = name
        else:
            raise ValueError("Name must not be an empty string!")
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Weight must not be zero or negative!")

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"
        
    
class Suitcase():
    def __init__(self, max:int) -> None:
        self.max = max
        self.storage = []
        
    def add_item(self, item:Item):
        if self.weight() + item.weight() > self.max:
            return
        self.storage.append(item)
        
    def weight(self):
        total = 0
        for item in self.storage:
            total += item.weight()
        return total
            

    def print_items(self):
        for item in self.storage:
            print(item)
            
    def heaviest_item(self):
        if len(self.storage) == 0:
            return None
        heavy = self.storage[0]
        for item in self.storage[1:]:
            if item.weight() > heavy.weight():
                heavy = item
        return heavy
    
    def __str__(self) -> str:
        grammar = "item" if len(self.storage) == 1 else "items"
        weight = self.weight()
        return f"{len(self.storage)} {grammar} ({weight} kg)"
    
class CargoHold():
    def __init__(self, maximum:int) -> None:
        self.maximum = maximum
        self.storage = []
        self.weight = 0
        
    def add_suitcase(self, suitcase: Suitcase):
        if self.weight + suitcase.weight() > self.maximum:
            return
        self.storage.append(suitcase)
        self.weight += suitcase.weight()
        
    def print_items(self):
        for suitcase in self.storage:
            for item in suitcase.storage:
                print(f"{item.name()} ({item.weight()} kg)")
        
    def __str__(self) -> str:
        grammar = "suitcase" if len(self.storage) == 1 else "suitcases"
        weight = self.weight
        return f"{len(self.storage)} {grammar}, space for {self.maximum - self.weight} kg"
    

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()