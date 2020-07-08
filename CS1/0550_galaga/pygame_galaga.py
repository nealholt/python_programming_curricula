# https://youtu.be/aHmtOrrLmxg
import pygame, math, random

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
screen_width = 850
screen_height = 600
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

class Square:
    def __init__(self, color, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = 'E'
        self.speed = 5

    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed

    def collided(self, other_rect):
        #Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


#Build a square
sq = Square(green,200,200,100,100)

bullets = []
enemies = []

#Main program loop
done = False
while not done:
    #Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key) #Print value of key press
            if event.key==119: #w
                sq.direction = 'N'
            if event.key==97: #a
                sq.direction = 'W'
            if event.key==115: #s
                sq.direction = 'S'
            if event.key==100: #d
                sq.direction = 'E'
            if event.key==32: #spacebar
                #Fire a bullet
                spawnx = sq.rect.x + sq.rect.width/2 - 10
                b = Square(red, spawnx,sq.rect.y, 20,20)
                b.direction = 'N'
                b.speed = 10
                bullets.append(b)
    
    #Update game objects
    for b in bullets:
        b.move()
    for e in enemies:
        e.move()
    sq.move()
    #spawn enemies on the top of the screen and tell them to move down
    if random.randint(1,30) == 15: #15 doesn't matter
        x = random.randint(0,screen_width-40)
        e = Square(yellow, x,-40, 40,40)
        e.direction = 'S'
        enemies.append(e)
    #Check for collisions
    '''for b in bullets:
        for e in enemies:
            if b.collided(e.rect):
                #e.color = white #TESTING
                enemies.remove(e)
                bullets.remove(b)'''
    for i in reversed(range(len(bullets))):
        for j in reversed(range(len(enemies))):
            if bullets[i].collided(enemies[j].rect):
                #e.color = white #TESTING
                del enemies[j]
                del bullets[i]
                break

    #All the drawing
    surface.fill(black) #fill surface with black
    for b in bullets:
        b.draw(surface)
    for e in enemies:
        e.draw(surface)
    sq.draw(surface)
    pygame.display.flip()
    clock.tick(30) #30 FPS
pygame.quit()
exit()
