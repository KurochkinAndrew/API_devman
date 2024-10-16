import requests
import logging


logger = logging.getLogger('app_logger')
url_template = 'https://wttr.in/{}'
places_list = ['svo', 'Лондон', 'Череповец']

def get_weather():
    payload = {
        'qMTn': '',
        'lang': 'ru'
    }
    for place in places_list:
        response = None
        url = url_template.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()

        print(response.text)

def main():
    get_weather()


if __name__ == '__main__':
    main()
