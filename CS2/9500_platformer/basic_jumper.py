import pygame, math

pygame.init()

class Square:
    def __init__(self, surface):
        self.surface = surface
        self.color = blue
        self.rect = pygame.Rect(100,100,50,50)
        self.dy = 0

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
gravity = 1

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #This does not detect if a key is held down. For that, I think you need
            #to use your own boolean, but it's worth looking into.
            print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:
                square.rect.x += 5
            elif event.key == pygame.K_LEFT:
                square.rect.x -= 5
            elif event.key == pygame.K_UP:
                square.dy = -20

    #Increase downward acceleration
    square.dy += gravity
    #Move square up or down
    square.rect.y += square.dy
    #Stop square at bottom of screen
    if square.rect.y+square.rect.height > 300:
        square.rect.y = 300-square.rect.height

    surface.fill((0,0,0)) #fill surface with black
    square.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()