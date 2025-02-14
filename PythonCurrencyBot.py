import telebot
import buttons
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.from_user.id
    user_firstname = message.from_user.first_name
    user_username = message.from_user.username
    print(user_id, user_firstname, user_username)
    bot.send_message(chat_id=user_id,
                     text=f'Welcome to Currency Exchange bot!',
                     reply_markup=buttons.button())
    bot.register_next_step_handler(message, text)


def text(message, exchange=None):
    user_id = message.from_user.id
    if message.text == 'Back':
        start_bot(message)
    elif message.text or exchange == 'UZS > USD($)':
        bot.send_message(user_id, f'Type in UZS amount', reply_markup=buttons.back_btn())
        bot.register_next_step_handler(message, convert_uzs_to_usd, user_id)

    elif message.text or exchange == 'USD($) > UZS':
        bot.send_message(user_id, 'Type in USD amount', reply_markup=buttons.back_btn())
        bot.register_next_step_handler(message, convert_usd_to_uzs, user_id)


def convert_uzs_to_usd(message, user_id):
    if message.text.isdigit():
        uzd_amount = float(message.text) / 12648.00
        bot.send_message(message.chat.id,
                         f"UZS: {float(message.text):.2f}  > USD: ${uzd_amount:.2f}",
                         reply_markup=buttons.back_btn(qwe=2))
        bot.register_next_step_handler(message, text, exchange="UZS > USD($)")

    elif message.text == 'Back':
        start_bot(message)
    else:
        bot.send_message(user_id, "Please type a valid number.")
        bot.register_next_step_handler(user_id, text)


def convert_usd_to_uzs(message):
    user_id = message.from_user.id
    if message.text.isdigit:
        uzs_amount = float(message.text) * 12648.75
        bot.send_message(message.chat.id,
                         f"USD: ${float(message.text):.2f}  >  UZS: {uzs_amount:.2f}",
                         reply_markup=buttons.back_btn(qwe=2))

        bot.register_next_step_handler(message, text, exchange='USD($) > UZS')

    elif message.text == 'Back':
        start_bot(message)

    else:
        bot.send_message(user_id, "Please type a valid number.")
        bot.register_next_step_handler(message.chat.id, convert_usd_to_uzs)


bot.infinity_polling()
