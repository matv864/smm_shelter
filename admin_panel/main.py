import asyncio
from dotenv import load_dotenv

from src.bot import bot
from src.receiver import (
    recieve_all_messages,
    recieve_all_callbacks
)


load_dotenv()

asyncio.run(bot.polling())
