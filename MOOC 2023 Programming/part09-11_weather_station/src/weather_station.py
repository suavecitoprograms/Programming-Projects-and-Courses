# WRITE YOUR SOLUTION HERE:

class WeatherStation():
    def __init__(self, name:str) -> None:
        self.__name = name
        self.__observed = []
        self.__latest_observed = ""
    
    
    def add_observation(self, observation: str):
        self.__observed.append(observation)
        self.__latest_observed = observation
    
    def latest_observation(self):
        return self.__latest_observed
    
    def number_of_observations(self):
        return len(self.__observed)
    
    def __str__(self):
        return f"{self.__name}, {len(self.__observed)} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)