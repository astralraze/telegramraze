# version 1.1-0
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
import random
from aiogram import Bot, Dispatcher, types, F
from handlers import database as db

HELP_TEXT = """
Умови гри 'Розмір члену'.
Ви можете збільшити або зменшити свій розмір члену від -10 до +10 см в день.

/size - Дізнатися свій розмір члену.
/play - Випробувати свою удачу на день та дізнайтеся теперішній розмір вашого члену.
"""

router = Router()

@router.message(F.text == '/start')
async def cmd_start_and_help(message: types.Message):
    #Вытягиваем id и записываем в бд
    await db.cmd_start_db(message.from_user.id)
    await message.answer(HELP_TEXT)
    print("Я в ахуи")

@router.message(F.text == '/help')
async def cmd_start_and_help(message: types.Message):
    await message.answer(HELP_TEXT)

@router.message(F.text == '/play')
async def cmd_up(message: types.Message):
    usersize = db.cur.execute("SELECT size FROM accounts WHERE tg_id == {key}".format(key=message.from_user.id)).fetchone()
    for user in usersize:
        math = random.randint(-5,10)
        user = user + math
        db.cur.execute('UPDATE accounts SET size = {size} WHERE tg_id == {key}'.format(size=user, key=message.from_user.id)).fetchone()
        db.db.commit()
        if math > 0:
            await message.answer(f'>>> 😻 Член збільшився на: {math} см. Ваш теперішній розмір: {user}')
        else:
            await message.answer(f'>>> 🤏 Член зменшився на: {math} см. Ваш теперішній розмір: {user}')
@router.message(F.text == '/size')
async def cmd_size(message: types.Message):
    await message.answer(">>> Ваш розмір члену: ")
