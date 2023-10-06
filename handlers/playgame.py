# version 1.1-0
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter
import random
from aiogram import Bot, Dispatcher, types, F
from handlers import database as db
import datetime

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
    chat_id = message.chat.id
    user_name = message.from_user.full_name
    print(user_name)
    await db.cmd_start_db(message.from_user.id, chat_id, user_name)
    await message.answer(HELP_TEXT)


@router.message(F.text == '/help')
async def cmd_start_and_help(message: types.Message):
    await message.answer(HELP_TEXT)

@router.message(F.text == '/play')
async def cmd_up(message: types.Message):
    #setcurrentdata in date
    date = datetime.datetime.now()
    date = int(date.strftime('%Y%m%d'))
    #setdatafromdb in datauser
    dateuser = await db.select_date(message)
    for lit in dateuser:
        if lit == 1 or lit != date:
            #getsizefromdb in usersize
            usersize = await db.select_size(message)
            for user in usersize:
                math = random.randint(-5,10)
                newsize = user + math
                newdate = date
                await db.update_size(newsize, message.from_user.id)
                await db.update_date(newdate, message.from_user.id)
                if math > 0:
                    await message.answer(f'>>> 😻 Член збільшився на: {math} см. Ваш теперішній розмір: {newsize}')
                else:
                    await message.answer(f'>>> 🤏 Член зменшився на: {math} см. Ваш теперішній розмір: {newsize}')
        elif lit == date:
            await message.answer('🙁 Сьогодні ви вже зіграли. Повертайтесь завтра 🙂')
        elif lit == 1:
            newdate = date
            await db.update_date(newdate, message.from_user.id)
            db.db.commit()

@router.message(F.text == '/size')
async def cmd_size(message: types.Message):
    size = await db.select_size(message)
    for rowed in size:
        await message.answer(f">>> Ваш розмір члену: {rowed} см")\

@router.message(F.text == '/leaders')
async def cmd_getleaders(message: types.Message):
    chat_id_session = message.chat.id
    chatid_db = await db.select_chat_id(message)
    print(f"Текущий айди: {chat_id_session} Айди с бд: {chatid_db}")
    for row in chatid_db:
        if chat_id_session != row:
            print("Это работает")
            newchatid = chat_id_session
            await db.update_chat_id(newchatid, message.from_user.id)
        elif chat_id_session == row:
            allmembers = await db.select_members(message)
            print(allmembers)
    db.db.commit()