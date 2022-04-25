import os
import time
import json
from main import collect_data
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from aiogram import Bot, Dispatcher, executor, types

TOKEN = '5207577524:AAFWyFgWKd_yZCzSqiULfKNZ2GQb8yWI-h0'

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = [ '🔪 Pichoqlar', '🥊 Qo\'lqoplar', '🔫 Snayperli miltig\'']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Katalog tanlang", reply_markup=keyboard)

@dp.message_handler(Text(equals='🔪 Pichoqlar'))
async def get_discount_knives(message: types.Message):
    await message.answer('Iltimos biroz kuting...')

    collect_data(cat_type=2)

    with open('result.json', encoding="utf8") as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Chegirma: ")}{item.get("overprice")}%\n' \
            f'{hbold("Narxi: ")}${item.get("item_price")}🔥'
        

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals='🔫 Snayperli miltig\''))
async def get_discount_guns(message: types.Message):
    await message.answer('Iltimos biroz kuting...')

    collect_data(cat_type=4)

    with open('result.json', encoding="utf8") as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Chegirma: ")}{item.get("overprice")}%\n' \
            f'{hbold("Narxi: ")}${item.get("item_price")}🔥'
        

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals='🥊 Qo\'lqoplar'))
async def get_discount_gloves(message: types.Message):
    await message.answer('Iltimos biroz kuting...')

    collect_data(cat_type=13)

    with open('result.json', encoding="utf8") as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
            f'{hbold("Chegirma: ")}{item.get("overprice")}%\n' \
            f'{hbold("Narxi: ")}${item.get("item_price")}🔥'
        

        if index%20 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
