
'''This is not an investigation, just some examples of a few more
things you can do with the turtle code including:
-Making the turtle respond to mouse clicks.
-Closing the turtle window when a particular key is pressed.'''

#Source: stackoverflow.com/questions/19782256/python-turtle-after-drawing-click-mouse-clear-screen-and-redraw
import turtle

#Create a variable named window that refers to the turtle screen.
window = turtle.Screen()

'''Create a new function that draws a square at the given
x,y coordinates'''
def draw(x, y): # x, y are mouse position arguments passed by onclick()
	#Create a new turtle
    pen = turtle.Turtle()
	#Hide the shape of the turtle
    pen.hideturtle()

	#Prepare to draw a square
    print(x,y)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

	#Draw a square
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)

'''Register the draw function so that whenever the screen is clicked,
the draw function gets called.'''
window.onclick(draw)

'''Register the q key to cause the window to close.'''
window.onkey(window.bye, "q")

'''Begin listening to events like key press & mouse clicks.'''
window.listen()
window.mainloop()
