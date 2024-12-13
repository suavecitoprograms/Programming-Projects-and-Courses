from string import *

class Registration:
    def __init__(self, owner: str, make: str, year: int, license_plate: str):
        self.__owner = owner
        self.__make = make
        self.__year = year
        
        self.license_plate = license_plate
        
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, plate):
        if Registration.license_plate_valid(plate):
            self.__license_plate = plate
        else:
            raise ValueError("Not valid")
    
    @classmethod
    def license_plate_valid(cls, plate:str):
        if len(plate) < 3 or "-" not in plate:
            return False
        letters, numbers = plate.split("-")
        
        for letter in letters:
            if letter not in ascii_lowercase:
                return False
        
        for number in numbers:
            if number not in digits:
                return False
        
        return True
        
if __name__ == "__main__":
    registration = Registration("Mary Motorist", "Volvo", "1992", "abc-123")

    if Registration.license_plate_valid("xyz-789"):
        print("This is a valid license plate!")