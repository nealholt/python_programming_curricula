'''This Python program demonstrates how to receive input from a SNES controller
like the one shown in SnesController.jpg.

snes_controller_advanced.py shows how to do more sophisticated things such
as responding to double taps and simultaneous button presses.
'''
import pygame, math

pygame.init()


#A simple self-drawing square is useful for this demonstration.
class Square:
    def __init__(self, surface):
        self.surface = surface
        self.color = blue
        self.rect = pygame.Rect(100,100,50,50)
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)


#Initialize variables:
clock = pygame.time.Clock()
surface = pygame.display.set_mode((300,300))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0
square = Square(surface)

# Initialize the joysticks
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
num_buttons = joystick.get_numbuttons()

#Main program loop
done = False
while not done:
    #Loop through all the button presses that happened since
    #the previous frame of the game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Check if any controller button was pressed down.
        elif event.type == pygame.JOYBUTTONDOWN:
            #Which controller button was pressed down?
            if joystick.get_button(0): #red button?
                square.color = red
            elif joystick.get_button(1): #yellow button?
                square.color = yellow
            elif joystick.get_button(2): #blue button?
                square.color = blue
            elif joystick.get_button(3): #green button?
                square.color = green
        #Check if any controller button was released.
        elif event.type == pygame.JOYBUTTONUP:
            #If any button was released, change the
            #square's color to white
            square.color = white
        #Check if any keyboard key was pressed down
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True

    #Any checks to a button outside the above loop will check to
    #see if that button is currently being held down.
    #Check if the left shoulder button is currently being pressed.
    if joystick.get_button(4):
        #Make the square bigger
        square.rect.width += 1
        square.rect.height += 1
    #Check if the right shoulder button is currently being pressed.
    if joystick.get_button(5):
        #Make the square smaller
        square.rect.width -= 1
        square.rect.height -= 1

    #The directional buttons or D-pad are a bit weird.
    #First we ask for the axis input. It's important to
    #round these numbers.
    x_motion = round(joystick.get_axis(0))
    y_motion = round(joystick.get_axis(1))
    #The x motion will be -1, 1, or 0 depending on which
    #direction was pushed, if any.
    if x_motion == 1:
        print('right key pressed')
    elif x_motion == -1:
        print('left key pressed')
    #The y motion will be -1, 1, or 0 depending on which
    #direction was pushed, if any.
    if y_motion == 1:
        print('down key pressed')
    elif y_motion == -1:
        print('up key pressed')

    #Move the square based on the input
    speed = 3
    square.rect.x+= x_motion * speed
    square.rect.y+= y_motion * speed

    #Draw everything
    surface.fill((0,0,0)) #fill surface with black
    square.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()