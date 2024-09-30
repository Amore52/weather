import requests

VALID_UNITS = {'u', 'm', 'M'}

def retrieve_for_city(city, unit):
    params = {
        'lang': 'ru',
        'n': '',
        'q': '',
        'T': ''
    }

    if unit in VALID_UNITS:
        params[unit] = ''
        url = f"https://wttr.in/{city}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text
    else:
        return ('Некорректный ввод')

city = input("Введите город или код аэропорта: ")
unit = input("Введите единицу измерения (u, m, M): ")

weather_info = retrieve_for_city(city, unit)
print(weather_info)