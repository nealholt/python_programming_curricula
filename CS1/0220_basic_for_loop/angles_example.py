import turtle

'''
Confused about angles? This might help
'''

pen = turtle.Turtle()
pen.speed(0)
for angle in range(0, 360, 15): #Count to 360 by 15, as in 15, 30, 45, 60...
    pen.setheading(angle)
    pen.forward(100)
    pen.write(str(angle) + '°') #Write text on the screen
    pen.backward(100)

turtle.done()