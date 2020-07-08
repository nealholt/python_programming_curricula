import pygame

black = 0,0,0

class Block:
    def __init__(self, screen, x, y, size):
        #Create a Sprite object
        self.screen = screen
        self.rect = pygame.Rect(x,y,size,size)
        self.energy = 0

    def draw(self):
        color = 100,min(255,100+self.energy*5),0
        if self.energy*5+100 > 255:
            color = max(0,100-self.energy),255,0
        pygame.draw.rect(self.screen, color, self.rect)
        #Draw black border
        pygame.draw.rect(self.screen, black, self.rect, 2)
