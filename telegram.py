import telebot

token = '8470143163:AAHOFKNTjkqG46cV4jHtfHlU11-E5GuHGPg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет я бот помощник')

bot.polling()    
