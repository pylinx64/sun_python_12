import bs4
import requests

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
	

