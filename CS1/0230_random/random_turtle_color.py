'''
For 35 points, create a significant modification to the following
program using both for loops and random colors to draw an interesting
pattern with turtles.
'''
import turtle, random

pen = turtle.Turtle()
pen.speed(0)

#Set the background color of the turtle screen
turtle.bgcolor('black')

#Repeat 100 times
for i in range(100):
    #Get a random amount of red, green, and blue for our turtle's color
    red = random.random()
    green = random.random()
    blue = random.random()

    #Set the turtle's color to this random mixture of colors
    pen.pencolor(red,green,blue)

    #Move forward more each time the loop repeats
    pen.forward(50 + i)
    #Turn a littl more than 90 degrees (a right angle)
    pen.right(90.911)

#Exit the turtle program when the screen is clicked
turtle.exitonclick()
