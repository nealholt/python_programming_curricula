'''
For 300 points, write a genetic algorithm.

Hill climbing optimization works great when there is a straight
path from a problem to a solution, but some problems are 'deceptive'.

For example, suppose I have a fitness function that takes a list
of ones and zeroes as input. The function gives some fitness points
for any triplets of ones or zeroes such as 111 or 000, but it gives
the most points for triplets of ones.

Here are the fitnesses of some example genomes:
010101101 Worst
000101001 Bad
000100111 Ok
000000000 Good
000111000 Better
111111111 Best

This same example is available in code below.

One difficulty with this function is that this genome
000111000 has higher fitness than this genome
101111010 even though the second is closer to the best fitness
level possible.

Your task is to write a genetic algorithm using genomes that are lists
of ones and zeroes and are length 27. Your genetic algorithm must
optimize the fitness function given below (same as the one described
above).

You must include:
    a mutation function,
    a crossover function,
    a function to create and return an individual genome,
    a function to create and return a whole population.

Your comments must describe any decisions you make about who lives and
who dies from one generation to the next, as well as any other relevant
choices.

For more information on genetic algorithms, or if you get stuck,
check out this website:
https://lethain.com/genetic-algorithms-cool-name-damn-simple/
'''

def fitnessFunction(genome):
    fitness = 0
    #step through by 3's
    for i in range(0,len(genome)-1,3):
        #Check for 3 in a row match
        if genome[i]==genome[i+1] and genome[i+1]==genome[i+2]:
            fitness += 1 #Fitness for identical triplets
            if genome[i]==1:
                fitness += 1 #Even more fitness if those triplets are ones
    return fitness


#TESTING
test = [0,1,0,1,0,1,1,0,1] #Worst 0
print(fitnessFunction(test))
test = [0,0,0,1,0,1,0,0,1] #Bad 1
print(fitnessFunction(test))
test = [0,0,0,1,0,0,1,1,1] #Ok 3
print(fitnessFunction(test))
test = [0,0,0,0,0,0,0,0,0] #Good 3
print(fitnessFunction(test))
test = [0,0,0,1,1,1,0,0,0] #Better 4
print(fitnessFunction(test))
test = [1,1,1,1,1,1,0,0,0] #Even Better 5
print(fitnessFunction(test))
test = [1,1,1,1,1,1,1,1,1] #Best 6
print(fitnessFunction(test))


