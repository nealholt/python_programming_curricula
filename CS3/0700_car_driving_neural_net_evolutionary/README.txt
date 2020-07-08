
This project is in great shape. It would be nice to write some investigation questions for it, but you SHOULD use this for students in CS3 next year.



This project is really about hill climbing optimization or genetic algorithms, not neural nets.

However it does rely on the neural net code.

These files also contain your very best line segment intersection code.


Fun sequence of videos doing pretty much the exact same thing as what I did:
https://www.youtube.com/watch?v=ZX2Hyu5WoFg
https://www.youtube.com/watch?v=OpodKCR6P-M
https://www.youtube.com/watch?v=GDy45vT1xlA


=== INVESTIGATION LEADING UP TO PROJECT

TODO:

Write questions that educate them about
-genetic algorithms
-mutation
-crossover
-fitness
-selection
-weighted sums
-how to keep the mutated weights in range
-how to write tests to evaluate their code despite the randomness.


=== IDEAS FOR STUDENTS

-Students could implement a "rolling" rather than generational population that simply throws back in new members whenever a car crashes.


=== INSPIRATION

This project was inspired by the following (foul language in the code bullet video):
https://www.youtube.com/watch?v=wL7tSgUpy8w
https://www.youtube.com/watch?v=r428O_CMcpI


=== ORGANIZATION:

move constants out of the top of car and into the top of main.


=== CURIOSITY:

Use neural net learning by creating a set of scenarios and initially training the neural net on these scenarios before performing further optimization with the genetic algorithm. For instance, short sensors on the left should make the car turn right and vice versa. Long sensors in all directions should make the car speed up. Short sensors ahead should make the car slow down. This sort of learning can be trained directly into the neurons using reinforecement learning.
You could also have smaller scenarios where a car has to turn left around an obstacle, turn right around an obstacle, and drive straight between obstacles.


=== OPTIMIZATION:

optimize collision detection


