import pygame

pygame.init()

#The following are image sequences and corresponding x,y movements:
walk_sequence = ['walk1','walk2','walk3','walk4','walk5','walk6','walk7','walk8']

class AnimatedSprite:
    def __init__(self, screen, x, y, frames):
        self.screen = screen
        #x and y are the center of this object
        self.x = x
        self.y = y
        #A dictionary of all the images
        self.frames = frames
        self.default_frame = 'stand'
        self.frame_name = 'stand'
        self.rect = self.frames[self.frame_name].get_rect()
        self.sequence = []
        self.motion = []

    def draw(self):
        screen.blit(self.frames[self.frame_name],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))


def strip_from_sheet():
    '''Strips individual frames from specific sprite sheet.'''
    frames = {} #dictionary
    #Image source: sprite_sheet_test_by_pfunked
    #pfunked.deviantart.com/art/Sprite-Sheet-test-80837813
    sheet = pygame.image.load('sprite_sheet_test_by_pfunked.png')
    rect = pygame.Rect(0, 0, 64, 128)
    frames['stand'] = sheet.subsurface(rect)
    rect = pygame.Rect(64, 0, 64, 128)
    frames['crouch'] = sheet.subsurface(rect)
    rect = pygame.Rect(142, 0, 64, 128)
    frames['fall'] = sheet.subsurface(rect)
    rect = pygame.Rect(230, 0, 80, 128)
    frames['leap'] = sheet.subsurface(rect)

    rect = pygame.Rect(333, 0, 73, 128)
    frames['roll1'] = sheet.subsurface(rect)
    rect = pygame.Rect(418, 0, 75, 128)
    frames['roll2'] = sheet.subsurface(rect)
    rect = pygame.Rect(518, 0, 70, 128)
    frames['roll3'] = sheet.subsurface(rect)
    rect = pygame.Rect(620, 0, 65, 128)
    frames['roll4'] = sheet.subsurface(rect)
    rect = pygame.Rect(715, 0, 73, 128)
    frames['roll5'] = sheet.subsurface(rect)

    rect = pygame.Rect(33, 128, 50, 128)
    frames['walk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(152, 128, 66, 128)
    frames['walk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(270, 128, 97, 128)
    frames['walk3'] = sheet.subsurface(rect)
    rect = pygame.Rect(407, 128, 70, 128)
    frames['walk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(32, 256, 50, 128)
    frames['walk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(151, 256, 66, 128)
    frames['walk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(270, 256, 96, 128)
    frames['walk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(407, 256, 70, 128)
    frames['walk8'] = sheet.subsurface(rect)

    rect = pygame.Rect(531, 128, 74, 128)
    frames['hurdle1'] = sheet.subsurface(rect)
    rect = pygame.Rect(667, 128, 68, 128)
    frames['hurdle2'] = sheet.subsurface(rect)
    rect = pygame.Rect(786, 128, 106, 128)
    frames['hurdle3'] = sheet.subsurface(rect)

    rect = pygame.Rect(532, 294, 52, 128)
    frames['ascend1'] = sheet.subsurface(rect)
    rect = pygame.Rect(635, 310, 45, 147)
    frames['ascend2'] = sheet.subsurface(rect)
    rect = pygame.Rect(731, 314, 45, 134)
    frames['ascend3'] = sheet.subsurface(rect)
    rect = pygame.Rect(829, 284, 43, 133)
    frames['ascend4'] = sheet.subsurface(rect)
    rect = pygame.Rect(921, 255, 66, 131)
    frames['ascend5'] = sheet.subsurface(rect)

    rect = pygame.Rect(8, 384, 101, 128)
    frames['crawl1'] = sheet.subsurface(rect)
    #rect = pygame.Rect(141, 444, 96, 68)
    rect = pygame.Rect(141, 384, 96, 120)
    frames['crawl2'] = sheet.subsurface(rect)
    #rect = pygame.Rect(264, 447, 100, 65)
    rect = pygame.Rect(264, 384, 100, 128)
    frames['crawl3'] = sheet.subsurface(rect)
    return frames


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
frames = strip_from_sheet()


sprite = AnimatedSprite(screen, 250, 300, frames)

counter = 0
#Draw all images on the screen
done = False
while not done:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        sprite.frame_name = walk_sequence[counter]
        sprite.x += 5
        counter += 1

    if counter == len(walk_sequence):
        counter = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill((0,0,0)) #fill screen with black
    sprite.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()