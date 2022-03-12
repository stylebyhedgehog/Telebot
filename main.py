import telebot
import os
from flask import Flask, request

bot = telebot.TeleBot("5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ")
server = Flask(__name__)

@bot.message_handler(commands = ['start'])
def start(message):
  bot.send_message(message.chat.id, 'чем я могу помочь?')

@bot.message_handler(content_types = ['text'])
def texta(message):
  if message.text == "Привет":
    bot.send_message(message.chat.id, 'Ну привет')
  elif message.text == "Пока":
    bot.send_message(message.chat.id, 'BBBBBBBB')
  elif message.text == "/test" or "/help":
    bot.send_message(message.chat.id, 'Вы использовали команду /test')

@server.route('/' + "5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-new-new.herokuapp.com/' + "5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ")
    return "!", 200


if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
