import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет!')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        request = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric&lang=ru')
        data = request.json()

        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        await message.reply(
            f'Дата: {datetime.datetime.now().date()}\nПогода в городе: {city}\nТемпература: {temp}\nВлажность: {humidity}\nСкорость ветра: {wind}\nРассвет: {sunrise}')

    except:
        await message.reply("Проверьте название города")



if __name__ == '__main__':
    executor.start_polling(dp)


