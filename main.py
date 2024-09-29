import requests


def retrieve_for_city(city, unit):
    params = {
        'lang': 'ru',
        '?n': '',
        '?q': '',
        '?T': ''
    }

    if unit == 'u':
        params['?u'] = ''
    elif unit == 'm':
        params['?m'] = ''
    elif unit == 'M':
        params['?M'] = ''


    url = f"https://wttr.in/{city}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


city = input("Введите город или код аэропорта: ")
unit = input("Введите единицу измерения (u, m, M): ")

weather_info = retrieve_for_city(city, unit)
print(weather_info)