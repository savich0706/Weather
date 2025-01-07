from dataclasses import dataclass
from get_coordinates import Coordinates
from typing import NamedTuple
from datetime import datetime
import requests
from config import API_KEY_WEATHER
from exceptions import CantGetWeather


Celcium = int
Time = str
City = str

class Weather(NamedTuple):
    temperature: Celcium # температура прогноза в градусах цельсия
    real_temperatire: Celcium # температура по ощущению в градусах цельсия
    status: str # ясно, пасмурно, дождь и т.д.
    wind: int # Ветер м/с
    humidity: int # Влажность в %
    time_update: datetime # во сколько было последнее обновление погоды
    sunrise: Time # восход
    sunset: Time # закат
    city: City # город
    

def get_weather(coordinates: Coordinates) -> Weather:
    '''Получаем погоду по координатам'''
    latitude = coordinates.latitude
    longitude = coordinates.longitude
    return _get_data_by_response(latitude, longitude)


def _request_weather_by_api(latitude, longitude) -> dict:
    '''Запрос к open сервису для получения данных о погоде'''
    try:
        response = requests.get(f'https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={API_KEY_WEATHER}&lang=ru')
        
        if response.status_code == 200:
            return response.json()["data"][0]
    except:
        raise CantGetWeather


def _get_data_by_response(latitude, longitude) -> Weather:
    '''Получаем только необходимые данные'''
    try:
        all_data: dict = _request_weather_by_api(latitude, longitude)
        result_data = Weather(
            temperature=all_data['temp'],
            real_temperatire=all_data['app_temp'],
            status=all_data['weather']['description'],
            wind=all_data['wind_spd'],
            humidity=all_data['rh'],
            time_update=datetime.fromisoformat(all_data['ob_time']),
            sunrise=all_data['sunrise'],
            sunset=all_data['sunset'],
            city=all_data['city_name']                
            )
        return result_data
    except Exception as e:
        raise CantGetWeather
    

'''Дальнейший код нужен только для проверки работоспособности кода
при непосредственном запуске файла (Run в Вашей IDE). При запуске
всей программы из файла weather.py этот код читаться интерпретатором не будет'''
if __name__ == '__main__':    
    weather = get_weather(Coordinates(57.6, 13.2))
    print(weather)
