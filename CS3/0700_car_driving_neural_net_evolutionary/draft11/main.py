import random
import pygame, player, line_segment
import neural_net_draft05 as brain

#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
black = 0,0,0


def makeNewGeneration(current_gen,parents,nudge=True):
    '''Both of the arguments to this function are lists
    of neural networks.'''
    #Copy the parents over the current generation
    index = 0
    for i in range(len(current_gen)):
        current_gen[i] = parents[index].getCopy()
        index = (index+1)%len(parents)
    #Crossover members of the current generation but preserve
    #the parents
    for _ in range(crossover_count):
        p1 = random.choice(current_gen[len(parents)-1:])
        p2 = random.choice(current_gen[len(parents)-1:])
        crossover(p1,p2)
    #Mutate members of the current generation but preserve
    #the parents
    for _ in range(mutation_count):
        p1 = random.choice(current_gen[len(parents)-1:])
        if nudge:
            mutateNudge(p1)
        else:
            mutateBlast(p1)



def userInputToPlayer(player):
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

            #Enter or space for a new generation. space gives
            #a light nudge mutation. Enter gives bigger mutations
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                global cars, selected, population_size
                makeNewGeneration(brains,selected, event.key == pygame.K_SPACE)
                #Reset everything
                selected = []
                for i in range(population_size):
                    cars[i] = player.Player(screen, 100, 200)

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos,',') #TODO
            for i in range(len(cars)):
                if cars[i].contains(pos):
                    if not brains[i] in selected:
                        selected.append(brains[i])
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
    #Delay to get 30 fps
    #clock.tick(30)


def mutateBlast(neural_net):
    '''Re-roll a random weight.'''
    layer = random.choice(neural_net.layers[1:])
    neuron = random.choice(layer)
    neuron.weights[random.randint(0,len(neuron.weights)-1)] = random.random()

def mutateNudge(neural_net):
    '''Adjust a random weight.'''
    layer = random.choice(neural_net.layers[1:])
    neuron = random.choice(layer)
    neuron.weights[random.randint(0,len(neuron.weights)-1)] += (random.random()-0.5)*0.1

def crossover(nnet1, nnet2):
    '''Swap half the neurons in a layer between neural nets.'''
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

race_track_inner = [
(103, 283) ,
(208, 125) ,
(285, 157) ,
(227, 305) ,
(339, 372) ,
(513, 400) ,
(657, 256) ,
(746, 145) ,
(801, 292) ,
(699, 363) ,
(728, 488) ,
(563, 472) ,
(474, 433) ,
(260, 398) ,
(147, 418)]
race_track_outer = [(21, 237) ,
(202, 35) ,
(396, 85) ,
(366, 206) ,
(319, 280) ,
(404, 332) ,
(473, 344) ,
(582, 212) ,
(685, 80) ,
(748, 46) ,
(863, 143) ,
(867, 337) ,
(791, 394) ,
(848, 512) ,
(696, 577) ,
(481, 566) ,
(449, 478) ,
(330, 468) ,
(202, 545) ,
(47, 438) ,
(12, 276)]
race_track = []
white = 255,255,255
for i in range(len(race_track_inner)-1):
    seg = line_segment.LineSeg(screen, white,
                race_track_inner[i][0],
                race_track_inner[i][1],
                race_track_inner[i+1][0],
                race_track_inner[i+1][1])
    race_track.append(seg)
seg = line_segment.LineSeg(screen, white,
            race_track_inner[-1][0],
            race_track_inner[-1][1],
            race_track_inner[0][0],
            race_track_inner[0][1])
race_track.append(seg)

for i in range(len(race_track_outer)-1):
    seg = line_segment.LineSeg(screen, white,
                race_track_outer[i][0],
                race_track_outer[i][1],
                race_track_outer[i+1][0],
                race_track_outer[i+1][1])
    race_track.append(seg)
seg = line_segment.LineSeg(screen, white,
            race_track_outer[-1][0],
            race_track_outer[-1][1],
            race_track_outer[0][0],
            race_track_outer[0][1])
race_track.append(seg)


#Create bunches of paired neural nets and cars
brains = []
cars = []
selected = [] #a list of cars that have been clicked on
population_size = 100
mutation_count = 200
crossover_count = 3
for _ in range(population_size):
    c = player.Player(screen, 100, 200)
    cars.append(c)
    b = brain.NeuralNet([7,12,2])
    brains.append(b)


#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents(brains)

    #Send user input to the player
    #userInputToPlayer(player)
    for i in range(len(cars)):
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