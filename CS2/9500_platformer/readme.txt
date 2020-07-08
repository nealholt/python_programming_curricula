
Platformers have a few issues:
 - managing collisions with platforms
 - how to "shove out" from a platform
 - when the player can jump again
 - controls issues such as, can the player change direction in mid air.
There is no right or wrong way to do these things.
The code you wrote in main07.py doesn't behave exactly the way you want, but if you made it so the player can't change their horizontal movement in mid air then this would be much more similar to Mario and match up with your expectations.

But none of this is important.
What's important is that students decide how they want to manage these issues and they create their own game that they want to play.
So help students make and execute a plan. Don't worry that your code is not perfect. They don't get to use your code.

==============================================

3 Projects should really be done here.

1. Closed: You need to write a particular program to accomplish a particular task.
Write a program that jumps a sprite into the air and then applies gravity each frame. Also, must stop the sprite at the bottom of the screen. Also walk the sprite left and right. Also draw a rectangle in the air. For now, your sprite will simply pass through the other rectangle.

2. Open ended: You need to write any program that will accomplish a particular task.
Write a function that is triggered the moment that the sprite collides with the rectangle. Your function needs to make the sprite interact with the ractangle the same way mario interacts with blocks. If mario is approaching from the bottom he should lose all upward momentum and be pushed out of the block. If approaching from top he stands on top of the block. If approaching from the sides then shove out in that direction, but don't change upward momentum.
This is actually pretty tricky. x, y, width, height, and dx and dy of the sprite are all relevant.

3. Free: You need to write any program to accomplish a general task.
Write your own platformer game.


Like everything, the kids should design their own game here.
Your input should be to help them understand interaction with platforms and how to manage the jumping. Then they can make any sort of game they want. You could also present the follow camera and have them put the two together into their own game. They'll have to invent their own enemies and figure out if they're doing something more like mario or mega man or something else entirely.

Challenge: Add a rewind feature like braid. You just need to remember a rolling set of previous locations and then rewind through them at the press of a button. You can record every other frame if you want.

Challenge: Different friction (atmospheric viscosity or ground friction, ice) or wind conditions

Students can take this as far as they want. Give them some space to play here. Maybe talk about how to load different levels or consider doing the follow camera early.
