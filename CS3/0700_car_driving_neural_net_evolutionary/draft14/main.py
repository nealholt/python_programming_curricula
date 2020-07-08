import random
import pygame, car, car_ballistic
import neural_net_draft06 as brain
from maps import getMapById


map_index = 2 #0=hard, 1=medium, 2=easy
population_size = 100
mutation_count = 200 #mutations per generation
crossover_count = 3 #crossover events per generation
use_ballistic = True
'''IMPORTANT: this is where the number of layers and number
of neurons per layer is chosen. The first layer must have 7
and the last layer must have 2 because that's the specified
number of inputs and outputs.'''
nn_layers = [7,12,2]
#Attributes of the ballistic car
friction = 0.2
acceleration = 0.4 #Acceleration as a percentage of max speed per frame
#Attributes of the "normal" car




#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
black = 0,0,0



def getCar():
    if use_ballistic:
        return car_ballistic.CarBallistic(screen, 100, 200, friction,acceleration)
    else:
        return car.Car(screen, 100, 200)

def makeNewGeneration(current_gen,parents,nudge=True):
    '''Both of the arguments to this function are lists
    of neural networks.

    current_gen is the current list of neural networks.

    parents is a list of neural networks selected for breeding
    the next generation.

    nudge specifies which type of mutation to use.'''
    if len(parents) == 0:
        return
    #Copy the parents over the current generation,
    #obliterating the previous generation.
    index = 0
    for i in range(len(current_gen)):
        current_gen[i] = parents[index].getCopy()
        index = (index+1)%len(parents)
    #Crossover members of the current generation but preserve
    #the parents by only crossing over from
    #len(parents)-1 to the end of the list.
    for _ in range(crossover_count):
        p1 = random.choice(current_gen[len(parents)-1:])
        p2 = random.choice(current_gen[len(parents)-1:])
        crossover(p1,p2)
    #Mutate members of the current generation but preserve
    #the parents by only crossing over from
    #len(parents)-1 to the end of the list.
    for _ in range(mutation_count):
        p1 = random.choice(current_gen[len(parents)-1:])
        if nudge:
            mutateNudge(p1)
        else:
            mutateBlast(p1)



def userInputToPlayer(player):
    '''This is no longer in use.'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.moveForward()
    if keys[pygame.K_DOWN]:
        player.moveBackward()
    if keys[pygame.K_LEFT]:
        player.rotateLeft()
    if keys[pygame.K_RIGHT]:
        player.rotateRight()
    if keys[pygame.K_a]:
        player.accelerate()
    if keys[pygame.K_d]:
        player.brake()


def handleEvents(brains):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True

            #Press enter or space for a new generation. space gives
            #a light nudge mutation. Enter gives completely random
            #replacement mutation
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                global cars, selected, population_size
                makeNewGeneration(brains,selected, event.key == pygame.K_SPACE)
                #Reset selected neural nets and all the cars
                selected = []
                for i in range(population_size):
                    cars[i] = getCar()

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #Print position of the mouse click. This was used
            #to create the race track.
            print(pos,',')
            #Check if the mouse clicked on any particular cars.
            #This is currently how "fit" individuals are selected.
            for i in range(len(cars)):
                if cars[i].contains(pos):
                    if not brains[i] in selected:
                        #Add select neural nets to the selected list
                        selected.append(brains[i])
                    #Highlight selected cars
                    cars[i].line_thickness = 5
            print('Selected: '+str(len(selected)))
    return False

def drawAndDelay(cars, race_track):
    #fill screen with black
    screen.fill(black)
    #Draw player
    for c in cars:
        c.draw()
    for seg in race_track:
        seg.draw()
    #Update the screen
    pygame.display.flip()
    #Delay to get 30 fps NOTE: Don't delay any more. It's already too slow.
    #clock.tick(30)


def mutateBlast(neural_net):
    '''Re-roll a random weight in the neural network.'''
    layer = random.choice(neural_net.layers[1:])
    neuron = random.choice(layer)
    neuron.weights[random.randint(0,len(neuron.weights)-1)] = random.random()*2-1

def mutateNudge(neural_net):
    '''Adjust a random weight in the neural network.'''
    layer = random.choice(neural_net.layers[1:])
    neuron = random.choice(layer)
    index = random.randint(0,len(neuron.weights)-1)
    neuron.weights[index] += (random.random()-0.5)*0.1
    if neuron.weights[index] > 1:
        neuron.weights[index] = 1
    if neuron.weights[index] < -1:
        neuron.weights[index] = -1



def crossover(nnet1, nnet2):
    '''Swap random neurons in a random layer between
    neural nets.'''
    layer_index = random.randint(1,len(nnet1.layers)-1)
    layer1 = nnet1.layers[layer_index]
    layer2 = nnet2.layers[layer_index]
    split = random.randint(0,len(layer1)-1)
    for i in range(split):
        copy = layer1[i].getCopy()
        layer1[i] = layer2[i]
        layer1[i].inputs = nnet1.layers[layer_index-1]
        layer2[i] = copy
        layer2[i].inputs = nnet2.layers[layer_index-1]



#TESTING: verify that neural net copying and mutating function
#roughly as expected. This code will exit if there is a problem.
b1 = brain.NeuralNet([7,10,2])
b1.verifyInputLayer()
b2 = b1.getCopy()
b2.verifyInputLayer()
if b1 == b2:
    print('ERROR: getCopy returns shallow copy.'); exit()
if not b1.sameAs(b2):
    print('ERROR: getCopy does not return proper copy.'); exit()
mutateBlast(b2)
if b1.sameAs(b2):
    print('ERROR: mutateBlast does not modify neural net.'); exit()
b2 = b1.getCopy()
mutateNudge(b2)
if b1.sameAs(b2):
    print('ERROR: mutateNudge does not modify neural net.'); exit()

race_track = getMapById(screen, map_index)

#Create paired neural nets and cars
brains = []
cars = []
selected = [] #a list of cars that have been clicked on
for _ in range(population_size):
    c = getCar()
    cars.append(c)
    b = brain.NeuralNet(nn_layers)
    brains.append(b)


#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents(brains)

    #Send user input to the player
    #userInputToPlayer(player)

    #Update all the cars
    for i in range(len(cars)):
        #Ignore cars that hit the wall
        if not cars[i].crashed:
            cars[i].resetVision()
            cars[i].senseTrack(race_track)
            data = cars[i].getSensorData()
            #print('data '+str(data))
            brains[i].predict(data) #Send data to neural net
            outputs = brains[i].getOutputs() #Get response from neural net
            #print('nn outputs '+str(outputs))
            cars[i].respondToInput(outputs) #Control car with the response
            cars[i].moveForward()
            #print()
            #print(player.getSensorLengths())
            #print(player.getSensorPercents())

    #Draw on the screen
    drawAndDelay(cars, race_track)

pygame.quit()