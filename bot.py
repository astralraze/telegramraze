import asyncio
import logging
import os
import sys
from os import getenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from handlers.playgame import router
from handlers.registration import router_reg
from handlers.filter_text import router_filter
from handlers.games import games_rtr
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv
from handlers import database as db



load_dotenv()

async def main():
    bot = Bot(token=os.environ.get('TOKEN'), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(router_reg)
    dp.include_router(games_rtr)
    dp.include_router(router_filter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())