from cfg import *
import telebot


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
            '\n'
            '\n')
    BOT_TOKEN.send_message(message.chat.id, text)


@BOT_TOKEN.message_handler(commands=['daily'])
def daily(message):
    photo = open('daily.png', 'rb')
    BOT_TOKEN.send_photo(message.chat.id, photo)


@BOT_TOKEN.message_handler(content_types=['text'])
def profile(message):
    if message.text == '/profile':
        BOT_TOKEN.send_message(message.chat.id, 'Вы зарегестрированны?')
        text1 = ''
        flag = False
        if message.text == 'да':
            profile_user(message.from_user.id)
        if message.text == 'нет':
            text1 = 'Ссылка для регестрации: '
            BOT_TOKEN.send_message(message.chat.id, text1)

    # def profile_user(message):
    #    BOT_TOKEN.send_message(message.chat.id, 'писька')


@BOT_TOKEN.message_handler(content_types=['text'])
def start_game(message):
    if message.text == '/start_game':
        BOT_TOKEN.send_message(message.chat.id, 'код игры') #  {123}


def get_id(id):
    pass


def profile_user():
    print(123)


BOT_TOKEN.polling(none_stop=True)
