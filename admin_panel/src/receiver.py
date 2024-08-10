from telebot.types import Message, CallbackQuery

from src.bot import bot
from src.developer import developer
from src.admin import admin_helper
from src.sender import send_message


@bot.callback_query_handler(func=lambda call: True)
async def recieve_all_callbacks(call: CallbackQuery):
    await common_handler(
        chat_id=call.message.chat.id,
        username=call.from_user.username,
        message_text=call.data
    )


@bot.message_handler(func=lambda message: True)
async def recieve_all_messages(message: Message):
    await common_handler(
        chat_id=message.chat.id,
        username=message.from_user.username,
        message_text=message.text
    )


async def common_handler(chat_id: int, username: str, message_text: str):
    if await developer.is_it_admin(username):
        await admin_helper(chat_id, username, message_text)
    elif await developer.is_it_developer(username):
        await send_message(
            chat_id,
            await developer.command_from_developer(message_text)
        )
    else:
        await send_message(chat_id, "I don't know you")
