import telebot
import bs4
import requests
import random

def gif_fat_cat():
	'''Парсит ссылки с гифками котов'''
	# Подключаемся к сайту с гифками котов
	res = requests.get('https://tenor.com/search/fat-cat-gifs')
	# Проверяем подключение к сайту 404 - ошибка, 200 - ок
	res.raise_for_status()
	# Скачиваем файл .html и анализируем
	soup = bs4.BeautifulSoup(res.text)
	
	# находит все ссылки с картинками и сохраняет в list
	gifElem = soup.select('img[src]')
	gif_list = []
	
	for i in gifElem:
		gifUrl = i.get('src')
		gif_list.append(gifUrl)
	return gif_list
	
def gif_shark():
	'''Парсит ссылки с гифками котов'''
	# Подключаемся к сайту с гифками котов
	res = requests.get('')
	# Проверяем подключение к сайту 404 - ошибка, 200 - ок
	res.raise_for_status()
	# Скачиваем файл .html и анализируем
	soup = bs4.BeautifulSoup(res.text)
	
	# находит все ссылки с картинками и сохраняет в list
	gifElem = soup.select('img[src]')
	gif_list = []
	
	for i in gifElem:
		gifUrl = i.get('src')
		gif_list.append(gifUrl)
	return gif_list


bot = telebot.TeleBot('токен') # сюда вставить токен


@bot.message_handler(commands=['start'])
def start_message(message):
	'''Принимает команду и отвечает на нее'''
	keyboard = telebot.types.ReplyKeyboardMarkup(True)
	keyboard.row('Привет', '🧱')
	bot.send_message(message.chat.id, 'Привет, я кирпич-бот!', reply_markup=keyboard)
	print(message.chat.username +message.text)


@bot.message_handler(content_types=['text'])
def send_text(message):
	'''Ловит сообщения и отправляет ответ'''
	if 'привет' in message.text.lower():
		bot.send_message(message.chat.id, 'Привет, я 🧱')
	elif 'пока' in message.text.lower():
		bot.send_message(message.chat.id, 'Пока я 🧱, я не умру')
	elif '🧱' in message.text:
		bot.send_message(message.chat.id, '🏭🏭🏭🏭🐨')
	elif 'кот' in message.text:
		bot.send_message(message.chat.id, random.choice(gif_fat_cat()))
	elif 'шарк' in message.text:
		bot.send_message(message.chat.id, random.choice(gif_shark()))
	elif 'шарк' in message.text:
		bot.send_message(message.chat.id, 'https://i.gifer.com/XiPu.gif')
		bot.send_sticker(message.chat.id, 'AMCAgADGQEAA59fuj3rG7YKWtWTLlcAAeIvnlPpl2QAAjwAA0QNzxf-PedQzMHxY06Oyw4ABAEAB20AA2llAAIeBA',)
		

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
	print(message.sticker.file_id)


bot.polling()
