import turtle

colors = ['#DA37A0', '#418DDD', '#19E7E4', '#6EE719', '#FBF759', '#FB59D1']
t = turtle.Pen()
turtle.bgcolor('black')

t.penup()

sides = int(turtle.numinput('Подсказка 1', 'Введите кол-во спиралей: ', 4, 2, 6))

