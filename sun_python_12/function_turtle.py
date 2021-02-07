import turtle 

colors = ['#7FFF1B', '#1BECFF', '#FF1BF8']
t=turtle.Pen()


def side(tangle=120, lenth=100, number_color=2):
	t.pencolor(colors[number_color])
	t.forward(lenth)
	t.left(tangle)

side(120, 100, 2)


turtle.done()
