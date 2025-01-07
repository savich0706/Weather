from correct_output import correct_print
from get_coordinates import get_coordinates
from weather_api import get_weather
from exceptions import CantGetCoordinatesByIP, CantGetIPAdress, CantGetWeather


def main():
    try:
        coordinates = get_coordinates()
        weather = get_weather(coordinates)
        correct_weather = correct_print(weather)
        return correct_weather
    except CantGetCoordinatesByIP:
        return 'Произошла ошибка получения координат по IP-адресу...'
    except CantGetIPAdress:
        return 'Произошла ошибка определения Вашего IP-адреса... Проверьте интернет соединение'
    except CantGetWeather:
        return 'Произошла ошибка получения данных о погоде...'
    except Exception:
        return 'Произошла неизвестная ошибка...'
    
    
if __name__ == '__main__':
    result = main()
    print(result)
    
    