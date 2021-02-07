import requests
import bs4
import random

def meme_random_gif():
    '''Функция которая находит рандомную с gif котом'''
    res = requests.get('C:/Users/User/Documents/alex_python/kolegi.html')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    gifElem = soup.select('img[src]')
    gif_list = []
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)
    gif_random = random.choice(gif_list)
    return gif_random
    
memeGif = meme_random_gif()
print(memeGif)
