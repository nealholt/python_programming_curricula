import turtle, time

#Create and name a variable for the tracer
jimbo = turtle.Turtle()
jimbo.shape("arrow")

jimbo.penup()
jimbo.speed(600)
jimbo.color(0,0,1)
jimbo.goto(-400,-400)
jimbo.setheading(90)



x_co = int(-400)

for i in range(800):
	jimbo.pendown()
	jimbo.color(0,1,i/799)
	jimbo.goto(x_co,400)
	jimbo.goto(x_co,-400)
	x_co = (x_co + 1)