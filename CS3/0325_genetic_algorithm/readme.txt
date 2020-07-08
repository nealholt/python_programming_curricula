
Create a project to illustrate genetic algorithms and deceptive functions that fool hill climbers.

Use a fitness function that takes a binary list as input and gives fitness for triplets of the same value, gives more fitness for multiple aligned triples of ones, and gives the most fitness for a list of all ones.
010101101 Worst
000101001 Bad
000100111 Ok
000000000 Good
000111000 Better
111111111 Best

One difficulty with this function is that this genome
000111000 has higher fitness than this genome
101111010 even though the second one is closer to the best fitness level possible.

Students should use a longer genome of length 27.





Here is a basic project idea:

Optimize a function on interval -99 to 99. With each gene a digit. Could be fun!
Your genome is each digit xx.xxxxxx

This function can be maximized on the interval -10 to 10
y=(1/300)(x-5)(x+1)(x+2)(x-10)(x+4)
Now you just need a better function the bigger interval. Could use sum of sine waves!



ANOTHER IDEA: represent a tic tac tow board in trinary (0, 1, or 2) and then associate each board with a valid next move and then evolve the solutions against each other.
I like this idea and you don't need 2d arrays. You can use 3 1-d arrays.


ANOTHER IDEA: You could convert to and from binary as part of the lesson then each index in the gene array could correspond to a game history that plays the prisoner's dilemma and you could see what evolves.

ANOTHER IDEA: Could you use function drawing to create creatures with different fur patterns? Start off with the creature having white fur (check for white pixels) and then teach punnet squares or some such with how they mate and evolve?
