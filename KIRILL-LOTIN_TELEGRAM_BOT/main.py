import telebot
from translator import to_cyrillic, to_latin

TOKEN = "your bot token" #----> You can get bot token from @botFather in telegram 
bot = telebot.TeleBot(token=TOKEN)

#for getting  \start  command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username # username of user
    message_send = 'Hi I can convert your text to latin or cyrill text! \nSend me text!'
    bot.send_message(message.chat.id, message_send)

# function for getting messages of user send
@bot.message_handler(func=lambda msg: msg.text is not None)

def translit(message):
    msg = message.text
    message_answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, message_answer(msg))
    

bot.polling()
