def hacker(a, b):
	#return a + b
	s = a + b
	return s

z=hacker(1, 2)
print(z)
z=hacker('Alex', 'ITFriends')
print(z)

def proz(a, b, c):
	s = a * b * c
	return s
	
z=proz(1, 2, 3)
print(z)

print(proz(1, 2, 3))

def exp(a, b):
	s = a ** b
	return s
	
res = exp(2, 3)
print(res)

import time
def test1(a, b):
	print('-----#test1-------')
	et = time.time()
	res = exp(a, b)
	st = time.time()
	dt = st - et
	print('#test1 time - ', dt)
	print('#test1 res - ', res)

test1(100000, 100000)

