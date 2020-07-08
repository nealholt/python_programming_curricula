'''
https://www.youtube.com/watch?v=-3ODe9mqoDE
'''

import pygame, math

pygame.init()


width = 10
fps = 10

class Square:
    def __init__(self, surface, x, y, color):
        self.surface = surface
        self.color = color
        self.rect = pygame.Rect(x,y,width,width)
        self.direction = ""

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def move(self):
        if self.direction == "up":
            self.rect.y -= width
        elif self.direction == "down":
            self.rect.y += width
        elif self.direction == "left":
            self.rect.x -= width
        elif self.direction == "right":
            self.rect.x += width


#Initialize variables:
clock = pygame.time.Clock()
surface = pygame.display.set_mode((700,400))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0
red_square = Square(surface, 0,0, red)
blue_square = Square(surface,600,300,blue)



def outOfBounds(square):
    #Return True if square is out of bounds
    w_max,h_max = surface.get_size() #Screen width and height
    return square.rect.centerx<0 or \
            square.rect.centery<0 or \
            square.rect.centerx>w_max or \
            square.rect.centery>h_max



#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key) #Print value of key press

    #Detect held down keys:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        red_square.direction = "left"
    elif pressed[pygame.K_UP]:
        red_square.direction = "up"
    elif pressed[pygame.K_RIGHT]:
        red_square.direction = "right"
    elif pressed[pygame.K_DOWN]:
        red_square.direction = "down"

    if pressed[119]: #w
        blue_square.direction = "up"
    elif pressed[97]: #a
        blue_square.direction = "left"
    elif pressed[115]: #s
        blue_square.direction = "down"
    elif pressed[100]: #d
        blue_square.direction = "right"

    red_square.move()
    blue_square.move()

    if outOfBounds(red_square) or surface.get_at((red_square.rect.centerx,red_square.rect.centery)) == blue:
        print("red loses")
        done = True
    if outOfBounds(blue_square) or surface.get_at((blue_square.rect.centerx,blue_square.rect.centery)) == red:
        print("blue loses")
        done = True

    #surface.fill((0,0,0)) #fill surface with black
    red_square.draw()
    blue_square.draw()
    pygame.display.flip()
    #Delay to get 10 fps
    clock.tick(fps)
pygame.quit()