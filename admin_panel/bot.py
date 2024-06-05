# from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import CallbackQuery, Message

token = "5931137819:AAH8NAR-9Lo5OQ1wINa0iR8WDPYXbL2jTos"

bot = telebot.TeleBot(token)

hello_text = '''\
Привет
Сегодня я хочу познакомить тебя с нашими подопечными\
'''


def gen_markup(items):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        *[
            InlineKeyboardButton(item, callback_data=item)
            for item in items
        ]
    )
    return markup


@bot.callback_query_handler(func=lambda call: call.data == "сначала")
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message | CallbackQuery):
    if (type(message) is CallbackQuery):
        message = message.message

    bot.reply_to(
        message,
        hello_text,
        reply_markup=gen_markup(["котята", "собачки"])
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery):
    match(call.data):
        case("котята"):
            bot.send_photo(call.message.chat.id, open("admin_panel/kitten.jpeg", 'rb'), caption="")
            bot.reply_to(
                call.message,
                "смотри какой",
                reply_markup=gen_markup(["сначала"])
            )
        case("собачки"):
            bot.send_photo(call.message.chat.id, open("admin_panel/puppy.jpeg", 'rb'), caption="")
            bot.reply_to(
                call.message,
                "наш крепыш",
                reply_markup=gen_markup(["сначала"])
            )


bot.infinity_polling()
