import telebot
from config import TOKEN 
import requests
import json
import time
import urllib

"""[summary]

message.chat.id  user_id or group_id
message.message_id id when user sends a msg
message.text msg content

send_message(message.chat.id, text)
send_message(message.chat.id, text, reply_to_message_id=message.message_id, **kwargs)
"""
class Commands():
	get_me = '/getme'
	get_update = '/getUpdates'

def get_url(url):
	response = requests.get(url)
	content = response.content.decode('utf-8')
	return content 

def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js

def get_update(offset):
	url = 'https://api.telegram.org/bot{}{}?timeout=100'.format(TOKEN, Commands.get_update) 
	# content = requests.get(url).text
	if offset:
		url += '&offset={}'.format(offset)
	js = get_json_from_url(url)
	return js

def get_last_chat_id_and_text(updates):
	update_ids = []
	for update in updates['result']:
		update_ids.append(int(update['update_id']))

	return max(update_ids)

def echo_all(updates):
	for update in updates['result']:
		try:
			text = update['message']['text']
			chat = update['message']['chat']['id']
			server_reply_msg(text, chat)
		except Exception as e:
			print(e)
	# num_update = len(updates['result'])
	# last_update = num_update - 1
	# text = updates['result'][last_update]["message"]["text"]
	# chat_id = updates['result'][last_update]["message"]["chat"]["id"]
	# return (text, chat_id)

def server_reply_msg(text):
	text = urllib.parse.quote_plus(text)
	reply_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(TOKEN, 421392046, text)

	get_url(reply_url)

def main():
	last_text = (None, None)
	last_update_id = None

	while True:
		updaes = get_update(last_update_id)
		if len(updates['result']) > 0:
			last_update_id = get_last_chat_id_and_text(updates) + 1
			echo_all(updates)

		# text, chat = get_last_chat_id_and_text(get_update())
		# if (text, chat) != last_text:
		# 	last_text = (text, chat)
			## server_reply_msg(text, chat)
		time.sleep(0.5)

	server_reply_msg('Hello back')


if __name__ == '__main__':
	main()



# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.send_message(message.chat.id, 'Welcome')

# @bot.message_handler()
# def echo(message):
# 	bot.reply_to(message, message.text)

# @bot.message_handler(commands=['help'])
# def send_welcome(message):
# 	bot.send_message(message.chat.id, 'How can I help you?')
# # def send_welcome(message):
# # 	bot.send_message(reply_to_message_id=message.message_id, char_id = message.chat.id, text="I'm here to help!")


# if __name__ == '__main__':
# 	bot.polling()