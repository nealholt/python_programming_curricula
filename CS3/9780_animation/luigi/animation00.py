'''
This is a good search term:
https://www.google.com/search?q=grid+aligned+spritesheet
'''

import pygame
pygame.init()

class AnimatedSprite:
    def __init__(self, screen, x, y, frames):
        self.screen = screen
        self.x = x
        self.y = y
        self.index = 0
        self.frames = frames
        self.rect = self.frames[self.index].get_rect()

    def advanceImage(self):
        self.index = (self.index+1)%len(self.frames)

    def draw(self):
        screen.blit(self.frames[self.index],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))



def strip_from_sheet():
    '''Strips individual frames from specific sprite sheet.'''
    #Image source: deviantart.com/xabring/art/Luigi-Side-View-Battle-for-RPG-Maker-MV-575328113
    #Image source: deviantart.com/xabring/art/Luigi-Side-View-Luigi-DreamTeam-694186193
    sheet = pygame.image.load('luigi_higher_res.png')

    r = sheet.get_rect()
    rows = 6
    columns = 9
    img_width = r.w/columns
    img_height = r.h/rows

    frames = []
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(col*img_width, row*img_height, img_width, img_height)
            frames.append(sheet.subsurface(rect))
    return frames




clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

frames = strip_from_sheet()

dimensions = frames[0].get_rect()
#Reminder: this is how you resize the image if you want.
scaling = 1
dimensions = (dimensions.w*scaling,dimensions.h*scaling)
for i in range(len(frames)):
    frames[i] = pygame.transform.scale(
                            frames[i],
                            dimensions)

sprite = AnimatedSprite(screen, 400, 300, frames)



#Draw all images on the screen
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0)) #fill screen with black
    sprite.draw()
    sprite.advanceImage()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(5)
pygame.quit()