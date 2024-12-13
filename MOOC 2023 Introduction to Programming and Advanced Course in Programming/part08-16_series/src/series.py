# Write your solution here:

class Series():
    def __init__(self, title:str, seasons:int, genre:list) -> None:
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.ratings = [0, 0, 0, 0, 0, 0]
        self.reviews = 0
        
    def __str__(self) -> str:
        total = 0
        for i in range(0, 6):
            total += self.ratings[i] * i
        average = total / self.reviews if self.reviews > 0 else 0
            
        genre_list = ", ".join(self.genre)
        
        summary = ""
        summary += f"{self.title} ({self.seasons} seasons)\n"
        summary += f"genres: {genre_list}\n"
        summary += f"{self.reviews} ratings, average {average:.1f} points" if self.reviews > 0 else "no ratings"
            
        return summary
    
    def rate(self, rating:int):
        self.ratings[rating] += 1
        self.reviews += 1
        
    def grade(self):
        total = 0
        for i in range(0, 6):
            total += self.ratings[i] * i
            
        return total/self.reviews if self.reviews > 0 else 0
        

def minimum_grade(rating:float, series_list:list):
    matching = []

    for title in series_list:
        if title.grade() > rating:
            matching.append(title)
                
    return matching
        
def includes_genre(genre:str, series_list:list):
    matching = []
        
    for title in series_list:
        if genre in title.genre:
            matching.append(title)
                
    return matching


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)