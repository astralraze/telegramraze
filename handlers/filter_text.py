from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram import Bot, Dispatcher, types, F

router_filter = Router()

SAVOCHKIN_PHRASE = [
    'савочкин', 'savochkin', 'савочкину', 'савочкиным', 'савочкін', 'савочкіну', 'савочкіним',
    'владислав савочкін', 'владислав савочкин', 'владиславу савочкину', 'влад савочкин',
    'савочкин', 'савочкін', 'владислав савочкін', 'владислав савочкин', 'савочкину', 'савочкина',
    'савок'
]

SKAKUN_PHRASE = [
    'скакун', 'скакунчик', 'артем скакун', 'skakun', 'артём скакун', 'админ скакун'
]

RAZE_PHRASE = [
    'raze', 'рейз', 'рейзы'
]

@router_filter.message()
async def filter(message: types.Message):
    if any(word.lower() in message.text.lower() for word in SAVOCHKIN_PHRASE):
        await message.reply("Савочкин пидрила ебаное. Мать его умерла давно.")
    elif any(word.lower() in message.text.lower() for word in SKAKUN_PHRASE):
        await message.reply("Скакун пидрила ебаное. Мать его умерла давно.")
    elif message.text.__contains__('@game_penis_bot'):
        await message.reply('Ку)')
    elif any(word.lower() in message.text.lower() for word in RAZE_PHRASE):
        await message.reply('❤️ Рейзы - 100 ❤️')