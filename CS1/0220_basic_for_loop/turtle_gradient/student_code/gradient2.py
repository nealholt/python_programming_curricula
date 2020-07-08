"""
Evan Custer
10-10-2017
CS1 Gradiant 
"""
#getting the turtle and time and setting up the turtle and setting tim=turtle.Turtle()
import turtle, time 

tim=turtle.Turtle()
tim.hideturtle()
tim.speed(5000)

tim.penup()
for i in range(701):
    #i am taking the varible i and then dividing it by 1000 to get the gradiant of color
    tim.color(i/700,0,0)

    #it is saying go to the cordents and then the other set then foward 1 and then repeat
    tim.goto((-350+i),-350)
    tim.pendown()
    tim.goto((-350+i),350)
    tim.fd(1)
    

time.sleep(10)