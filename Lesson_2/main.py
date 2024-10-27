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

    try:
        return response.json()['response']['short_url']
    except KeyError:
        return 'Вы ввели неправильную ссылку'


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
        return 'Вы ввели неправильную ссылку'

    try:
        return click_count.json()['response']['stats'][0]['views']
    except IndexError or KeyError:
        return 0


def is_shorten_link(url):
    netloc = urlparse(url).netloc
    return 'vk.cc' in netloc


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    entered_link = input()

    if is_shorten_link(entered_link):
        click_num = get_count_clicks(token, entered_link)
        print(click_num)
    else:
        short_link = get_shorten_link(token, entered_link)
        print(short_link)


if __name__ == "__main__":
    main()
