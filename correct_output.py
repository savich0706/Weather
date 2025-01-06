from weather_api import Weather
import datetime


def correct_print(weather: Weather) -> str:
    '''Вывод погоды в терминал в корректном виде'''
    try:
        return (f'\nПогода в {weather.city} по состоянию на '
              f'{datetime.datetime.now().strftime('%H:%M %d.%m.%Y')}:\n\nНа улице {weather.status}\n'
              f'Температура: {weather.temperature} °C\n'
              f'Температура по ощущениям: {weather.real_temperatire} °C\n'
              f'Ветер: {weather.wind} м/с\n'
              f'Влажность: {weather.humidity} %\n'
              f'Восход: {weather.sunrise}\n'
              f'Закат: {weather.sunset}\n\n'
              f'Последнее обновление данных метеостанции {weather.time_update}'
              )
    except:
        pass


if __name__ == '__main__':
    weather = Weather(temperature=-1.3, real_temperatire=-7, status='Небольшой снег', wind=5.6, humidity=92, time_update=datetime.datetime(2025, 1, 6, 10, 21), sunrise='07:45', sunset='14:38', city='Länghem') 
    print(correct_print(weather))