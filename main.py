import datetime
import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        request = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru')
        data = request.json()
        # pprint(data)

        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        print(
            f'Дата: {datetime.datetime.now().date()}\nПогода в городе: {city}\nТемпература: {temp}\nВлажность: {humidity}\nСкорость ветра: {wind}\nРассвет: {sunrise}')

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input('Введите название города: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
