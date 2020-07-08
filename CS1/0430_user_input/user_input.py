'''
For 50 points, complete the following investigation.

This investigation is all about keyboard and mouse input, but also uses a
user-defined class called Square. There will be some questions about Square
toward the end.

1. What is the line number of the line of code that moves the square to the
left when you hold the left key?

2. What is the line number of the line of code that moves the square down when
you hold the down key?

This code responds to key press and key release separately.
3. What is the line number of the line of code that changes the square's color
when you press up?

4. What is the line number of the line of code that changes the square's color
when you release up?

Every key has a corresponding numeric value. This program prints that value.
5. What is the numeric value of the w key?

6. What is the numeric value of the space bar?

7. What is the line number of the line of code that prints the key's numeric
value?

8. What is the line number of the line of code that checks to see if a mouse
button was clicked?

9. What is the line number of the line of code that checks to see if the mouse
cursor was inside the square when it was released?

The block of indented code beginning with   class Square:   is an example of
a class. Classes are instructions for creating objects. We've already used
lots of objects including turtles and pygame rectangles. Objects are groups
of variables that begin with "self." and functions that, as usual, start with
def, but also include the argument "self"

10. What are Square's three variables?

11. What are Square's two functions?

'''
import pygame
pygame.init()

#All keyboard and mouse input will be handled by the following function
def handleEvents():
    #Check for new events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            #This does not detect if a key is held down. For that, I think you need
            #to use your own boolean, but it's worth looking into.
            print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                return True
            elif event.key == pygame.K_RIGHT:
                square.color = red
            elif event.key == pygame.K_LEFT:
                square.color = green
            elif event.key == pygame.K_UP:
                square.color = blue
            elif event.key == pygame.K_DOWN:
                square.color = yellow
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                square.color = green
            elif event.key == pygame.K_LEFT:
                square.color = red
            elif event.key == pygame.K_UP:
                square.color = yellow
            elif event.key == pygame.K_DOWN:
                square.color = blue
        #The following detects left or right mouse clicks.
        #For more on pygame mouse events see: pygame.org/docs/ref/mouse.html
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if square.rect.collidepoint(pos):
                square.color = black
        #The following detects left or right mouse clicks.
        #For more on pygame mouse events see: pygame.org/docs/ref/mouse.html
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if square.rect.collidepoint(pos):
                square.color = white
    return False


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

#Main program loop
done = False
while not done:
    done = handleEvents()
    #Detect held down keys:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        square.rect.x-=1
    if pressed[pygame.K_UP]:
        square.rect.y-=1
    if pressed[pygame.K_RIGHT]:
        square.rect.x+=1
    if pressed[pygame.K_DOWN]:
        square.rect.y+=1

    surface.fill(black) #fill surface with black
    square.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()