'''
This is a good search term:
https://www.google.com/search?q=grid+aligned+spritesheet

Next steps:
    1 horizontal flip
    2 labeling sets of images
    3 incorporating movement
'''

import pygame
pygame.init()

frame_sets = [(0,2),(3,5),(6,8),(9,11),(12,14),(15,17),
              (18,20),(21,23),(24,26),(27,29),(30,32),(33,35),
              (36,38),(39,41),(42,44),(45,47),(48,50),(51,53)]
set_index = 0

class AnimatedSprite:
    def __init__(self, screen, x, y, frames):
        self.screen = screen
        self.x = x
        self.y = y
        self.index = 0
        self.frames = frames
        self.rect = self.frames[self.index].get_rect()

    def advanceImage(self):
        self.index = (self.index+1)%(frame_sets[set_index][1]+1)
        if self.index<frame_sets[set_index][0]:
            self.index = frame_sets[set_index][0]
        #print(self.index)

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
scaling = 3
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
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:
                set_index = (set_index+1)%len(frame_sets)
            elif event.key == pygame.K_LEFT:
                set_index = 1
            elif event.key == pygame.K_UP:
                set_index = 2
            elif event.key == pygame.K_DOWN:
                set_index = 3

    screen.fill((0,0,0)) #fill screen with black
    sprite.draw()
    sprite.advanceImage()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(5)
pygame.quit()