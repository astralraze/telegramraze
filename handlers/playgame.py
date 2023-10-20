# version 1.1-0
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile
from aiogram.methods.send_voice import SendVoice
from aiogram.filters import Filter, Command
import random
from aiogram import Bot, Dispatcher, types, F
from handlers import database as db
import datetime
import asyncio



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
    if not check_user:
        await message.reply("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        await message.reply(HELP_TEXT)

@router.message(Command('dick'))
async def cmd_up(message: types.Message):
    ATTEMPTS = 2
    check_user = await db.select_username(message)
    if not check_user:
        await message.reply("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
    #setcurrentdata in date
        now = datetime.datetime.now()
        #setdatafromdb in datauser
        dateuser = await db.select_date(message)
        if dateuser:
            last_used_time = datetime.datetime.strptime(dateuser[0], '%Y-%m-%d %H:%M:%S.%f')
            difference = now - last_used_time
            if difference < datetime.timedelta(hours=12):
                hours_left = (12 * 60 - difference.seconds // 60) // 60
                minutes_left = (12 * 60 - difference.seconds // 60) % 60
                if hours_left < 5 and hours_left != 1 and hours_left != 0:
                    await message.reply(f'😐 Почекай ще {hours_left} години {minutes_left} хвилин.')
                elif hours_left == 1:
                    await message.reply(f'😐 Почекай ще {hours_left} годину {minutes_left} хвилин.')
                elif hours_left == 0:
                    await message.reply(f'😐 Почекай ще {minutes_left} хвилин.')
                else:
                    await message.reply(f'😐 Почекай ще {hours_left} годин {minutes_left} хвилин.')
            else:
                #getsizefromdb in usersize
                usersize = await db.select_size(message)
                for user in usersize:
                    math = random.randint(-10,10)
                    newsize = user + math
                    await db.update_size(newsize, message.from_user.id)
                    await db.update_date(now, message.from_user.id)
                    if math > 0:
                        await message.reply(f'>>> 😻 Член збільшився на: {math} см. Твій теперішній розмір: {newsize} см')
                    elif math == 0:
                        await message.reply(f'>>> 😐 Член не змінився. Твій розмір: {newsize} см')
                    elif math < 0:
                        await message.reply(f'>>> 🤏 Член зменшився на: {math} см. Твій теперішній розмір: {newsize} см')

@router.message(Command('size'))
async def cmd_size(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.reply("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        size = await db.select_size(message)
        for rowed in size:
            await message.reply(f"▪︎ Твій розмір члену: {rowed} см")
            voice = FSInputFile("voice/voice_07-10-2023_03-03-21.ogg")
            await message.answer_voice(voice)

@router.message(Command('leaders'))
async def cmd_getleaders(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.reply("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        chat_id_session = message.chat.id
        chatid_db = await db.select_chat_id(message)
        for row in chatid_db:
            if chat_id_session != row:
                newchatid = chat_id_session
                await db.update_chat_id(newchatid, message.from_user.id)
                allmembers = await db.select_members(message)
                sorted_list = sorted(allmembers, key=lambda x: x[1], reverse=True)
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
                    formatted_messages.append(f'{leader_stik} ▪︎ {value} см ▪︎ {name}')
                    pers += 1

                text = '\n'.join(formatted_messages)
                await message.reply(f'👑 Список лідерів 👑\n\n{text}')
            elif chat_id_session == row:
                allmembers = await db.select_members(message)
                sorted_list = sorted(allmembers, key=lambda x: x[1], reverse=True)
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
                    formatted_messages.append(f'{leader_stik} ▪︎ {value} см ▪︎ {name}')
                    pers += 1


                text = '\n'.join(formatted_messages)
                await message.reply(f'👑 Список лідерів 👑\n\n{text}')
        db.db.commit()


@router.message(Command('rade'))
async def send_box(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.reply("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        numberID_event = 1
        eventName = await db.select_eventName(numberID_event)
        descriptionName = await db.select_eventDescription(numberID_event)
        rand_time = random.randint(10, 50)

        now = datetime.datetime.now()
        dateevent = await db.select_dateEvent(numberID_event)
        if dateevent:
            last_date_time = datetime.datetime.strptime(dateevent[0], '%Y-%m-%d %H:%M:%S.%f')
            difference = now - last_date_time
            if difference < datetime.timedelta(hours=3):
                hours_left = (3 * 60 - difference.seconds // 60) // 60
                minutes_left = (3 * 60 - difference.seconds // 60) % 60
                if hours_left < 5 and hours_left != 1 and hours_left != 0:
                    await message.reply(f'😐 Івент буде доступний через {hours_left} години {minutes_left} хвилин.')
                elif hours_left == 1:
                    await message.reply(f'😐 Івент буде доступний через{hours_left} годину {minutes_left} хвилин.')
                elif hours_left == 0:
                    await message.reply(f'😐 Івент буде доступний через {minutes_left} хвилин.')
                else:
                    await message.reply(f'😐 Івент буде доступний через {hours_left} годин {minutes_left} хвилин.')
            else:
                randSleep = random.randint(15,30)
                await db.update_dateEvent(now, numberID_event)
                await message.reply('Івент активований!\nПочався пошук конверту... Очікуйте')
                await asyncio.sleep(randSleep)
                await message.reply(f'Прийшов конверт.\n Для того щоб забрати конверт використайте команду - /claim.')
                takeIsActive = await db.takeIsActive(numberID_event)
                newActive = 1
                await db.updateIsActive(newActive, numberID_event)


@router.message(Command('claim'))
async def claim_chest(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        await message.reply("😿 Котик, ти не зареєстрований для цієї команди. Зареєструйся за допомогою /reg")
    else:
        numberID_event = 1
        takeIsActive = await db.takeIsActive(numberID_event)
        if takeIsActive == 1:
            prizeSize = random.randint(1,3)
            sizeUser = await db.select_size(message)
            for ns in sizeUser:
                newsize = prizeSize + ns
                await db.update_size(newsize, message.from_user.id)
                await message.reply(f'Ти відкрили конверт і отримали подарунок у вигляді +{prizeSize}.\n Твій поточний розмір {newsize}.')
                newActive = 0
                await db.updateIsActive(newActive, numberID_event)
        else:
            await message.reply('Конверт вже відкритий, очікуй наступного івенту.')