from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
from aiogram import Bot, Dispatcher, types, F
from handlers import database as db

games_rtr = Router()

@games_rtr.message(Command(commands=['dice', 'кости', 'кістки']))
async def game_dice(message: Message):
    await message.answer('Я')
    await message.answer_dice(emoji='🎲')
    await message.answer('Ти')
    await message.answer_dice(emoji='🎲')


@games_rtr.message(Command(commands=['Bball', 'баскетбол', 'баскет']))
async def game_basketball(message: Message):
    await message.answer('Я')
    await message.answer_dice(emoji='🏀')
    await message.answer('Ти')
    await message.answer_dice(emoji='🏀')

@games_rtr.message(Command(commands=['Fball', 'футбол', 'фут']))
async def game_football(message: Message):
    await message.answer('Я')
    await message.answer_dice(emoji='⚽')
    await message.answer('Ти')
    await message.answer_dice(emoji='⚽')

@games_rtr.message(Command(commands=['darts', 'дартс']))
async def game_darts(message: Message):
    await message.answer('Я')
    await message.answer_dice(emoji='🎯')
    await message.answer('Ти')
    await message.answer_dice(emoji='🎯')
