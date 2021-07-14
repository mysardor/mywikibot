from settings.local_settings import TELEGRAM_TOKEN
from settings import *
import requests
import telebot

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'hello world')
    
@bot.message_handler(commands=['help'])
def searching(message):
    bot.reply_to(message,'Write down what to look for.')

@bot.message_handler(content_types=['text'])
def message_text(message):
    response = requests.get('https://en.wikipedia.org/w/api.php', {
        'action' : 'opensearch',
        'search' : message.text,
        'limit' : 1,
        'namespace' : 0,
        'format' : 'json'
    })
    result = response.json()
    link = result[3]
    if link:
        bot.reply_to(message,"Link on your request: " + link[0])
    else:
        bot.reply_to(message,"There is nothing on your request")

bot.polling()