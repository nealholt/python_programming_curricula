import turtle, math

tommy = turtle.Turtle()

tommy.penup()
tommy.goto(-400, 0)
tommy.pendown()
tommy.color('green')
i = -400
while i < 400:
	tommy.goto(i, 100*math.sin(i/10.0))
	i = i+1

turtle.done()