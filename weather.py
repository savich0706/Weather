from correct_output import correct_print
from get_coordinates import get_coordinates
from weather_api import get_weather


def main():
    coordinates = get_coordinates()
    weather = get_weather(coordinates)
    correct_weather = correct_print(weather)
    return correct_weather
    
    
if __name__ == '__main__':
    result = main()
    print(result)
    
    