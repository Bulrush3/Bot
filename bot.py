import telebot
import config

from telebot import types
bot = telebot.TeleBot(config.TOKEN)

word = ''
user_result = None
file = open('days.txt')
text3 = file.read()

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Как дела?")
    item2 = types.KeyboardButton("Найти слово")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name} ".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types =['text'])
def lala(message):
    # keyboard
    if message.chat.type == 'private':
        if message.text == 'Как дела?':
            bot.send_message(message.chat.id, 'Всё заебись')
        elif message.text == 'Найти слово':
            msg = bot.send_message(message.chat.id, 'Введите слово:')
            bot.register_next_step_handler(msg, process_1)
        else:
            bot.send_message(message.chat.id, 'Чего???')

def process_1(message, user_result = None):
        word = message.text
        if word in text3:
            msg = bot.send_message(message.chat.id, 'Такое слово есть')
        else:
            msg = bot.send_message(message.chat.id, 'Слово отсутствует')

bot.polling(none_stop=True)
