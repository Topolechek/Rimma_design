
import telebot

token = ''
my_id = 443232407
bot = telebot.TeleBot(token)

def send_message(text):
    bot.send_message(my_id, text, parse_mode="Markdown")
