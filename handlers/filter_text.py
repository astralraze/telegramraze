from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram import Bot, Dispatcher, types, F

router_filter = Router()


SAVOCHKIN_PHRASE = [
    'Савочкин', 'Savochkin', 'Савочкину', 'Савочкиным', 'Савочкін', 'Савочкіну', 'Савочкіним',
    'Владислав Савочкін', 'Владислав Савочкин', 'Владиславу Савочкину', 'Влад Савочкин',
    'савочкин', 'савочкін', 'владислав савочкін', 'владислав савочкин', 'савочкину', 'савочкина'
]

SKAKUN_PHRASE = [
    'скакун', 'Скакун', 'Скакунчик', 'Артем Скакун', 'Skakun', 'Артём Скакун', 'Админ Скакун'
]


@router_filter.message()
async def filter(message: types.Message):
    if any(word in message.text for word in SAVOCHKIN_PHRASE):
        await message.reply("Савочкин пидрила ебаное. Мать его умерла давно.")
    elif any(word in message.text for word in SKAKUN_PHRASE):
        await message.reply("Скакун пидрила ебаное. Мать его умерла давно.")
    else:
        pass