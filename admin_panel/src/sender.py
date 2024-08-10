from telebot.util import quick_markup

from src.bot import bot


async def send_message(
    chat_id: int,
    text: str,
    buttons: list[str] = []
) -> None:
    markup = quick_markup(
        {button: {'callback_data': button} for button in buttons}
    )
    await bot.send_message(chat_id, text, reply_markup=markup)
