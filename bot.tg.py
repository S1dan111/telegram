import random,telebot,sqlite3
from random import randint

import seconds
from telebot import TeleBot


token = '8470143163:AAHOFKNTjkqG46cV4jHtfHlU11-E5GuHGPg'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    conn = sqlite3.connect("tgbot.sql")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(50), pass varchar(50))")

    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id,"Сейчас тебя зарегестрируем! Введите свое имя")
    bot.register_next_step_handler(message,user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id,"Введите свой пароль")
    bot.register_next_step_handler(message,user_pass)


def user_pass(message):
    password = hash(message.text.strip())
    bot.send_message(message.chat.id,"Отлично,ты зарегестрирован")


    conn = sqlite3.connect("tgbot.sql")
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name,pass) VALUES (\'%s\',\'%s\')' % (name, password))

    conn.commit()
    cur.close()
    conn.close()

    print(name, password)

bot.polling()
