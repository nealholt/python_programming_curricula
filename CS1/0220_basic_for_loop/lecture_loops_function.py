import turtle

#Use this as an instructional example during lecture

tommy = turtle.Turtle()
tommy.penup()
tommy.goto(0,-100)
tommy.pendown()
tommy.pensize(6)
tommy.color('green')
tommy.speed(0)

def makeLoops(pen, side_length, angle, iterations):
    for i in range(iterations):
        pen.forward(side_length)
        pen.right(angle)

makeLoops(tommy, 2, 5, 50)
tommy.forward(100)
makeLoops(tommy, 1, 2, 170)
tommy.forward(100)
makeLoops(tommy, -3, 3, 100)
tommy.forward(100)
makeLoops(tommy, 2, 5, 50)

turtle.done()