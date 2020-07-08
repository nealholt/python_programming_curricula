

Students should make the bones of the game starting from this tutorial (which uses pygame Sprites!): https://realpython.com/pygame-a-primer/


Tile map drawing tutorial:
https://qq.readthedocs.io/en/latest/


Make all the students watch this first then submit, then discuss ideas for the primary game loop.
https://www.youtube.com/watch?v=yh26jd9UqRw
Some major considerations:
-Should the dungeon scroll? In other words, should the player stay centered and move the dungeon around them or simply load a different dungeon each time? Centering the player is harder.
-How much is the game skill-based vs rpg based? Is there chance to hit and chance to block based on a random number generator? Of course there are many combinations of both. We could even have distance to target and frame of animation influence things like chance to hit, chance to critical, chance to block, chance to stun.
-Even if the primary game loop is something akin to: kill, loot, heal self, repeat. The second step is asking where the challenge comes in. Is there space management in terms of clutter in the dungeon and getting surrounded? Is it like the Super Star Wars games in which enemies often damage you, usually, give you some healing potions, but have more and less efficient ways to be killed and the challenge is a quick thinking issue of what's coming at you? Is it slower, like Diablo in which the challenge comes in planning your load out and skill set?

The following should be made use of very early on:
https://www.pygame.org/docs/ref/sprite.html



=== NOTES ON IMAGE SOURCES AND PRE-SETUP

Files:
	0x72_DungeonTilesetII_v1.2.png
	crop.py
	tiles_list.txt
Downloaded from here:
https://0x72.itch.io/dungeontileset-ii
To run crop.py you need PIL
which I downloaded no problem with the following line in the command prompt:
	pip install Pillow
I modified crop.py slightly. crop.py cuts out every image from the spritesheet and saves each one into the images folder.


=== 
Interface pieces (Flesh this out into function names, Class names, and input/output pre/post specifications):

Function that cuts out, converts, and loads all images into a single dictionary, which it returns.

	Dungeon Object Description:
	Dungeon Functions:
	Dungeon Tests:
Dungeon object: draws on screen tiles, given a coordinate returns False if that coordinate is blocked by a wall or otherwise out of bounds, helper function that translates xy coordinates into row col of a particular cell, perhaps functions that generate particular dungeon rooms that can be strung together or loads a dungeon from file, dungeon will also keep track of which cells are occupied by enemies or the player or items or traps etc.



	Sprite Object Description:
All images on the screen will be some sort of sprite. Minimally a sprite consists of an image and a location.

	Sprite Functions:
getRect - returns this sprite's bounding rectangle.
collidePoint - takes an x,y coordinate and returns true if this sprite's rectangle contains that point. This function doesn't need to do anything more than returning the restult of calling the rectangle's collide_point function.
collideRect - Much like the previous, this function doesn't need to do anything more than returning the restult of calling the rectangle's collide_rect function.
draw - a sprite can draw its image at a particular location.

	Sprite Tests:
Demonstrate correct collision with point
Demonstrate correct collision with rect
Draw on screen



	MovingSprite Object Description:
This object inherits from the base Sprite. MovingSprites animate, move, attack, and receive damage. MovingSprites consist of sequences of running and idling animations. They have hitpoints and collision damage. They have speed and direction.
All players and enemies will be sprite objects.

	MovingSprite Functions:
takeDamage - Takes an amount of damage, triggers this sprite's got_hit animation (if any) and reduces the hp of this sprite. This function may also check if this sprite is dead and trigger a death animation.
dealDamage - Takes a moving sprite as an argument and calls that sprite's takeDamage function with collisionDamage as an argument.
updateFunction - Updates the current animation image
moveLeft - Checks to see if this is a change in direction and, if so, updates the animation set in use. Changes x coordinate, sets direction variable.
moveRight - similar to previous
moveUp - similar to previous but changes y coordinate and does not update direction variable.
moveDown - similar to previous

	MovingSprite Tests:
walk right as a pygame circle
walk right as a circle (shadow) with run animation sequence
Same as above but while moving left.
Same as the above except moving up or down. When moving up or down player keeps facing left or right as they were when they started to move up and down.
Moving diagonally.
Cycle through idle animation when not moving.
Transition smoothly from the idle animation to the running animation and back again.
Go to target location: Given a target (x,y), take one step toward that location each frame until arrival, then transition to idle animation. This will be used by enemies to seek the player. We could also use it to send player's to a mouse click location if that's the game control scheme we want.





	Enemy Object Description:
	Enemy Functions:
	Enemy Tests:
Enemy object: move toward target location including updating the animation, attack that includes animation (initially just do damage on contact and try to move toward the player) and temporarily telling the dungeon object that a cell is having damage dealt to its occupant, function stringing all this together into implementation of moving to and attacking player, take damage function and animation, draw function, death animation, much later enemies can have different attack patterns; visions; etc.
Vision radius for enemy sprites

	Player Object Description:
	Player Functions:
	Player Tests:
Player Object: movement in all cardinal directions with displaying appropriate animation, picking up items, wielding swords, attacking, taking damage with animation, displaying health, later interacting with any dungeon elements; special abilities; etc

TODO Research pygame's built in sprite and spritegroup objects.
	SpriteGroup Object Description:
	SpriteGroup Functions:
	SpriteGroup Tests:
sprite_group object: keep list of all sprites, update all sprites, draw them all, check for collisions (though this might be mediated by the dungeon which tracks who is occupying which tiles), remove dead or unused sprites from the game.





Small test pieces
	-cutting out images, formatting them, slotting them into a dictionary for ready use
	-tiling. using 2d arrays to create maps. solely visual for starters
	-moving the player around and animating this movement
	-sword swinging animation (need image rotation?)
	-hitboxes
	-integrating the last three to swing sword and strike enemy
	-enemies: moving and animating
	-enemies damaging player
	-walls that obtruct movement
	-other environment interaction
	-picking up items off the ground




Extensions:
-scrolling world with follow camera. Initially, players will move between static maps for which the whole map is visible on the screen at the same time.

-a shadow under the creature helps clarify its location and can show if the creature is being flung through the air or hovering over the ground by displaying the sprite significantly above the shadow and shrinking the size of the shadow the higher the sprite goes.

-auto-generating maps. probably make them static at first.

-game over screen and new game screens.

-distinct enemy movement and attack patterns.
Enemies that spawn endlessly out of the ground like in zombies ate my neighbors.
Enemies that jump to a target spot on the screen. The spot will be indicated with a circle. Players have to get out of the spot, then strike the creature on the ground before it moves again.
Enemies that line up with the player horizontally, pause, then dash across the screen.

-special character roles and abilities:
healers, melee and ranged attacks, knockback, reviving fallen allies.

-death animations: turn character horizontal, draw them lower and stretch their shadow to makit look like they are lieing down. Draw a couple overlapping red circles for blood animations beneath them.

Don't necessarilly be limited by a diablo-like game.
Could make it so player creates dungeons against the heroes.
Could be dungeon puzzle games.
Could be something where you click on the enemies from above, almost like an RTS.

Magic spells. Draw enemies in gray scale to indicate they have been turned to statues.

Use skeleton creatures that rise from the dead bodies of other fallen enemies.

Spinning around with swords
Block stance
Shoot arrows
Swing sword to knock arrows back toward target

Shrink size of sword images to make them less ridiculous.

make character interesting like in super star wards. block front. bllock above. swing overhead. stab/lunge. Then make the enemies attack from all these directions. Enemies can: dash, leap, shoot, lob. Player can also do ranged attacks.

add random star-shaped spiky polygon flash at point of contact to give hit feedback. Color the polygon to signify the damage.


