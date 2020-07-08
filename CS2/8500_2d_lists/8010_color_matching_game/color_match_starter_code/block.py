import pygame

black = 0,0,0

class Block:
    def __init__(self, screen, x, y, color, size):
        #Create a Sprite object
        self.screen = screen
        self.rect = pygame.Rect(x,y,size,size)
        self.color = color

    def draw(self):
        if self.color != None:
            pygame.draw.rect(self.screen, self.color, self.rect)
            #Draw black border
            pygame.draw.rect(self.screen, black, self.rect, 2)
