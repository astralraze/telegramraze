# version 1.1-0
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
import random
from aiogram import Bot, Dispatcher, types, F
from handlers import database as db
import datetime

HELP_TEXT = """
Умови гри '🌵 DICK DICK DICK 🌵'.
Ви можете збільшити або зменшити свій розмір пісюна від -5 до +10 см в день.
👑 Змагайтесь з гравцями за найбільший пісюн чату 

🎲 /dick - Випробувати удачу. 
🌵 /size - Дізнатися свій розмір пісюна. 
👑 /leaders - Переглянути таблицю лідерів.
"""

router = Router()

@router.message(Command('dickinfo'))
async def cmd_start_and_help(message: types.Message):
    check_user = await db.select_username(message)
    print (check_user)
    if not check_user:
        await message.answer("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        await message.answer(HELP_TEXT)

@router.message(Command('dick'))
async def cmd_up(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.answer("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
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

@router.message(Command('size'))
async def cmd_size(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.answer("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        size = await db.select_size(message)
        for rowed in size:
            await message.answer(f">>> Ваш розмір члену: {rowed} см")

@router.message(Command('leaders'))
async def cmd_getleaders(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.answer("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
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
                sorted_list = sorted(allmembers, key=lambda x: x[1], reverse=True)
                print(sorted_list)
                formatted_messages = []
                pers = 1
                leader_stik = '🥇'
                for name, value in sorted_list:
                    if pers == 1:
                        leader_stik = leader_stik
                    elif pers == 2:
                        leader_stik = '🥈'
                    elif pers == 3:
                        leader_stik = '🥉'
                    elif pers > 3:
                        leader_stik = '👤'
                    formatted_messages.append(f'{leader_stik}  {name} 👉 {value} см')
                    pers += 1

                text = '\n'.join(formatted_messages)
                await message.answer(f'👑 Список лідерів 👑\n\n{text}')
        db.db.commit()
