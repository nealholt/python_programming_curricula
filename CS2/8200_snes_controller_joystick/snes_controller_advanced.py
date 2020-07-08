'''This Python program demonstrates how to receive complex input from a
SNES controller such as responding to double taps and simultaneous button
presses.
'''
import pygame, math

class Player:
    #Create a player
    def __init__(self, screen, x, y):
        self.screen = screen
        #Coordinates of the center of the player
        self.x = x
        self.y = y
        #Velocity
        self.dx = 0
        self.dy = 0
        #Current direction player is facing
        self.angle = 0
        #How fast this player rotates
        self.rotation_rate = math.pi/32
        #Amount of friction always applied
        self.braking_friction = 0.1
        self.default_friction = 0.001
        self.friction = self.default_friction
        #How much acceleration this ship has
        self.default_accel = 0.5
        self.boost_accel = 1.5
        self.accel = self.default_accel
        self.boost_timeout = 30
        self.boost_reset = 30

    def update(self):
        #move
        self.x = self.x+self.dx
        self.y = self.y+self.dy
        #apply friction
        self.dx = self.dx*(1-self.friction)
        self.dy = self.dy*(1-self.friction)
        #Countdown to removal of boost
        self.boost_timeout -= 1
        if self.boost_timeout == 0:
            self.accel = self.default_accel

    def accelerate(self, angle, accel):
        self.dx = self.dx + math.cos(angle)*accel
        self.dy = self.dy + math.sin(angle)*accel

    def accelerateForward(self):
        self.accelerate(self.angle,self.accel)

    def accelerateBackward(self):
        self.accelerate(self.angle+math.pi,self.accel/2)

    def accelerateLeft(self):
        self.accelerate(self.angle-math.pi/2,self.accel/2)

    def accelerateRight(self):
        self.accelerate(self.angle+math.pi/2,self.accel/2)

    def rotateLeft(self):
        self.angle -= self.rotation_rate

    def rotateRight(self):
        self.angle += self.rotation_rate

    def getCorners(self, radii, angles):
        #Returns list of points to draw the Player
        points = []
        for i in range(len(angles)):
            a = angles[i]*math.pi/180+self.angle
            x = self.x+radii[i]*math.cos(a)
            y = self.y+radii[i]*math.sin(a)
            points.append((x,y))
        return points

    def draw(self):
        #Angles and radii to determine shape of the player
        angles = [0,135,-135] #in degrees
        radii = [40,20,20] #in pixels
        #Draw outline of player.
        points = self.getCorners(radii, angles)
        #5 is line thickness.
        pygame.draw.polygon(self.screen, white, points,5)


#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
black = 0,0,0
white = 255,255,255

# Initialize the joysticks
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
num_buttons = joystick.get_numbuttons()

#Track shoulder button state to detect simultaneous press or release
shoulder_left = joystick.get_button(4)
shoulder_right = joystick.get_button(5)

#Track up button state to detect double tap
up_button = round(joystick.get_axis(1))==-1 #True if pressed
up_change_count = 0 #in unit of frames

def userInputToPlayer(p):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.accelerateForward()
    if keys[pygame.K_DOWN]:
        p.accelerateBackward
    if keys[pygame.K_LEFT]:
        p.rotateLeft()
    if keys[pygame.K_RIGHT]:
        p.rotateRight()

    #Detect simultaneous press of both shoulder buttons to reverse player
    global shoulder_left, shoulder_right
    if not shoulder_left and not shoulder_right and joystick.get_button(4) and joystick.get_button(5):
        p.angle += math.pi
    #Check if the left shoulder button is currently being pressed.
    elif joystick.get_button(4):
        p.rotateLeft()
    #Check if the right shoulder button is currently being pressed.
    elif joystick.get_button(5):
        p.rotateRight()
    shoulder_left = joystick.get_button(4)
    shoulder_right = joystick.get_button(5)

    #The directional buttons or D-pad are a bit weird.
    #First we ask for the axis input. It's important to
    #round these numbers.
    x_motion = round(joystick.get_axis(0))
    y_motion = round(joystick.get_axis(1))
    #The x motion will be -1, 1, or 0 depending on which
    #direction was pushed, if any.
    if x_motion == 1:
        p.accelerateRight()
    elif x_motion == -1:
        p.accelerateLeft()
    #The y motion will be -1, 1, or 0 depending on which
    #direction was pushed, if any.
    if y_motion == 1:
        p.accelerateBackward()
    elif y_motion == -1:
        p.accelerateForward()

    #Track changes in up button to give speed boost if double tapped
    global up_button, up_change_count
    up_change_count += 1
    #If up button was down but is now up, start the timer
    if up_button and round(joystick.get_axis(1))==0:
        up_change_count = 0
    #If the upbutton is pressed again within 15 frames, initiate speed boost
    elif not up_button and round(joystick.get_axis(1))==-1 and up_change_count <= 15:
        p.accel = p.boost_accel
        p.boost_timeout = p.boost_reset
    up_button = round(joystick.get_axis(1))==-1 #True if pressed


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
                #Check if any controller button was pressed down.
        elif event.type == pygame.JOYBUTTONDOWN:
            #Which controller button was pressed down
            if joystick.get_button(0): #red button
                pass
            if joystick.get_button(1): #yellow button
                p.friction = p.braking_friction
            if joystick.get_button(2): #blue button
                pass
            if joystick.get_button(3): #green button
                pass
        #Check if any controller button was released.
        elif event.type == pygame.JOYBUTTONUP:
            if not joystick.get_button(1): #yellow button
                #Reset friction
                p.friction = p.default_friction

    return False

def drawAndDelay(p):
    #fill screen with black
    screen.fill(black)
    p.draw()
    #Update the screen
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)

#Create the player
p = Player(screen, 100, 200)

#Main loop
done = False
while not done:
    #Handle any events, possibly closing the game.
    done = handleEvents()
    #Send user input to the player
    userInputToPlayer(p)
    #Update player
    p.update()
    #Draw on the screen
    drawAndDelay(p)

pygame.quit()