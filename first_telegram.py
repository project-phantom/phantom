import telebot
from config import TOKEN 
"""[summary]

message.chat.id  user_id or group_id
message.message_id id when user sends a msg
message.text msg content

send_message(message.chat.id, text)
send_message(message.chat.id, text, reply_to_message_id=message.message_id, **kwargs)
"""

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Welcome')

@bot.message_handler()
def echo(message):
	bot.reply_to(message, message.text)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'How can I help you?')
# def send_welcome(message):
# 	bot.send_message(reply_to_message_id=message.message_id, char_id = message.chat.id, text="I'm here to help!")


if __name__ == '__main__':
	bot.polling()