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


async def select_eventName(numberID_event):
    event_name = cur.execute("SELECT name FROM event WHERE id == {key}".format(key=numberID_event)).fetchone()
    db.commit()
    for name in event_name:
        return name


async def select_eventDescription(numberID_event):
    event_name = cur.execute("SELECT description FROM event WHERE id == {key}".format(key=numberID_event)).fetchone()
    db.commit()
    for name in event_name:
        return name


async def select_dateEvent(numberID_event):
    dateEvent = cur.execute("SELECT date FROM event WHERE id == {key}".format(key=numberID_event)).fetchone()
    db.commit()
    return dateEvent

async def update_dateEvent(now, numberID_event):
    cur.execute("UPDATE event SET date = ? WHERE id = ?", (now, numberID_event))
    db.commit()

async def takeIsActive(numberID_event):
    isActive = cur.execute("SELECT isActive FROM event WHERE id == {key}".format(key=numberID_event)).fetchone()
    db.commit()
    for active in isActive:
        return active\

async def updateIsActive(newActive, numberID_event):
    isActive = cur.execute("UPDATE event SET isActive == {newActive} WHERE id == {key}".format(newActive=newActive, key=numberID_event)).fetchone()
    db.commit()