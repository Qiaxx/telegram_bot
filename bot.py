import utils
import telebot
from telebot import types

bot = telebot.TeleBot('6917585855:AAGbKQ2bH3EtCJ8tPl-mUlvw6JCisRs_vxU', parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name is not None:
        bot.send_message(message.chat.id,
                         f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>\n'
                         f'Я умею присылать курс рубля', parse_mode='html')
    else:
        bot.send_message(message.chat.id,
                         f'Привет, <b>{message.from_user.first_name}</b>\n'
                         f'Я умею присылать курс рубля', parse_mode='html')


@bot.message_handler(commands=['currency'])
def currency(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in utils.get_all_currency():
        markup.add(types.KeyboardButton(item))
    bot.send_message(message.chat.id, 'Введите курс который хотите узнать (USD, EUR)', reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def get_currency(mess):
        if mess.text in utils.get_all_currency():
            bot.send_message(mess.chat.id, f'{utils.main(mess.text)}')
        else:
            bot.send_message(mess.chat.id, 'Такой валюты нет')

bot.polling(none_stop=True)
