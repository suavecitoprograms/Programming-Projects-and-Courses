# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
        self.__money = (euros * 100) + cents
        
    def __str__(self):
        return f"{(self.__money/100):.02f} eur"
    
    def __eq__(self, another: "Money") -> bool:
        return self.__money == another.__money
    
    def __ne__(self, another: "Money") -> bool:
        return self.__money != another.__money
    
    def __lt__(self, another: "Money") -> bool:
        return self.__money < another.__money
    
    def __gt__(self, another: "Money") -> bool:
        return self.__money > another.__money
    
    def __add__(self, another: "Money") -> "Money":
        result = self.__money + another.__money
        return Money(result // 100, result % 100)

    def __sub__(self, another: "Money") -> "Money":
        result = self.__money - another.__money
        if result > 0:
            return Money(result // 100, result % 100)
        raise ValueError("Negative ito boss!")
    
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1