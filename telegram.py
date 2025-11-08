
import random

import  telebot

token = '8470143163:AAHOFKNTjkqG46cV4jHtfHlU11-E5GuHGPg'
bot = telebot.TeleBot(token)


Sovet_mem= [
    "Главный мем года - 67",
    "Тут вам не там,там вам не тут",
    "Я тут босс",
    "Главное думать только о себе",
    "Хочешь трудиться - иди трудись",
    "Андроид и Айфон- 2 разные вещи",
    "Нельзя сравнить макбук и виндовс",
    "у виво лучшие шайбы."
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет я бот помощник')

@bot.message_handler(commands=['sovet'])
def sovet(message):
    bot.send_message(message.chat.id, random.choice(Sovet_mem))



bot.polling()
