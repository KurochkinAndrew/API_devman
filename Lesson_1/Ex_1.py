import requests


def get_weather(place_name):
    payload = {
        'qMTn': '',
        'lang': 'ru'
    }
    url_template = 'https://wttr.in/{}'

    url = url_template.format(place_name)
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.text


def main():
    places = ['svo', 'Лондон', 'Череповец']

    for place in places:
        print(get_weather(place))

if __name__ == '__main__':
    main()
