import turtle

#Create turtle
tommy = turtle.Turtle()

#Put the turtle in the location you want.
tommy.penup()
tommy.goto(-200,200) #Near the top left
tommy.pendown()

i = 0
while i< 10:
    tommy.goto(40*i-200, -200) #go to the bottom of the screen
    tommy.goto(40*i-200, 200) #Reset to the top of the screen
    i = i+1

#Pause when the program ends
turtle.done()