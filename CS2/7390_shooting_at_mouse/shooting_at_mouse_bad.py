import pygame, math

pygame.init()

'''IMPORTANT
Slower bullets can cause rounding problems when
rectangles are used because self.rect.x always gets rounded
to an integer, but self.x can be treated like a float
for more accuracy.
'''

class Square:
    def __init__(self, surface, x,y,dx, dy, size):
        self.surface = surface
        self.color = blue
        self.rect = pygame.Rect(x,y,size,size)
        self.dx = dx
        self.dy = dy

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)


#Initialize variables:
clock = pygame.time.Clock()
surface = pygame.display.set_mode((900,500))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0
square = Square(surface, 100, 100, 0, 0, 50)

bullets = []

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #This does not detect if a key is held down.
            print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
        #The following detects left or right mouse clicks.
        #For more on pygame mouse events see: pygame.org/docs/ref/mouse.html
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            distance = math.sqrt((pos[0]-square.rect.x)**2+(pos[1]-square.rect.y)**2)
            dx = (pos[0]-square.rect.x)/distance
            dy = (pos[1]-square.rect.y)/distance
            speed = 2
            b = Square(surface, square.rect.x, square.rect.y, dx*speed, dy*speed, 5)
            b.color = yellow
            bullets.append(b)

    #Detect held down keys:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        square.rect.x-=5
    if pressed[pygame.K_UP]:
        square.rect.y-=5
    if pressed[pygame.K_RIGHT]:
        square.rect.x+=5
    if pressed[pygame.K_DOWN]:
        square.rect.y+=5

    surface.fill((0,0,0)) #fill surface with black
    square.draw()
    #Move and draw all the bullets
    for b in bullets:
        b.rect.x += b.dx
        b.rect.y += b.dy
        b.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()