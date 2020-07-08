'''
For 20 points, read the instructions and answer the following
questions. You will use this code to answer the questions.

Here you will learn to use dx and dy to simulate friction.

Friction is always slowing the velocity of an object.

Since dx and dy are velocity variables, friction will change
both of them.

1. In the following program what value is the friction variable
set to?

2. What lines of code calculates how friction changes velocity?

3. Would a larger or smaller amount of friction make tina
slow down sooner?

4. You can think of friction as the percentage of velocity lost
each time the screen updates. dx is set equal to its current
value times 1-friction because 1-friction gives the amount of
velocity that remains.
What is the value of  1-friction  ?

5. If the value of dx is currently 6, what is the new value of
dx after running this line of code:
    dx = dx*(1-friction)

6. Change the value of friction so that tina the turtle bounces
off the far wall and just barely makes it back to where she
started. What value of friction did you use?

7. What percentage of velocity is lost each screen update with
your new friction value?

8. What percentage of velocity remains between each screen update
with your new friction value?
'''

import turtle

dx = 6
dy = 35
bounds= 320
gravity = 0.8
friction = 0.01
x = -bounds
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
        dy = -dy
    #apply gravity
    dy = dy-gravity
    #apply friction
    dx = dx*(1-friction)
    dy = dy*(1-friction)
    #Move
    x=x+dx
    y=y+dy
    tina.goto(x, y)
    #Stamp a turtle imprint on the screen
    tina.stamp()

turtle.done()