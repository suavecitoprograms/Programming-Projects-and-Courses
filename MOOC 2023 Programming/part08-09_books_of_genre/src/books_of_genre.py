# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
# Write your solution here
def books_of_genre(books: list, genre: str):
    matching = []
    for book in books:
        if book.genre == genre:
            matching.append(book)
    return matching
# -----------------------------

if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")
    '''
    
    Please write a function named books_of_genre(books: list, genre: str) 
    which takes a list of objects of type Book and a string representing a 
    genre as its arguments.

    The function should return a new list, which contains the books with 
    the desired genre from the original list. Please see the examples below.

    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")
    Sample output
    Books in the crime genre:
    Sofi Oksanen: Norma
    Jo Nesbø: The Snowman
    
    '''