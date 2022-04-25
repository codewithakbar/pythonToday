from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup
import requests

TOKEN = '5207577524:AAFWyFgWKd_yZCzSqiULfKNZ2GQb8yWI-h0'

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    salom = f"Salom!\nMen Glotr qidiruvchi botman\nMaxsulot nomini yozing"

    await bot.send_message(message.chat.id, salom)


# parser
@dp.message_handler(content_types=['text'])
async def parse(message: types.Message):
    url = "https://glotr.uz/search/?q=" + message.text
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")

    all_links = soup.find_all('a', class_='proposal-item-link')
    for link in all_links:
        url = "https://glotr.uz" + link['href']
        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        name = soup.find("div", class_="single-main-info").find("h1")
        # print(name)
        price = soup.find("div", class_="single-price").fing("span")
        








def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
