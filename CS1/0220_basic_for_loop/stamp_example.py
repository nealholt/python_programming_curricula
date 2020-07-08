import turtle

'''You can create a "stamp" of your turtle's shape on the screen
using the stamp command.'''
pen = turtle.Turtle()
pen.penup()

for i in range(30, -1, -1): #Count down from 30
    pen.stamp() #STAMP
    pen.left(i)
    pen.forward(20)

#Clear with this:
#clearstamps()

turtle.done()