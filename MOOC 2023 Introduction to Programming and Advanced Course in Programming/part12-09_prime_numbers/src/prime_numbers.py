# Write your solution here
def prime_numbers():
    numero = 2
    while True:
        if prime_check(numero):
            yield numero
        numero += 1
        
def prime_check(number:int):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))