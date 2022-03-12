import telebot
import os
from flask import Flask, request


bot = telebot.TeleBot("5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ")

server = Flask(__name__)


@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, 'чем я могу помочь?')


@server.route('/' + "5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telebot2241.herokuapp.com/' + tokenBot.TOKEN)
    return "!", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
