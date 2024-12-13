# Write your solution here
def create_tuple(x: int, y: int, z: int):
    
    coordinates = (
        min([x, y, z]),
        max([x, y, z]),
        sum([x, y, z])
    )
    return coordinates
