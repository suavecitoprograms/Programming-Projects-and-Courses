
def get_station_data(filename: str):
    with open(filename) as new_file:
        station_data = {}
        for line in new_file:
            data = line.split(";")
            
            if data[0] == "Longitude":
                continue
            
            station_data[data[3]] = (float(data[0]), float(data[1]))
        return station_data

def distance(station_data: dict, station1: str, station2: str):
    import math
    
    x_km = (station_data[station1][0] - station_data[station2][0]) * 55.26
    y_km = (station_data[station1][1] - station_data[station2][1]) * 111.2
    
    distance_km = math.sqrt(x_km**2 + y_km**2) ## pythagorean theorem to find distance
    
    return distance_km

def greatest_distance(station_data: dict):
    greatest = 0
    for start_station in station_data:
        for end_station in station_data:
                current = distance(station_data, start_station, end_station) 
                if current > greatest:
                    greatest = current
                    station_1 = start_station
                    station_2 = end_station
                
    return (station_1, station_2, greatest)
