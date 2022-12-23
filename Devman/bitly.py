import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

load_dotenv()


bitlinks = 'https://bit.ly/3YKOIlW'  # 'https://bit.ly/3BWoIKq', 'https://bit.ly/3hNTr5I'
long_url = 'https://obuchalka.org/20200217118457/sekreti-python-59-rekomendacii-po-napisaniu-effektivnogo-koda-slatkiv-b-2016.html'
token = os.environ['TOKEN']
domain = 'bit.ly'


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
    }
    data = {
        "long_url": link,
        "domain": domain,
        "group_guid": ""
    }

    check_link = requests.get(link, headers=headers)
    check_link.raise_for_status()

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
        'Referer': 'https://www.google.com/',
    }
    params = (
        ('unit', ''),
        ('units', '-1'),
        ('unit_reference', ''),
    )

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    # pprint(response.json())
    total_clicks = response.json()["total_clicks"]
    return total_clicks


def is_bitlink(url):
    parsed = urlparse(url)
    return parsed.netloc == domain


def cut_shema_bitlink(url):
    parsed = urlparse(url)
    return ''.join(parsed[1:])


def main():
    user_input = input('Введите ссылку: ')
    try:
        if is_bitlink(user_input):
            count = count_clicks(token, cut_shema_bitlink(user_input))
            print(f'По вашей ссылке, прошли {count} раз(а)')
        else:
            bitlink = shorten_link(token, user_input)
            print('Битлинк:', bitlink)
    except requests.exceptions.RequestException as err:
        print('Ошибка при проверке ссылки:', err)


if __name__ == '__main__':
    main()


