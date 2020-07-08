import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed(0)
timmy.pensize(4)

sides = 180 #Change this to change the shape! Lots of sides makes a circle
angle = 360/sides #Calculate the angle you need to turn to make a regular shape with the given number of sides.
side_length = 600/sides #shorten the side length when there are more sides

#List of colors in order.
#This will let us greatly shorten the code!
roygbiv = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

count = 0

#Use an outer for loop to loop over the colors
for color in roygbiv:
	timmy.penup()
	timmy.color(color)
	timmy.goto(-4*count, 0)
	timmy.setheading(90)
	timmy.pendown()
	#Introduce an even more appropriate loop to shorten our code:
	for i in range(int(sides/2)): #Move over half a circle not a full circle
		timmy.forward(side_length-0.15*count)
		timmy.left(angle)
	count = count + 1

turtle.done()