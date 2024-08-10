import os
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()
token = os.getenv("TOKEN")


bot = AsyncTeleBot(token)
