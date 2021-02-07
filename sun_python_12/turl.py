import turtle
import time

colors = ['lime', 'yellow', '#5DE9D8', '#AC61CB', '#CB616C']
t = turtle.Pen()
turtle.bgcolor('black')

def side():
	t.pencolor(colors[0])
	t.write('''............(\_/)
~..... #####(.)(.)
......\#####/( * )
.......||\\""||||
.......*..*.*.''')
	t.penup()
	t.forward(80)
	t.pendown()
	t.left(62)

i = 0
while i < 6:
	side()
	i = i + 1



time.sleep(100)
