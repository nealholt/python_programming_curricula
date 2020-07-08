
This could make a great machine learning / optimization game. See notes at the bottom for progress on this front.

This guy goes deep into his experience doing this
https://www.codingame.com/blog/genetic-algorithm-mars-lander/
I didn't get much out of the article, but a link took me here:
https://www.codingame.com/blog/genetic-algorithms-coders-strike-back-game/

and I appreciated the insight that his GA basically broke down to different genes controlling conditions in an if statement and the actions that trigger when those conditions are met:

For example:

So a typical genome could be read as:

[(no shield, angle = 12°, thrust = 200), (no shield, angle = 18°, thrust = 150), (shield, angle = 18°, thrust ignored)]

So a raw genome is actually closer to this:

{(0.08, 0.43, 0.07), (0.27, 0.55, 0.15), (0.18, 0.07, 0.02), (0.51, 0.97, 0.43), (0.15, 0.69, 0.99), (0.33, 0.05, 0.01)};
The algorithm reads it like so, in pseudo code:

for each triplet (gene1, gene2, gene3)
 if(gene1 > 0.95)
     requestShield();
 if(gene2 < 0.25) requestAngle(-18); else if(gene2 > 0.75)
     requestAngle(18);
 else
     requestAngle(-18 + 36 * ((gene2 – 0.25) * 2.0));
 if(gene3 < 0.25) requestThrust(0); else if(gene3 > 0.75)
     requestThrust(200);
 else
     requestThrust(200 * ((gene3 – 0.25) * 2.0));






Input: ship angle, x distance to pad, altitude, dx, dy
I added a "getData" function to game Manager to gather all this info, but none of it is normalized.

Output: rotate left or right, thrust amount

Added rateTheLanding function in ground.py.

Could add in fuel later.
