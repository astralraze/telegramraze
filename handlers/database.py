import sqlite3 as sq
from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery

db = sq.connect('tg.db')
cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tg_id INTEGER,"
                "size INTEGER,"
                "date INTEGER DEFAULT 1,"
                "chatID INTEGER,"
                "username TEXT)")
    db.commit()

async def cmd_start_db(user_id, chat_id, user_name):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id, size, chatID, username) VALUES ({key} , 10, {keychat}, '{nick_name}')".format(key=user_id, keychat=chat_id,
                                                      nick_name=user_name))
    db.commit()

#метод выбрать дату
async def select_date(message: types.Message):
    datauser = cur.execute("SELECT date FROM accounts WHERE tg_id == {key}".format(key=message.from_user.id)).fetchone()
    return datauser
    db.commit()

#метод выбрать размер
async def select_size(message: types.Message):
    size = cur.execute("SELECT size FROM accounts WHERE tg_id == {key}".format(key=message.from_user.id)).fetchone()
    return size
    db.commit()

#метод обновить размер
async def update_size(newsize, user_id):
    cur.execute('UPDATE accounts SET size = {size} WHERE tg_id == {key}'.format(size=newsize, key=user_id)).fetchone()
    db.commit()

#метод обновить дату
async def update_date(newdate, user_id):
    cur.execute("UPDATE accounts SET date = {datetime} WHERE tg_id == {key}".format(datetime=newdate, key=user_id)).fetchone()
    db.commit()

#метод выбрать chatid у юзера
async def select_chat_id(message: types.Message):
    chatid = cur.execute('SELECT chatID FROM accounts WHERE tg_id == {key}'.format(key=message.from_user.id)).fetchone()
    return chatid
    db.commit()

#метод обновления чатайди
async def update_chat_id(newchatid, user_id):
    cur.execute("UPDATE accounts SET chatID = {chat} WHERE tg_id == {key}".format(chat=newchatid, key=user_id)).fetchone()
    db.commit()

#метод выбрать всех пользователей с одинаковым чат айди
async def select_members(message: types.Message):
    members = cur.execute('SELECT tg_id FROM accounts WHERE chatID == {key}'.format(key=message.chat.id)).fetchall()
    return members
    db.commit()