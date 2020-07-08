import turtle

tim = turtle.Turtle()
tim.speed(0)
tim.pensize(7)

rows = 10
columns = 10
radius = 10
spacing = 60
xoffset = -290
yoffset = -275

for y in range(rows):
	for x in range(columns):
		tim.penup()
		tim.goto(xoffset+x*spacing, yoffset+y*spacing)
		tim.pendown()
		tim.color(y/rows, x/columns, 0.5)
		tim.circle(radius*2)

#Click on the screen to close it
turtle.exitonclick() 
