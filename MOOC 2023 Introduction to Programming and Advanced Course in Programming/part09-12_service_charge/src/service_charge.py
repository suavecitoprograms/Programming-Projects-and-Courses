# WRITE YOUR SOLUTION HERE:

class BankAccount():
    def __init__(self, owner:str, account_number:str, balance:float) -> None:
        self.___owner = owner
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount must be greater than 0")
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("The account does not contain that amount")
        self.__balance -= amount
        self.__service_charge()

              
    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance -= self.__balance * .01
        
if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
