'''
For 40 points, read the instructions and answer the following
questions. You will use this code to answer the questions.

Using a pair of variables named dx and dy is the professional
way to implement all kinds of movement for computer games or
simulations.

dx stands for "delta x" and means the "change in x". dx is
the run in the slope formula: rise/run.

dy stands for "delta y" and means the "change in y". dy is
the rise in the slope formula: rise/run.

If you want an object to move at a 45 degree angle, set dx=1
and dy=1.

If you want an object to move at a 90 degree angle, set dx=0
and dy=1.

1. Which line of code below checks to see if tina the turtle
has run outside the edges of the screen?

2. What three lines of code cause tina to move?

3. What line of code reverses tina's direction?

4. If the value of dx is currently 5, what is the new value of
dx after running this line of code:
    dx = -dx

5. If the value of dx is currently -1, what is the new value of
dx after running this line of code:
    dx = -dx

6. Add new code to the program so that tina bounces off the top
and bottom of the screen in the same way that she currently
bounces off the sides of the screen. (Turn in this entire
program when you're finished so I can see your answer.)

7. What does dx stand for?

8. What does dx mean?

9. What does dy stand for?

10. What does dy mean?

11. What should dx and dy be set to if I want tina to move at
an angle of negative 45 degrees (down and to the right)?

12. What should dx and dy be set to if I want tina to move at
an angle of negative 135 degrees?

13. OPTIONAL: For 20 extra points, add code so that tina's color
changes as she moves.

14. OPTIONAL: For 30 extra extra points, add code so that
tina has a buddy turtle named tim and both turtles bounce
around the screen. (You can/should modify their initial
dx and dy values so they head in different directions.)
'''

import turtle

x = 0
y = 0
dx = -5
dy = -1
bounds= 350

tina = turtle.Turtle()
tina.speed(2)
tina.pensize(10)

for i in range(500):
    #Stay inside the screen's bounds
    if x>bounds or x<-bounds:
        #reverse direction
        dx = -dx
    #Move
    x=x+dx
    y=y+dy
    tina.goto(x, y)

turtle.done()