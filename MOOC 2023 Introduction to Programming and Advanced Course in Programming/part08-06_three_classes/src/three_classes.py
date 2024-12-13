# Write your solution here
class Checklist():
    def __init__(self, header:str, entries:list) -> None:
        self.header = header
        self.entries = entries

class Customer():
    def __init__(self, id:str, balance:float, discount:int) -> None:
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable():
    def __init__(self, model:str, length:float, max_speed:int, bidirectional:bool) -> None:
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional
    
if __name__ == "__main__":
    
    '''
    
    Please write the three classes specified below. Each class 
    should have exactly the same names and types of attributes as listed.

    Please also include a constructor in each class. The constructor
    should take the initial values of the attributes as its arguments,
    in the order listed below.

    Class Checklist
    attribute header (string)
    attribute entries (list)
    
    Class Customer
    attribute id (string)
    attribute balance (float)
    attribute discount (integer)
    
    Class Cable
    attribute model (string)
    attribute length (float)
    attribute max_speed (integer)
    attribute bidirectional (Boolean)   
    
    
    '''