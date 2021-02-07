print("Hello world")						# функция							


x = 10										# Переменная число
print(x)
text = 'Hello'								# Переменная строка
answer = True 								# Переменная логика
v_list = ['potato', 'apple', 'kirpich']		# Переменая список


for element in v_list:						# Цикл for in  для списка				
	print(element)

i = 0										# счетчик
while i < len(v_list):						# Цикл while для списка
	print(v_list[i])
	i += 1									# инкреминтация (увеличение на 1)
	

import random								# импортируем библиотеку
r = random.randint(0, 5)					# используем библиотеку

											# условия/проверка
if r == 0:									# если						
	print('OK')								# работает если проверка True	
elif r == 1:								# тоже если	
	print('ne OK')
else:										# иначе (если не сработало)
	print('...')
