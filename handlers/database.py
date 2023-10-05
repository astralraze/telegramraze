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