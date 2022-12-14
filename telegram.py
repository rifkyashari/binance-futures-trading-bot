import os 
import telebot
from binance_client import my_balance

# Balance in string format
balance = 'Current balance : {} USDT'.format(my_balance())

# Bot API KEY 
bot = telebot.TeleBot(os.getenv('api_key_telegram'))

# Message Handler
@bot.message_handler(commands = ['balance'])
def mybalance(message):
    bot.send_message(message.chat.id, balance)

# Keep running script
bot.infinity_polling()