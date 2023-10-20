import sqlite3 as sq
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery

db = sq.connect('tg.db')
cur = db.cursor()

async def cmd_start_db(user_id, chat_id, user_name):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id, size, chatID, username) VALUES ({key} , 10, {keychat}, '{nick_name}')".format(key=user_id, keychat=chat_id,
                                                      nick_name=user_name))
    db.commit()

#метод выбрать дату
async def select_date(message: types.Message):
    datauser = cur.execute("SELECT time FROM accounts WHERE tg_id == {key}".format(key=message.from_user.id)).fetchone()
    db.commit()
    return datauser

#метод выбрать размер
async def select_size(message: types.Message):
    size = cur.execute("SELECT size FROM accounts WHERE tg_id == {key}".format(key=message.from_user.id)).fetchone()
    db.commit()
    return size

#метод обновить размер
async def update_size(newsize, user_id):
    cur.execute('UPDATE accounts SET size = {size} WHERE tg_id == {key}'.format(size=newsize, key=user_id)).fetchone()
    db.commit()

#метод обновить дату
async def update_date(now, user_id):
    cur.execute("UPDATE accounts SET time = ? WHERE tg_id = ?", (now, user_id))
    db.commit()

#метод выбрать chatid у юзера
async def select_chat_id(message: types.Message):
    chatid = cur.execute('SELECT chatID FROM accounts WHERE tg_id == {key}'.format(key=message.from_user.id)).fetchone()
    db.commit()
    return chatid

#метод обновления чатайди
async def update_chat_id(newchatid, user_id):
    cur.execute("UPDATE accounts SET chatID = {chat} WHERE tg_id == {key}".format(chat=newchatid, key=user_id)).fetchone()
    db.commit()

#метод выбрать всех пользователей с одинаковым чат айди
async def select_members(message: types.Message):
    members = cur.execute('SELECT username, size FROM accounts WHERE chatID == {key}'.format(key=message.chat.id)).fetchall()
    db.commit()
    return members

#метод выбрать имя пользователя
async def select_username(message: types.Message):
    username = cur.execute('SELECT tg_id FROM accounts WHERE tg_id == {key}'.format(key=message.from_user.id)).fetchone()
    db.commit()
    return username