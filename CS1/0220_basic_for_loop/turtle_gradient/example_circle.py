import turtle

tommy = turtle.Turtle()

tommy.penup()
tommy.goto(0, -400)
tommy.pendown()

i = 0
while i< 800:
    tommy.color(i/800,i/1600,i/800)
    tommy.begin_fill()
    tommy.circle(800-i)
    tommy.end_fill()
    tommy.penup()
    tommy.goto(0, -400+i/2)
    tommy.penup()
    i = i+10

turtle.done()