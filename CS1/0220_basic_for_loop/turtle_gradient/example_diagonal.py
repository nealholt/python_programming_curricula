import turtle

tommy = turtle.Turtle()

tommy.penup()
tommy.goto(-300, 300)

tommy.pendown()

i = 0
while i< 600:
    tommy.color(0,0,i/600)
    tommy.goto(-300, 300-i)
    tommy.goto(i-300, 300)
    i = i+1

turtle.done()