import turtle

tommy = turtle.Turtle()

tommy.speed(0)
tommy.penup()
tommy.goto(-200, 0)
tommy.pendown()

i = 0
while i<100:
    tommy.color(0,0,i/100) #Adjust the color a little
    tommy.goto(4*i-200, 0) #Walk right a little
    #Draw a circle
    tommy.begin_fill()
    tommy.circle(50)
    tommy.end_fill()
    i = i+1

turtle.done()