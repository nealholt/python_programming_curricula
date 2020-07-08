'''
For 18 points, read the instructions and answer the following
questions. You will use this code to answer the questions.

Here you will learn to use dx and dy to simulate gravity.

Gravity is a force that constantly pulls objects down toward
the center of the Earth.

Since dy is our vertical velocity variable, gravity will change
the dy variable.

1. In the following program what value is the gravity variable
set to?

2. What line of code calculates how gravity should change dy?

3. If the value of dy is currently 5, what is the new value of
dy after running this line of code:
    dy = dy-gravity

4. Would a larger or smaller amount of gravity make tina
the turtle bounce higher?

5. Change the value of gravity so that tina the turtle's bounce
just scrapes the top of the screen. What's the new value of
gravity?

6. Change the value of dx so that the arc of tina's bounce is
wider.

7. What does dx stand for?

8. What does dx mean?

9. What does dy stand for?

10. What does dy mean?

'''

import turtle

dx = 2
dy = 30
bounds= 320
gravity = 0.8
x = 0
y = -bounds

tina = turtle.Turtle()
tina.speed(2)
tina.penup()
tina.goto(x, y)

for i in range(500):
    #Stay inside the screen's bounds
    if x>bounds or x<-bounds:
        #reverse direction
        dx = -dx
    #bounce when you hit the ground
    if y < -bounds:
        dy = 30
    #apply gravity
    dy = dy-gravity
    #Move
    x=x+dx
    y=y+dy
    tina.goto(x, y)
    #Stamp a turtle imprint on the screen
    tina.stamp()

turtle.done()