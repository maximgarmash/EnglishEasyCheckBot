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
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route('/', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

#
# @app.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
#     return "!", 200


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