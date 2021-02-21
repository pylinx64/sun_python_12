'''
try:
	x = input('Введите число ')
	x = int(x)
	b = input('Введите число ')
	b = int(b)
	print(x / b)
except ZeroDivisionError:
	print('Деление на ноль')
except:	
	print('Введите числа')
'''

import colorama, tqdm, time, random
from colorama import Fore


for x in tqdm.tqdm(range(10), ascii=True, colour='CYAN', desc='Loading game...', bar_format='{desc} {bar} {percentage:3.0f}%', ncols=50):	#range(100) - [0, 1, 2, 3, 4, 5..., 99]
	r = random.uniform(0.01, 0.5)
	time.sleep(r)

colorama.init()
print(Fore.GREEN + 'Vzlom virusa proizoshol')

print(Fore.GREEN + 'A', end='')
print(Fore.CYAN + 'l', end='')
print(Fore.RED + 'e', end='')
print(Fore.MAGENTA + 'x', end='')
