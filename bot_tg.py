from cfg import *
import telebot
from telebot import types
import random
import datetime
import glob
import time

f = False


@BOT_TOKEN.message_handler(commands=['start'])
def start(message):
    BOT_TOKEN.send_message(message.chat.id, 'Вас приветствует бот сайта sigmachess, нажмите на команду, '
                                            'которую я должен выполнить! /help - для списка команд')
    print(message.chat.id)


@BOT_TOKEN.message_handler(commands=['help'])
def help(message):
    text = ('\n/help - список команд'
            '\n/daily - задача дня'
            '\n/profile - профиль'
            # '\n/start_game - ссылка на игру под определённым кодом'
            '\n/debut - случайный дебют'
            '\n/info - информация о разработчиках и разработке'
            '\n/cube - бросить шестигранный кубик')
    print(message.chat.id)
    BOT_TOKEN.send_message(message.chat.id, text)


@BOT_TOKEN.message_handler(commands=['info'])
def info(message):
    BOT_TOKEN.send_message(message.chat.id, f'Ссылка на сайт: {"pass"} \nСсылка на гитхаб: {"pass"} ')


@BOT_TOKEN.message_handler(commands=['cube'])
def cube(message):
    BOT_TOKEN.send_dice(message.chat.id, emoji='🎲').dice.value


@BOT_TOKEN.message_handler(commands=['debut'])
def debut(message):
    a = open(f'debuts/debut{random.randint(1, len(glob.glob("debuts/*")))}.txt', 'r')
    BOT_TOKEN.send_message(message.chat.id, a)


@BOT_TOKEN.message_handler(commands=['daily'])
def daily(message):
    global f
    a = open('id.txt', 'a+')
    a1 = open('id.txt', 'r')
    g = [i for i in a1.read().split('\n')]
    if not f:
        if message.chat.id not in g:
            BOT_TOKEN.send_message(message.chat.id, 'рассылка включена')
            f = True
            print(message.chat.id, file=a)
            print(message.chat.id)
        if datetime.datetime.now().strftime("%H:%M:%S") == '00:00:00' or message.chat.id == 1262754010:
            for i in g:
                BOT_TOKEN.send_message(i, 'Задача дня:')
                BOT_TOKEN.send_photo(i, open('daily.png', 'rb'))
    else:
        BOT_TOKEN.send_message(message.chat.id, 'рассылка выключена')
        f = False


@BOT_TOKEN.message_handler(content_types=['text'])
def great(message):
    if message.text == '/profile':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("жмяк", url='https://sigma-chess.com')  # с Миши
        markup.add(button1)
        BOT_TOKEN.send_message(message.chat.id,
                               "Cайт твоего профиля)".format(message.from_user),
                               reply_markup=markup)
    if message.text == '/start_game':
        code = 'pass'
        BOT_TOKEN.send_message(message.chat.id, f'{code}')  # новая игра, Миша sql табла


BOT_TOKEN.polling(none_stop=True)
