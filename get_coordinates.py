from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float
    

def get_coordinates() -> Coordinates:
    '''Получаем свои координаты GPS'''
    latitude = 57.6
    longitude = 37.5
    return Coordinates(latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    coord = get_coordinates()
    print(f'Широта: {coord.latitude}\nДолгота: {coord.longitude}')