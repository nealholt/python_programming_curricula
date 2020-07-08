
'''For 80 points, write a program using turtle code that writes
your name on the screen.

You must create a different function for each letter of your name.
In other words one function will write N. (See the following example.)

You must create at least 4 functions.

Consider checking out how_to_write_cursive.py in the basic_for_loop
folder before doing this project if you want to get fancy.

You are encouraged to collaborate with your classmates to write all
the letters you need, but you MUST use comments to record who wrote
which functions.
'''
import turtle

def writeN(pen, x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.goto(x,y+100)
    pen.goto(x+100,y)
    pen.goto(x+100,y+100)

t = turtle.Turtle()
writeN(t, 0,0)
turtle.done()
