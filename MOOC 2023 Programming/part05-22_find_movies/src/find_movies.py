# Write your solution here
def find_movies(database: list, search_term: str):
    my_movies = []
    
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            my_movies.append(movie)
    return my_movies

'''
initial version when i havent realized that the .lower() method and [in] function actually searchs the whole string for the word
so python is found in "pythons"
    
    catalogue = []

    
    for movie in database:
        catalogue.append(movie["name"])
        
    for movie in range(len(catalogue)):
        catalogue[movie] = catalogue[movie].lower()
    
    for movie in catalogue:
        spelling = movie.split()
        if search_term.lower() in spelling:
            i = catalogue.index(movie)
            my_movies.append(database[i])
        else:
            for word in spelling:
                spelled = ""
                for i in range(len(word)):
                    spelled += word[i]
                    if spelled == search_term.lower():
                        i = catalogue.index(movie)
                        my_movies.append(database[i])
    

'''
                        
        
    
        
if __name__ == "__main__":
    database = [
    {"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}
    ]

    my_movies = find_movies(database, "python")
    print(my_movies)
    
        
    
