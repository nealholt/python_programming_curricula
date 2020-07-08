import pygame, math

pygame.init()

class Square:
    def __init__(self, surface, x,y,dx, dy, size):
        self.surface = surface
        self.color = blue
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = size

    def draw(self):
        r = pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.rect(self.surface, self.color, r)


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
            distance = math.sqrt((pos[0]-square.x)**2+(pos[1]-square.y)**2)
            dx = (pos[0]-square.x)/distance
            dy = (pos[1]-square.y)/distance
            speed = 2
            b = Square(surface, square.x, square.y, dx*speed, dy*speed, 5)
            b.color = yellow
            bullets.append(b)

    #Detect held down keys:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        square.x-=5
    if pressed[pygame.K_UP]:
        square.y-=5
    if pressed[pygame.K_RIGHT]:
        square.x+=5
    if pressed[pygame.K_DOWN]:
        square.y+=5

    surface.fill((0,0,0)) #fill surface with black
    square.draw()
    #Move and draw all the bullets
    for b in bullets:
        b.x += b.dx
        b.y += b.dy
        b.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()