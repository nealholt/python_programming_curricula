
'''This is not an investigation or project, just some pieces
of example code to help you draw curves or write cursive.'''

import turtle

t = turtle.Turtle()
t.pensize(4)
t.speed(0)

#EXAMPLE 1: BLACK
angle = 3
side_length = 3
for i in range(50):
    t.forward(side_length)
    t.left(angle)

#EXAMPLE 2: GREEN
t.penup()
t.goto(-200,0)
t.pendown()
t.color('green')
angle = 0.1
side_length = 14
for i in range(100):
    t.forward(side_length)
    t.left(angle)
    angle = angle+0.1

#EXAMPLE 3: BLUE
t.penup()
t.goto(-100,0)
t.pendown()
t.color('blue')
angle = 5
side_length = 3
for i in range(120):
    t.forward(side_length)
    t.left(angle)
    angle = angle-0.1

#EXAMPLE 4: red
t.penup()
t.goto(100,0)
t.pendown()
t.color('red')
angle = 5
side_length = 0
for i in range(100):
    t.forward(side_length)
    t.left(angle)
    side_length = side_length+0.1

#EXAMPLE 5: YELLOW
t.penup()
t.goto(100,100)
t.pendown()
t.color('yellow')
angle = 5
side_length = 4
for i in range(100):
    t.forward(side_length)
    t.left(angle)
    side_length = side_length-0.1

#EXAMPLE 6: ORANGE
t.penup()
t.goto(-200,-100)
t.pendown()
t.color('orange')
angle = 3
side_length = 5
pen_size = 1
t.pensize(pen_size)
for i in range(100):
    t.forward(side_length)
    t.left(angle)
    pen_size = pen_size+0.2
    t.pensize(pen_size)

turtle.done()
