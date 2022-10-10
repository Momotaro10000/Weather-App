import requests

LOCATIONS = ['London', 'svo', 'Cherepovets']


def what_weather_is_in(location):
    weather_parameters = {
        'nmTq': '',
        'lang': 'ru'
    }
    response = requests.get(url=f'http://wttr.in/{location}',params=weather_parameters)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for location in LOCATIONS:
        print(what_weather_is_in(location))