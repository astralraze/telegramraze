from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, Command
import random
from aiogram import Bot, Dispatcher, types, F
from handlers import database as db
import datetime

router_reg = Router()

HELP_TEXT = """
🦄 Тобі доступні такі ігри:

/dick - змагайся серед гравців у розмірі пісюна. 🌵
/dickinfo - подивитись інформацію про гру та доступні команди 🌵📒
"""

ABOUT_TEXT = """
🦄 Я Misa BOT

Хочеш грати? Тобі доступні такі ігри:

/dick - змагайся серед гравців у розмірі пісюна. 🌵
/dickinfo - подивитись інформацію про гру та доступні команди 🌵📒
"""


@router_reg.message(Command('reg'))
async def cmd_start_and_help(message: types.Message):
    check_user = await db.select_username(message)
    if not check_user:
        #Вытягиваем id и записываем в бд
        chat_id = message.chat.id
        user_name = message.from_user.full_name
        print(user_name)
        await db.cmd_start_db(message.from_user.id, chat_id, user_name)
        await message.reply(f"🥰 Привіт {user_name}, ти успішно зареєстрований.\n {HELP_TEXT}")
    else:
        await message.reply(f"💞 Сонечко, ти вже був зареєстрований.\n {HELP_TEXT}")

@router_reg.message(Command('about'))
async def cmd_about(message: types.Message):
    await message.reply(f"{ABOUT_TEXT}")