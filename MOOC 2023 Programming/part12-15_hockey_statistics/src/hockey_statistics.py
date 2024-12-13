# Write your solution here
"""
    rationale:
    create 3 classes: Player, PlayerDatabase, HockeyStatisticsApplication
    Player should contain the following data attributes and should all be encapsulated and can't be manipulated:
      "name": "Travis Zajac",
      "nationality": "CAN",
      "assists": 16,
      "goals": 9,
      "penalties": 28,
      "team": "NJD",
      "games": 69
      
    PlayerDatabase is a database that includes objects of type Player.
    It should have the following functionalities:
        - player search
        - teams
        - countries
        - players in teams
        - players from country
        - most points
        - most goals
    
    HockeyStatisticsApplication should be the only place where we handle user input.
    Once this is called we should instantly load all existing information from filename and import them as Players and into the PlayersDatabase
        - utilize "try-except" blocks when handling user inputs
"""
import json

class Player():
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties:int, team:str, games:int) -> None:
        self.__name = name
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games
        self.__points = goals + assists
        
    @property
    def name(self):
        return self.__name
    
    @property
    def nationality(self):
        return self.__nationality
    
    @property
    def assists(self):
        return self.__assists
    
    @property
    def goals(self):
        return self.__goals   
    
    @property
    def points(self):
        return self.__points 
    
    @property
    def penalties(self):
        return self.__penalties
        
    @property
    def team(self):
        return self.__team
        
    @property
    def games(self):
        return self.__games
    
    def __str__(self):
        return f"{self.__name:<20}{self.__team:>4}{self.__goals:>4} + {self.__assists:>2} ={self.__points:>4}"

class PlayerDatabase():
    def __init__(self) -> None:
        self.__player_database = {}
        
    @property
    def player_database(self):
        return self.__player_database
        
    def add_player(self, player: Player):
        self.__player_database[player.name] = player
        
    def search_player(self, name:str):
        return [self.player_database[name]]
    
    def search_team(self):
        return sorted(list(set([player.team for player in self.player_database.values()])))
    
    def search_countries(self):
        return sorted(list(set([player.nationality for player in self.player_database.values()])))
    
    def team_players(self, team:str):
        match = list(filter(lambda player: player.team == team, self.player_database.values()))
        return sorted(match, key=lambda player:player.points, reverse=True)
    
    def country_players(self, nationality:str):
        match = list(filter(lambda player: player.nationality == nationality, self.player_database.values()))
        return sorted(match, key=lambda player:player.points, reverse=True)
    
    def most(self, metric:str, nth:int):
        if metric == "points":
            match = sorted(self.player_database.values(), key=lambda player:(player.points, player.goals), reverse=True)
        elif metric == "goals":
            match = sorted(self.player_database.values(), key=lambda player:(player.goals, -player.games), reverse=True)
        return match[:nth]
    
    def __str__(self):
        return
    

class HockeyStatisticsApplication():
    def __init__(self) -> None:
        self.__application = PlayerDatabase()
        
    @property
    def application(self):
        return self.__application
        
    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
        print()
        
        
    def error_handle(self):
        print("error handling input!")
        print()
        
    def import_file(self):
        file_name = input("file name: ")
        try:
            with open(file_name) as new_file:
                info = new_file.read()
                info = json.loads(info)
            return self.handle_file(info)
        except:
            self.error_handle()
            print(f"filename not found!")
            print()
    
    
    def handle_file(self, info:list):
        for p in info: 
            player = Player(p["name"], p["nationality"], p["assists"], p["goals"], p["penalties"], p["team"], p["games"])
            self.application.add_player(player)
        print(f"read the data of {len(info)} players")
        print()
        
    def handle_print(self, match: list):
        print()
        for player in match:
            print(player)
                    
    def search_player(self):
        name = input("name: ")
        try:
            match = self.application.search_player(name)
            self.handle_print(match)
        except:
            self.error_handle()
            print("player not found!")
    
    def search_team(self):
        try:
            match = self.application.search_team()
            self.handle_print(match)
        except:
            self.error_handle()
            print("no teams available")
    
    def search_countries(self):
        try:
            match = self.application.search_countries()
            self.handle_print(match)
        except:
            self.error_handle()
            print("no countries available")
    
    def team_players(self):
        team = input("team: ")
        try:
            match = self.application.team_players(team)
            self.handle_print(match)
        except:
            self.error_handle()
            print("no teams available")
    
    def country_players(self):
        country = input("country: ")
        try:
            match = self.application.country_players(country)
            self.handle_print(match)
        except:
            self.error_handle()
            print("no teams available")
    
    def most_points(self):
        points = input("how many: ")
        try:
            match = self.application.most("points", int(points))
            self.handle_print(match)
        except:
            self.error_handle()
            print("please input a valid number")
                
    def most_goals(self):
        goals = input("how many: ")
        try:
            match = self.application.most("goals", int(goals))
            self.handle_print(match)
        except:
            self.error_handle()
            print("please input a valid number")
            
    def execute(self):
        self.import_file()
        self.help()
        
        while True:
            command = input("command: ")
            
            if command == "1": ## add order
                self.search_player()
            elif command == "2":
                self.search_team()
            elif command == "3":
                self.search_countries()
            elif command == "4":
                self.team_players()
            elif command == "5":
                self.country_players()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            elif command == "0":
                break
            else:
                print(f"no such commands exists!")
            print()
            
application = HockeyStatisticsApplication()
application.execute()
            
        
"""

with open("partial.json") as new_file:
    info = new_file.read()
    info = json.loads(info)
    
print(info)
print()
name = "Travis Zajac"
team = "NJD"
goals = 9
assist = 16

print(f"{name:<20}{team:>4}{goals:>4} + {assist:>2} ={(goals + assist):>4}")
print("Travis Zajac         NJD   9 + 16 =  25")

"""