import turtle
import time

t = turtle.Pen()
turtle.bgcolor('black')
colors = ['#AF69FF', '#800080', '#00F700', '#00ECF7', '#BFBFBF']

for i in range(100):
	t.pencolor(colors[i%5])
	t.forward(i)
	t.left(67)


time.sleep(100)
