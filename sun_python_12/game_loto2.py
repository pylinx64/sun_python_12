import random 
import time 

list_1 = ['House', 'PS5', 'Minecraft', 'Кирпич', 'Баклажан', 'Tesla Model X']
money = 21
i = 0.5		# time FPS 
print('-> Приветсвую тебя в рулетке.net')
time.sleep(i)


list_win = []
for x in range(1000):
	t = random.choice(list_1)
	list_win.append(t)
print(list_win)


while True:
	if money < 5:
		print('-> Error: money = 0')
		time.sleep(i)
		break
	else:
		win = random.choice(list_win)
		print('-> GameModeWin = True: you win ', win)
		time.sleep(i)
		money = money - 5
		print('-> MoneyWork - 5 $: True')
		time.sleep(i)
		
