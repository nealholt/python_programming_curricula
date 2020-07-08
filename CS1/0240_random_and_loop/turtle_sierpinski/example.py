import turtle, random

x1 = 0
y1 = 300

x2 = -300
y2 = -200

x3 = 200
y3 = -300

tim = turtle.Turtle()
tim.speed(0)
tim.pensize(2)

x=0
y=0

radius = 2

while True:
	r = random.random()
	if r<0.3333:
		x = (tim.xcor()+x1)/2
		y = (tim.ycor()+y1)/2
	elif r<0.6666:
		x = (tim.xcor()+x2)/2
		y = (tim.ycor()+y2)/2
	else:
		x = (tim.xcor()+x3)/2
		y = (tim.ycor()+y3)/2
	tim.penup()
	tim.goto(x, y-radius)
	tim.pendown()
	tim.circle(radius*2)
