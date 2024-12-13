# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)
        
    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if self.count_numbers() > 0:
            return self.get_sum() / self.count_numbers()
        return 0
    
def main():
    print("Please type in integer numbers:")
    all = NumberStats()
    odd = NumberStats()
    even = NumberStats()
    
    while True:
        number = int(input(""))
        if number == -1:
            break
        if number % 2 == 0:
            even.add_number(number)
        else:
            odd.add_number(number)
        all.add_number(number)
    
    print(f"Sum of numbers: {all.get_sum()}")
    print(f"Mean of numbers: {all.average()}")
    print(f"Sum of even numbers: {even.get_sum()}")
    print(f"Sum of odd numbers: {odd.get_sum()}")

    
main()
