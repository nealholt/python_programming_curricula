import random
import pygame, car, car_ballistic
import neural_net_draft06 as brain
from maps import getMapById

#If fps is set to zero this will perform an automated run.
fps = 0
#Choose a map
map_index = 2 #0=hard, 1=medium, 2=easy
#Choose the number of cars
population_size = 100
#High friction ballistic cars or non-ballistic
use_ballistic = True
'''IMPORTANT: this is where the number of layers and number
of neurons per layer is chosen. The first layer must have 7
and the last layer must have 2 because that's the specified
number of inputs and outputs.'''
nn_layers = [7,12,2]
#Attributes of the ballistic car
friction = 0.2
acceleration = 0.4 #Acceleration as a percentage of max speed per frame


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


def handleEvents(brains):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True

            elif event.key == pygame.K_SPACE:
                pass
            elif event.key == pygame.K_RETURN:
                pass

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
    #Delay to get desired fps
    clock.tick(fps)


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

    if fps > 0:
        #Send user input to the player
        userInputToPlayer(cars[0])
        cars[0].resetVision()
        cars[0].senseTrack(race_track)
        #Draw on the screen
        drawAndDelay([cars[0]], race_track)

    else:
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