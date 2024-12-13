# Write your solution here:

class Book():
    def __init__(self, name:str, author:str, genre: str, year:int) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
    
if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

    print(f"{python.author}: {python.name} ({python.year})")
    print(f"The genre of the book {everest.name} is {everest.genre}")
    '''
    
    Please write a class named Book with the attributes name, author, genre and year, 
    along with a constructor which assigns initial values to these attributes.

    Your class should work like this:

    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

    print(f"{python.author}: {python.name} ({python.year})")
    print(f"The genre of the book {everest.name} is {everest.genre}")
        
    '''