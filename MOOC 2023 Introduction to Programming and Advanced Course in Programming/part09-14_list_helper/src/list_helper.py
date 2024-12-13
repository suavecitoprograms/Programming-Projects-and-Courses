# WRITE YOUR SOLUTION HERE:

class ListHelper():
    def __init__(self) -> None:
        pass
    
    
    @classmethod
    def database(cls, my_list: list):
        freq = {}
        for number in my_list:
            if number not in freq:
                freq[number] = 0
            freq[number] += 1
        return freq
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        freq = ListHelper.database(my_list)
        greatest = ""
        start = True
        for number, frequency in freq.items():
            if start or frequency > freq[greatest]:
                greatest = number
                start = False
        return greatest
            
    
    @classmethod
    def doubles(cls, my_list: list):
        freq = ListHelper.database(my_list)
        doble = []
        for number, frequency in freq.items():
            if frequency >= 2:
                doble.append(number)
        return len(doble)
    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))