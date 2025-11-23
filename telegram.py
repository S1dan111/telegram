
import random,telebot
from random import randint

import seconds
from telebot import TeleBot
import time


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




@bot.message_handler(commands=['pixel'])
def pixel(message):
    bot.send_message(message.chat.id, str(random.randint(1,6)))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет я бот помощник')

@bot.message_handler(commands=['sovet'])
def sovet(message):
    bot.send_message(message.chat.id, random.choice(Sovet_mem))

@bot.message_handler(content_types=['voice'])
def hande_voice(message):
    bot.reply_to(message,"Я пока не умею распозновать голос,напишите текстом")

@bot.message_handler(commands=["timer"])
def set_timer(message):
    try:
        seconds = int(message.text.split()[1])
        if seconds > 300:
            bot.send_message(message.chat.id,"Слишком много,максимум 5 минут")
            return
        bot.send_message(message.chat.id,f"Таймер установлен на {seconds}  секунд")
        time.sleep(seconds)
        bot.send_message(message.chay.id,f"Время вышло")
    except:
        bot.send_message(message.chat.id,f"Чтобы задать таймер используйте команду /timer *время_в_секундах")


citat_coin = [
    'Выпала - решка',
    'Выпал - орёл'
]


@bot.message_handler(commands=['coin'])
def coin(message):
    bot.send_message(message.chat.id, random.choice(citat_coin))





bot.polling()
