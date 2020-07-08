import pygame, math, random

pygame.init()

class Arrow:
    def __init__(self, surface, dx,dy, color):
        self.surface = surface
        self.color = color
        self.dx = dx
        self.dy = dy
        self.rect = pygame.Rect(arrow_start_x,arrow_start_y,10,10)

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.rect)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        #Change dy due to gravity
        self.dy = self.dy + 0.4


#Initialize variables:
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 700
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
black = 0,0,0
colors = [green, red, blue, yellow]

arrow_start_x = screen_width/2
arrow_start_y = screen_height-1

arrows = []

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
        #The following detects left or right mouse clicks.
        #For more on pygame mouse events see: pygame.org/docs/ref/mouse.html
        elif event.type == pygame.MOUSEBUTTONUP:
            #Create arrow. reset impulse to zero
            dx = random.random()*20-10
            dy = -15-random.random()*10
            color = colors[random.randint(0,len(colors)-1)]
            arrows.append(Arrow(surface, dx,dy, color))

    #move all arrows
    for a in arrows:
        a.move()
    #remove arrows that exit bottom of screen
    for i in reversed(range(len(arrows))):
        if arrows[i].rect.y > screen_height:
            del arrows[i]

    surface.fill(black)

    #arrows
    for a in arrows:
        a.draw()

    pygame.display.flip()
    pygame.display.update()
    #Delay to get 30 fps
    clock.tick(30)

pygame.quit()