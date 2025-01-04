from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using MacBook GPS"""
    return Coordinates(10, 20)

coord = get_gps_coordinates()
print(coord.latitude)