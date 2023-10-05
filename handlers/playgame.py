# version 1.1-0
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
import random

HELP_TEXT = """
Умови гри 'Розмір члену'.
Ви можете збільшити або зменшити свій розмір члену від -10 до +10 см в день.

/size - Дізнатися свій розмір члену.
/play - Випробувати свою удачу на день та дізнайтеся теперішній розмір вашого члену.
"""
LIST = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
DEFAULT_SIZE = 10


router = Router()

@router.message(F.text == '/start')
async def cmd_start_and_help(message: types.Message):
    await message.answer(HELP_TEXT)

@router.message(F.text == '/help')
async def cmd_start_and_help(message: types.Message):
    await message.answer(HELP_TEXT)

@router.message(F.text == '/play')
async def cmd_up(message: types.Message):
    math_action = None
    random_num = random.choice(LIST)
    if random_num < 0:
        math_action = DEFAULT_SIZE - random_num
    elif random_num > 0:
        math_action = DEFAULT_SIZE + random_num

    await message.answer(f'>>> Ваш теперішній розмір: {math_action}')

@router.message(F.text == '/size')
async def cmd_size(message: types.Message):
    await message.answer(">>> Ваш розмір члену: ")
