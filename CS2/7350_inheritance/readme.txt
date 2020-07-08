
Start with the tree diagram at the top of this page then also talk through the example on this page which is copied right below. Note that the call to the super class has been changed to be more modern. I now use super() instead of the name of the super class.
This
super().methodName(args)
instead of
Animation.methodName(self, args)
https://www.python-course.eu/python3_inheritance.php



Next your own example of inheritance. The folder galaga_like_example contains examples of 
	Inheriting attributes
	Inheriting methods
	Overriding super methods
	Calling super methods
Some relevant strings you can control-f for are "Override parent method" and "Call parent method"



Then story of the broken game camera. Here's the bug. Sometimes the camera that follows over the player's shoulder would simply stop moving. It seemed to occur sometimes, but not always after an explosion struck near the player.
Answer: The programmers were using a Sprite object that everything else in the game inherited from. The Sprite had hitpoints and could die, which was appropriate for almost everything in the game, but not for the camera. Explosions near the player were killing the camera. When the camera died it stopped moving.
Solution: Had a boolean variable is_invincible and set it to true for the camera.


Then some assignments:

Create a Vehicle object with attributes: number_of_wheels, top_speed, and terrain.
Then create three objects that inherit from Vehicle: Car, Boat, and Motorcycle.
Note: The number of wheels passed to the parent/super class should be constant, as should the terrain.

Create a Pet object. Then create Cat, Dog, and Goldfish objects that inherit from Pet. You decide what functions and attributes the parent and child classes should have.

Deeper inheritance:
Tell students that objects can have multiple layers of inheritance. Then the assignment is for students to create the following objects and use them in a short text program. They can be as creative as they like with the variables and methods.
PrepAffiliate class
Two classes, Lion and Unicorn, that inherit from the PrepAffiliate class.
Two more classes, LionStudent and UnicornStudent, that inherit from the Lion or Unicorn classes.


Note: This site covers multiple inheritance:
https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
