import pygame

def clickerCostScaling(level):
    '''Return the cost of the next level.'''
    return max(1, int(100*level**1.05)-90)

def mineCostScaling(level):
    '''Return the cost of the next level.'''
    return max(1, int(100*level**1.1)-90)

def farmCostScaling(level):
    '''Return the cost of the next level.'''
    return max(1, int(100*level**1.07)-90)


class Sprite:
    def __init__(self, name, x, y, image_file, screen):
        #Create a Sprite object
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 25)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.level = 0
        if name == "Clicker":
            self.level_up_function = clickerCostScaling
        elif name == "Farm":
            self.level_up_function = farmCostScaling
        elif name == "Mine":
            self.level_up_function = mineCostScaling

    def draw(self):
        #Draw this sprite on the screen
        white = 255,255,255
        self.screen.blit(self.image, self.rect)
        if self.name == 'Cookie':
            self.screen.blit(self.font.render('Cookies: '+str(int(self.level)),
                    True,white), (self.rect.x, self.rect.y+self.rect.height))
        else:
            self.screen.blit(self.font.render(self.name+' level: '+str(self.level),
                    True,white), (self.rect.x, self.rect.y+self.rect.height))
            self.screen.blit(self.font.render('Level up cost: '+str(self.level_up_function(self.level)),True,white),
                (self.rect.x, self.rect.y+20+self.rect.height))
