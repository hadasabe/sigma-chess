from cfg import *
import telebot


@BOT_TOKEN.message_handler(commands=['start'])
def start(message):
    BOT_TOKEN.send_message(message.chat.id, 'Вас приветствует бот сайта sigmachess, нажмите на команду, '
                                            'которую я должен выполнить!')


BOT_TOKEN.polling(none_stop=True)
