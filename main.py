from flask import Flask
from flask import request
from flask import jsonify
import telebot
# from flask_sslify import SSLify
import requests
import json
import constants
import re


app = Flask(__name__)
bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('/start', '/stop')
        user_markup.row('фото', 'аудио', 'документы')
        user_markup.row('стикер', 'видео', 'голос', 'локация')
        bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)


@app.route('/', methods=['POST', 'GET'])
def index()


    # @bot.message_handler(commands=['start'])
    # def handle_start(message):
    #     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    #     user_markup.row('/start', '/stop')
    #     user_markup.row('фото', 'аудио', 'документы')
    #     user_markup.row('стикер', 'видео', 'голос', 'локация')
    #     bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

    return '<h1>EnglishEasyCheckBot welcomes you<h1>'


if __name__ == "__main__":
    app.run()
#
# filename = 'english-module.txt'
#
# eng_dict = {}
# with open(filename, 'r', encoding='utf-8') as file:
#     for line in file.read().splitlines():
#         eng_dict[line.split('\t')[0]] = line.split('\t')[1]
# print(eng_dict)




# import fleep
    # info = fleep.get(f.read(128))
#
# print(info.type)
# print(info.extension)
# print(info).mime)
#
# print(info.type_matches("raster-image"))
# print(info.extension_matches("gif"))
# print(info.mime_matches("image/png"))