import turtle

red = turtle.Turtle()
red.shape("turtle")
red.speed(0)
red.pendown()
red.color('red')
red.goto(0,0)
red.setheading(90)
red.pensize(4)

blue = turtle.Turtle()
blue.shape("turtle")
blue.speed(0)
blue.pendown()
blue.color('blue')
blue.goto(-4,0)
blue.setheading(90)
blue.pensize(4)

yellow = turtle.Turtle()
yellow.shape("turtle")
yellow.speed(0)
yellow.pendown()
yellow.color('yellow')
yellow.goto(-8,0)
yellow.setheading(90)
yellow.pensize(4)

green = turtle.Turtle()
green.shape("turtle")
green.speed(0)
green.pendown()
green.color('green')
green.goto(-16,0)
green.setheading(90)
green.pensize(4)

sides = 180 #Change this to change the shape! Lots of sides makes a circle
angle = 360/sides #Calculate the angle you need to turn to make a regular shape with the given number of sides.
side_length = 600/sides #shorten the side length when there are more sides

#Introduce an even more appropriate loop to shorten our code:
for i in range(int(sides/2)): #Move over half a circle not a full circle
	red.forward(side_length)
	red.left(angle)
	blue.forward(side_length-0.2) #Shorten forward movement for interior arcs
	blue.left(angle)
	yellow.forward(side_length-0.4) #Shorten forward movement for interior arcs
	yellow.left(angle)
	green.forward(side_length-0.8) #Shorten forward movement for interior arcs
	green.left(angle)

turtle.done()