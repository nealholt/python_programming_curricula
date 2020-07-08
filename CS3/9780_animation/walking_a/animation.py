import pygame

pygame.init()

#Dwell on each image for this many frames.
dwell_reset = 5

#The following are image sequences and corresponding x,y movements:
leftwalk_sequence = ['lwalk1','lwalk2','lwalk3']
leftwalk_motion = [(-10,0), (-10,0), (-10,0)]

rightwalk_sequence = ['rwalk1','rwalk2','rwalk3']
rightwalk_motion = [(10,0), (10,0), (10,0)]

downwalk_sequence = ['dwalk1','dwalk2','dwalk3']
downwalk_motion = [(0,10), (0,10), (0,10)]

upwalk_sequence = ['upwalk1','upwalk2','upwalk3']
upwalk_motion = [(0,-10), (0,-10), (0,-10)]


class AnimatedSprite:
    def __init__(self, screen, x, y, frames):
        self.screen = screen
        #x and y are the center of this object
        self.x = x
        self.y = y
        #A dictionary of all the images
        self.frames = frames
        self.default_frame = 'dwalk3'
        self.frame_name = 'dwalk3'
        self.rect = self.frames[self.frame_name].get_rect()
        self.sequence = []
        self.motion = []
        #Dwell is a countdown that lets sprite dwell on each frame of an image
        #for longer to make the transition look smoother.
        self.dwell = dwell_reset



    def draw(self):

        screen.blit(self.frames[self.frame_name],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))



def strip_from_sheet():
    '''Strips individual frames from specific sprite sheet.'''
    frames = {} #dictionary
    #Image source: sprite_sheet_test_by_pfunked
    #pfunked.deviantart.com/art/Sprite-Sheet-test-80837813
    sheet = pygame.image.load('template_c.png')
    rect = pygame.Rect(64, 21, 29, 37)
    frames['dwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(96, 21, 29, 37)
    frames['dwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(0, 21, 29, 37)
    frames['dwalk3'] = sheet.subsurface(rect)

    rect = pygame.Rect(64, 85, 29, 37)
    frames['upwalk1'] = sheet.subsurface(rect)

    rect = pygame.Rect(96, 85, 29, 37)
    frames['upwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(32, 85, 29, 37)
    frames['upwalk3'] = sheet.subsurface(rect)

    rect = pygame.Rect(192, 85, 29, 37)
    frames['rwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(224, 85, 29, 37)
    frames['rwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(160, 85, 29, 37)
    frames['rwalk3'] = sheet.subsurface(rect)

    rect = pygame.Rect(192, 21, 29, 37)
    frames['lwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(224, 21, 29, 37)
    frames['lwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(160, 21, 29, 37)
    frames['lwalk3'] = sheet.subsurface(rect)

    return frames




clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
frames = strip_from_sheet()
dimensions = (29,37)
speed = 3
sprite = AnimatedSprite(screen, 250, 300, frames)


#Reminder: this is how you resize the image if you want.
scaling = 2
dimensions = (dimensions[0]*scaling,dimensions[1]*scaling)
for key in frames.keys():
    frames[key] = pygame.transform.scale(
                            frames[key],
                            dimensions)


#Draw all images on the screen
done = False
counter = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    #moves the paddle when u press left and right
    if pressed[pygame.K_LEFT]:
        if counter == 1:
            sprite.frame_name = "lwalk3"
        if counter == 3:
            sprite.frame_name = "lwalk2"
        if counter == 5:
            sprite.frame_name = "lwalk1"
        counter = counter + 1
        sprite.default_frame = "lwalk2"
        sprite.x = sprite.x -speed

        #sprite.setSequence(leftwalk_sequence, leftwalk_motion)


    if pressed[pygame.K_RIGHT]:
        if counter == 1:
            sprite.frame_name = "rwalk3"
        if counter == 3:
            sprite.frame_name = "rwalk1"
        if counter == 5:
            sprite.frame_name = "rwalk2"
        counter = counter + 1
        sprite.default_frame = "rwalk3"
        sprite.x = sprite.x +speed
        #sprite.setSequence(rightwalk_sequence, rightwalk_motion)
        pass
    if pressed[pygame.K_DOWN]:
        if counter == 1:
            sprite.frame_name = "dwalk3"
        if counter == 3:
            sprite.frame_name = "dwalk1"
        if counter == 5:
            sprite.frame_name = "dwalk2"
        counter = counter + 1
        sprite.default_frame = "dwalk3"
        sprite.y = sprite.y +speed
        #sprite.setSequence(downwalk_sequence, downwalk_motion)
    if pressed[pygame.K_UP]:
        if counter == 1:
            sprite.frame_name = "upwalk3"
        if counter == 3:
            sprite.frame_name = "upwalk1"
        if counter == 5:
            sprite.frame_name = "upwalk2"
        counter = counter + 1
        sprite.default_frame = "upwalk3"
        sprite.y = sprite.y -speed
        #sprite.setSequence(upwalk_sequence, upwalk_motion)
    if counter >= 6:
        counter = 1
    screen.fill((255,255,255)) #fill screen with black
    sprite.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()