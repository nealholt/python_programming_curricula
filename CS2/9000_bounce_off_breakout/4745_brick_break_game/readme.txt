
The goal is to write a game like that one ipad game marie had with the balls flying and hitting bricks.

Bricks enter from ceiling and have a health that goes up by 1 each time.
Bricks randomly spawn or not in 8 locations along the top of the screen.
Click to fire all balls in sequence from a random starting point at bottom of screen toward the mouse click.
Also include round "extra ball" powerups.


NOTE: This is harder than bullethell unless you share the pushOut method and the method that determines if a collision is more vertical or more horizontal. These are possibly worth sharing or making a mini lesson out of creating them.
You should also consider a mini test program with one large ball and one or two large bricks and a super slow frame rate to see a collision in great detail. Show the collision, the push out, draw the vectors and how they change.
You might be able to improve collisions by checking for collisions not with the ball's bounding rectangle, but with points on the circumference of the ball. You can use collidepoint. Then you might even use circular bounce off at the corners as if the bricks had rounded corners. This could be use if any point on the ball other than the cardinal direction points collide with the brick.


But first just make breakout which consists of a paddle moving along bottom of screen and bricks to break along the top.
