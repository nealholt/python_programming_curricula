import turtle

tommy = turtle.Turtle()

tommy.penup()
tommy.goto(-200, -200)
tommy.speed(0)
tommy.pendown()

i = 0
while i < 400:
    tommy.color((i/134)%1.0,i/1000,i/500)
    tommy.goto(i-200, 200)
    tommy.goto(i-200, -200)
    i = i + 1

turtle.done()