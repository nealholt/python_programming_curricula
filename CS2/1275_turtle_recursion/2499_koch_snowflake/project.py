'''
For 70 points, answer the following questions and write code
to draw a fractal koch snowflake using turtles.

This is not a group project. Help each other, but work alone.
You do not need to turn in a Program Plan.

Read the first two paragraphs of this website then look at the pictures.
en.wikipedia.org/wiki/Koch_snowflake

The following program draws one side of the Koch snowflake.

Investigate this code by:
    1. Running it with and without turtle.tracer(0,0) commented out.
    2. Experimenting with whole number depth values greater than 0

In the koch function, which is the base case and which is the recursive case?

What does the variable t represent?

Your assignment:
    1. Draw an enclosed snowflake. The following code draws one side.
       You need to draw all three. (You may resize the snow flake if you
       want.)
    2. Make at least one creative modification to the snow flake. For
       example, you could experiment with different angles for the bump
       (what if the bump was square? what if the point of the triangular
       bump was pointier?), you could make different parts of the
       snowflake different colors, you could tesselate the snow flake
       across the page or draw snowflakes of different sizes.
'''

import turtle

def koch(t, depth, length, angle):
    if depth <= 0:
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.right(angle*2)
        t.forward(length)
        t.left(angle)
        t.forward(length)
    else:
        koch(t, depth-1, length/4, angle)
        t.left(angle)
        koch(t, depth-1, length/4, angle)
        t.right(angle*2)
        koch(t, depth-1, length/4, angle)
        t.left(angle)
        koch(t, depth-1, length/4, angle)

#Tracer tells the screen not to update until the very end.
#This will greatly speed things up.
#stackoverflow.com/questions/16119991/how-to-speed-up-pythons-turtle-function-and-stop-it-freezing-at-the-end
turtle.tracer(0,0)

#Create a turtle
drawer = turtle.Turtle()
#Variables to control our snowflake
depth = 0
angle = 45
length  = 200
#Move the turtle to the left so we have more room to make a snowflake
drawer.penup()
drawer.goto(-300,0)
drawer.pendown()
#Draw one side of the three sides of the snowflake
koch(drawer, depth, length, angle)

turtle.update()
turtle.done()
