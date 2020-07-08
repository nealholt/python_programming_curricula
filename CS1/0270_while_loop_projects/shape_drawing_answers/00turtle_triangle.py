'''
Start by reading and running the following code
to see what it does.

1. Then rewrite this code so that it uses a for loop.
Challenge yourself to make the rewrite as short as
possible.
2. Modify your code to draw a square instead of a triangle.
3. Modify your code to draw a pentagon. (You should Google
what angles are needed if you can't otherwise figure them
out.)
4. Create a function that takes two arguments: a turtle
and a number of sides, like this:
def drawShape(my_turtle, sides):
Put code inside your function that draws a regular shape
with as many sides as the variable "sides" using my_turtle.
'''

import turtle

tommy = turtle.Turtle()

tommy.speed(1)
tommy.pendown()
tommy.color('green')

tommy.forward(100) #Move forward 100 pixels
tommy.left(120) #Turn left 120 degrees

tommy.forward(100)
tommy.left(120)

tommy.forward(100)
tommy.left(120)

turtle.done()