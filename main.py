from settings.local_settings import TELEGRAM_TOKEN
import telebot
from settings import *
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'hello world')
    
bot.polling()