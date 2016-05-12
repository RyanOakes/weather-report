# import requests
# import json
import os
from weather_classes import ZipCode


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def weather_to_play_again_or_not():
        replay = input("\nFancy a weather report? [y/N] \n")
        if replay.lower() == 'y':
            return True


def main():

    clear()

    zip_code = input("Please provide a zip code: \n")

    weather_request = ZipCode(zip_code)
    print(weather_request.retrieve_weather_info()['current_observation']['display_location']['full'])

    weather_request.check_current_conditions()
    print("The current temp is", weather_request.current_conditions, "degrees Fahrenheit.")

    # print("Forecast: ", weather_request.check_forecast())

    weather_request.check_sunrise_sunset()
    print("Sunrise is", weather_request.sunrise['hour'], ":", weather_request.sunrise['minute'])
    print("Sunset is", weather_request.sunset['hour'], ":", weather_request.sunset['minute'])


    print("Current alerts in your area:", weather_request.check_weather_alerts())

    weather_request.check_for_hurricanes()

    if weather_to_play_again_or_not():
        main()
    else:
        "Goodbye!"

if __name__ == '__main__':
    main()
