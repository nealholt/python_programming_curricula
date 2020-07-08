
'''The following python program contains a function called
drawCircle that uses the given turtle to draw a circle of the
given color and size at the given x,y coordinates.

For 35 points, write a different function that draws a 
particular shape and call the function to draw the shape on the 
screen.

'''

import turtle

def drawCircle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(2)

drawCircle(tommy, "green", 50, 25, 0)

drawCircle(tommy, "blue", 50, 0, 0)

drawCircle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)

turtle.done()
