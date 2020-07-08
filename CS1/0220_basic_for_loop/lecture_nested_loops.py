import turtle

#Lecture with this as an example

pen = turtle.Turtle()
pen.pensize(4)
pen.color('green')
pen.speed(0)

side_length1 = 100
angle2 = 5
side_length2 = 3

for i in range(7):
    pen.forward(side_length1)
    for j in range(60):
        pen.forward(side_length2)
        pen.left(angle2)

turtle.done()