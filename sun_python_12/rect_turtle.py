import turtle

t = turtle.Pen()

def rect(a):
	t.forward(a)
	t.left(120)
	t.forward(a)
	t.left(120)
	t.forward(a)
	t.left(120)

i = 0
while i < 100:
	rect(i)
	i = i + 1


turtle.done()
