import pygame
pygame.init()

#Dwell on each image for this many frames.
dwell_reset = 5

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
    #Image source: www.artstation.com/artwork/8L2dQ
    sheet = pygame.image.load('dominic-garcia-tumblr-ojn6bb7cfk1w36evao1-1280.jpg')

    r = sheet.get_rect()
    rows = 3
    columns = 5
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

    screen.fill((255,255,255)) #fill screen with white
    sprite.draw()
    sprite.advanceImage()
    pygame.display.flip()
    #Delay to get 10 fps
    clock.tick(10)
pygame.quit()