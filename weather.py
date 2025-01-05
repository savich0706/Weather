from correct_output import correct_print
from get_coordinates import get_coordinates
from weather_api import get_weather


def main():
    coordinates = get_coordinates()
    weather = get_weather(coordinates)
    output = correct_print(weather)
    print(output)
    
if __name__ == 'main':
    main()
    
    