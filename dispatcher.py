import logging
from aiogram import Bot, Dispatcher
import dotenv
import os

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot)