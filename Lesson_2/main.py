import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


load_dotenv()


def shorten_link(token, user_input):
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

    return response.json()


def count_clicks(token, link):
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
    count_click = requests.post(url, data=payload, params=headers)

    count_click.raise_for_status()

    return count_click.json()


def is_valid(link):
    if 'error' in link:
        return False
    return True


def is_shorten_link(url):
    netloc = urlparse(url).netloc
    if 'vk.cc' in netloc:
        return True
    return False


def main():
    token = os.environ['TOKEN']
    entered_link = input()

    if is_shorten_link(entered_link):
        click_num = count_clicks(token, entered_link)
        if is_valid(click_num):
            if click_num['response']['stats']:
                print(click_num['response']['stats'][0]['views'])
            else:
                print(0)
        else:
            print('Вы ввели неправильную ссылку')
    else:
        short_link = shorten_link(token, entered_link)
        if is_valid(short_link):
            print(short_link['response']['short_url'])
        else:
            print('Вы ввели неправильную ссылку')


if __name__ == "__main__":
    main()
