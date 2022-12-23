import requests


def get_weather(city: str) -> str:
    payload = {'nmqT': '', 'lang': 'ru'}
    url = f'https://wttr.in/{city}'
    response = requests.get(url, params=payload)

    try:
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f'Ошибка при загрузке страницы: {err}')

    return response.text


if __name__ == '__main__':
    cities = ['Лондон', 'Шереметьево', 'Череповец']
    [print(get_weather(city)) for city in cities]
