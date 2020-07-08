
'''Use the following lines of code to draw a single blue line
straight up from the bottom of the screen.
When you are done, the turtle should not be visible. just the line.
You may need more code than is given. You may need certain lines
more than once. You may not need some lines at all.'''

#Import the turtle code
import turtle
#Create a new turtle named t
t = turtle.Turtle()
#Every turtle drags a pen behind it. This tells turtle t to lift the pen
#so t will no longer draw when it moves.
t.penup()
#Tell turtle t to put its pen back down. After this it will draw when it moves
t.pendown()
#Erase everything drawn by t
t.clear()
#Turn t to a heading of 90 degrees.
t.setheading(90)
#Move t forward 10 steps
t.forward(10)
#Move t backward 10 steps
t.backward(10)
#Move t to a particular location given as an x,y coordinate.
t.goto(50,-100)
#Tell t to disappear. Other shape options include: “arrow”, “turtle”, “circle”,
#“square”, “triangle”, and “classic”
t.shape(None)
#Change t's color to "brown". Other common named colors will also work: "red",
#"blue", "green", "yellow", etc.
t.color("brown")
#Set the thickness of t's pen. 1 is narrow. 10 is thicker. You can make it
#even thicker. I'm not sure what the limit is.
t.pensize(10)
#Tell the turtle code you are done so it lets you close the window.
turtle.done()
