from dataclasses import dataclass
from get_coordinates import Coordinates
from typing import NamedTuple
from datetime import datetime


Celcium = int

class Weather(NamedTuple):
    temperature: Celcium # температура в градусах цельсия
    status: str # ясно, пасмурно, дождь и т.д.
    wind: int # Ветер м/с
    humidity: int # Влажность в %
    sunrise: datetime # восход
    sunset: datetime # закат
    

def get_weather(coordinates: Coordinates) -> Weather:
    '''Получаем погоду по координатам'''
    return Weather(
        temperature=15,
        status='Ясно',
        wind=3,
        humidity=80,
        sunrise=datetime(2025, 1, 5, 8, 12, 0),
        sunset=datetime(2025, 1, 5, 16, 3, 0)
    )


if __name__ == '__main__':    
    weather = get_weather(Coordinates(57.6, 13.2))
    print(weather.temperature)