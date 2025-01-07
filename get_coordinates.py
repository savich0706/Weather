from typing import NamedTuple
import requests
from exceptions import CantGetIPAdress, CantGetCoordinatesByIP


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class IPAdress(NamedTuple):
    my_ip: str    


def get_coordinates() -> Coordinates:
    '''Получаем свои координаты GPS'''
    data = _get_data_by_ip()
    latitude = data['latitude']
    longitude = data['longitude']
    return Coordinates(latitude=latitude, longitude=longitude)


def _get_my_ip() -> IPAdress:
    '''Получаем свой IP-адрес с помощью API ipify'''
    try:
        url = 'https://api.ipify.org?format=json'
        response = requests.get(url)
        
        return IPAdress(my_ip=response.json()['ip'])
    
    except:
        raise CantGetIPAdress


def _get_data_by_ip() -> dict:
    '''Через свой IP-адрес получаем город и координаты (широту и долготу) 
        с помощью API ipwhois'''
    try:
        my_ip = _get_my_ip().my_ip
        url = f"http://ipwho.is/{my_ip}"
        response = requests.get(url)
        response.raise_for_status()  # Обработка ошибок HTTP
        data = response.json()
        return data
    except CantGetIPAdress:
        raise CantGetIPAdress                         
    except:
        raise CantGetCoordinatesByIP


if __name__ == '__main__':
    coord = get_coordinates()
    print(f'Широта: {coord.latitude}\nДолгота: {coord.longitude}\n')