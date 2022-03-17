import os

from flask import Flask, request

import telebot

TOKEN = '5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands = ['start'])
def start(message):
  bot.send_message(message.chat.id, 'чем я могу помочь?')
  img = open("z.jpg", 'rb')
  bot.send_photo(message.chat.id, img)
  img.close()
  keyboard = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text='Аниме', callback_data='first_1')
  button2 = types.InlineKeyboardButton(text='Космос', callback_data='first_2')
  keyboard.add(button1)
  keyboard.add(button2)
  bot.send_message(message.chat.id, text="Выбери тематику фото", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('first'))
def query_handler(call):
  bot.answer_callback_query(callback_query_id=call.id) 
  if call.data == 'first_1':
      img = open("a.jpg", "rb")
      bot.send_photo(call.message.chat.id, img)
      img.close()
  elif call.data == 'first_2':
      img = open("b.jpg", "rb")
      bot.send_photo(call.message.chat.id, img)
      img.close()
      
      
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telebot2241.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
