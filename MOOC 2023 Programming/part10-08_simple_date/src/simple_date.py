# WRITE YOUR SOLUTION HERE:
# not implementing the datetime module from python std lib

class SimpleDate():
    def __init__(self, day:int, month:int, year:int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year
        
    def value(self) -> int:
        return (self.__year * 360) + (self.__month * 30) + (self.__day)
    
    def date(self, day:int) -> tuple:
        year = day // 360
        day = day % 360
        month = day // 30
        day = day % 30
        return SimpleDate(day, month, year)
        
    def __lt__(self, another: "SimpleDate") -> bool: ## less than or older
        return self.value() < another.value()

    def __gt__(self, another: "SimpleDate") -> bool: ## gt than or earlier
        return self.value() > another.value()
      
    def __eq__(self, another: "SimpleDate") -> bool: ## eq to
        return self.value() == another.value()
 
    def __ne__(self, another: "SimpleDate") -> bool: ## less than or older
        return self.value() != another.value()
    
    def __add__(self, days:int) -> "SimpleDate":
        return self.date(self.value() + days)
    
    def __sub__(self, date:"SimpleDate") -> int:
        return  abs(self.value() - date.value())
    
    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
 
if __name__ == "__main__":
    sdate = SimpleDate(1, 12, 1999)
    print(sdate + 150)

