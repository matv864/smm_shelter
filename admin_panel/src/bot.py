import os
from telebot.async_telebot import AsyncTeleBot


token = os.getenv("token")

bot = AsyncTeleBot(token)
