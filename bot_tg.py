from cfg import *
import telebot
from telebot import types
import random
import os

f = False


@BOT_TOKEN.message_handler(commands=['start'])
def start(message):
    BOT_TOKEN.send_message(message.chat.id, 'Вас приветствует бот сайта sigmachess, нажмите на команду, '
                                            'которую я должен выполнить! /help - для списка команд')


@BOT_TOKEN.message_handler(commands=['help'])
def help(message):
    text = ('\n/help - список команд'
            '\n/daily - задача дня'
            '\n/profile - профиль'
            '\n/start_game - ссылка на игру под определённым кодом'
            '\n/debut'
            '\n/')
    BOT_TOKEN.send_message(message.chat.id, text)


@BOT_TOKEN.message_handler(content_types=['text'])
def great(message):
    global f
    if message.text == '/daily':
        f = True
        BOT_TOKEN.send_message(message.chat.id, 'рассылка включена')
    if message.text == '/profile':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("жмяк", url='https://sigma-chess.com')
        markup.add(button1)
        BOT_TOKEN.send_message(message.chat.id,
                               "Cайт твоего профиля)".format(message.from_user),
                               reply_markup=markup)
    if message.text == '/start_game':
        code = 'pass'
        BOT_TOKEN.send_message(message.chat.id, f'{code}')  # новая игра, Миша sql табла


BOT_TOKEN.polling(none_stop=True)
