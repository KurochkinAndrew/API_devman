import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def get_shorten_link(token, user_input):
    url = "https://api.vk.com/method/utils.getShortLink"
    payload = {
        'url': user_input
    }
    headers = {
        'access_token': token,
        'v': '5.199'
    }
    response = requests.post(url, data=payload, params=headers)
    response.raise_for_status()

    return response.json()['response']['short_url']


def get_count_clicks(token, link):
    url = "https://api.vk.com/method/utils.getLinkStats"
    path = urlparse(link).path[1:]
    payload = {
        'key': path,
        'interval': 'forever',
        'extended': '0'
    }
    headers = {
        'access_token': token,
        'v': '5.199'
    }
    click_count = requests.post(url, data=payload, params=headers)
    click_count.raise_for_status()

    if 'error' in click_count.json():
        raise Exception('Вы ввели неправильную ссылку')

    return click_count.json()['response']['stats'][0]['views']


def is_shorten_link(url):
    netloc = urlparse(url).netloc
    return 'vk.cc' in netloc


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    entered_link = input()

    if is_shorten_link(entered_link):
        try:
            click_num = get_count_clicks(token, entered_link)
            print(click_num)
        except IndexError:
            print(0)
    else:
        try:
            short_link = get_shorten_link(token, entered_link)
            print(short_link)
        except KeyError:
            print('Вы ввели неправильную ссылку')
            raise Exception('Неправильная ссылка')


if __name__ == "__main__":
    main()
