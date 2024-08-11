from telebot.util import quick_markup

from src.bot import bot


async def send_message(
    chat_id: int,
    text: str,
    buttons: list[tuple[str, str]] = []
) -> None:
    markup = quick_markup(
        {button[0]: {'callback_data': button[1]} for button in buttons}
    )
    await bot.send_message(chat_id, text, reply_markup=markup)
