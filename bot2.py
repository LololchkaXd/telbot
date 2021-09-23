import telebot
import wakeonlan
import os, sys
from subprocess import Popen
from telebot import types
import random


from telebot import types
bot = telebot.TeleBot('1815443211:AAE6T7nIjb-wJH4C16pHZvN4kr960Jf4nnY')


@bot.message_handler(commands=['help', 'wake'])
def send_welcome(message):
   msg = bot.send_message(message.chat.id, 'Привет! Я codex_bot!')


@bot.message_handler(commands=['setatus', 'item2'])
def run_block(run):
    p = Popen('D:\scripts\Telegrambot\test.py')
    msg = bot.send_message(run.chat.id, '')
    
            

@bot.message_handler(commands=['run', 'item1'])
def read_blocked(wake):
    b = Popen('/home/ec2-user/Telebot/login2.py')
    bot.send_message(wake.chat.id, 'Сервер запущен')



 
if __name__ == "__main__":
    bot.polling()   
