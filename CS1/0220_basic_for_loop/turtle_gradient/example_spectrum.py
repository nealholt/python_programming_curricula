import turtle

#turtle.tracer(0.0)

tommy = turtle.Turtle()
tommy.speed(0)
tommy.penup()
tommy.goto(-400, -400)
tommy.pendown()

i = 0
while i< 800:
    tommy.color(0,0,i/800)
    tommy.goto(i-400, 400)
    tommy.goto(i-400, -400)
    i = i+1

turtle.update()
turtle.done()