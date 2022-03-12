import telebot
bot = telebot.TeleBot("5272849059:AAFcpFbq-C3sJW4lju1CX00S2c9CEbDM4vQ")


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

bot.polling(none_stop = True)
