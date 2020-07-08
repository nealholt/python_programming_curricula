
For 400 points, write a program that trains a
computer-controlled ship to make successful attack runs against
a target without running into the target.

An initial control scheme has been provided. The NPC ship 
decides whether or not to shoot, accelerate forward/backward,
yaw closer/further from the target, and turn toward/away from 
the target. It makes the decision based on an array of values
but selects a different set of values depending on its distance 
from the target. So, for example, far from the target the ship
may accelerate toward the target, while close to the target
the ship might choose to accelerate away while facing the 
target and shooting.

The ship fires 3 shots in a burst and then has a long cooldown
before it can fire again. The current challenge is to hit the
target with the maximum number of shots in 20 seconds without
running into the target. Points are allocated in main.py's 
updateBullets and experiment functions.

You should begin by familiarizing yourself with the program,
especially the player.py file and main.py.

You may use the given control scheme and baseline attack
pattern in player.py or modify it as you like, but make sure 
to budget your time so you can finish the project in a timely manner.

Next choose how you will optimize the control scheme. Will you use
a hill climber? Genetic algorithm? Something else?

You may also modify the physics or ship controls if you want.

You could even overhaul the game to create a duel in which the
ships learn to fight each other and both ships adapt and learn.

You should turn in commented code and a list of any 
modifications that you made outside of main.py. The code you
turn in should be easily runnable in two modes:
1. optimization mode in which the computer players learn
2. a mode that visually shows the best learned patterns in action.
