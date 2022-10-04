import requests

Locations = ['London', 'svo', 'Cherepovets']


def what_weather_is_in(location):
    weather_pref = {
        'nTq': '',
        'lang': 'en'
    }
    response = requests.get(url=f'http://wttr.in/{location}',params=weather_pref)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for location in Locations:
        print(what_weather_is_in(location))