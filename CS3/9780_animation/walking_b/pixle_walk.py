
import pygame

pygame.init()

#Dwell on each image for this many frames.
dwell_reset = 6

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
    sheet = pygame.image.load('pixle_walk.png')
    rect = pygame.Rect(16, 140, 35, 50)
    frames['dwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(80, 140, 35, 50)
    frames['dwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(144, 140, 35, 50)
    frames['dwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 140, 35, 50)
    frames['dwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(272, 140, 35, 50)
    frames['dwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(335, 140, 35, 50)
    frames['dwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(399, 140, 35, 50)
    frames['dwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(463, 140, 35, 50)
    frames['dwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(527, 140, 35, 50)
    frames['dwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(15, 11, 35, 50)
    frames['upwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(80, 11, 35, 50)
    frames['upwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(145, 11, 35, 50)
    frames['upwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 11, 35, 50)
    frames['upwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(271, 11, 35, 50)
    frames['upwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(336, 11, 35, 50)
    frames['upwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(399, 11, 35, 50)
    frames['upwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(465, 11, 35, 50)
    frames['upwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(527, 11, 35, 50)
    frames['upwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(20, 205, 35, 50)
    frames['rwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(83, 205, 35, 50)
    frames['rwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(148, 205, 35, 50)
    frames['rwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 205, 35, 50)
    frames['rwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(272, 205, 35, 50)
    frames['rwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(334, 205, 35, 50)
    frames['rwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(401, 205, 35, 50)
    frames['rwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(466, 205, 35, 50)
    frames['rwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(530, 205, 35, 50)
    frames['rwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(14, 76, 35, 50)
    frames['lwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(78, 76, 35, 50)
    frames['lwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(142, 76, 35, 50)
    frames['lwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 76, 35, 50)
    frames['lwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(269, 76, 35, 50)
    frames['lwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(334, 76, 35, 50)
    frames['lwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(399, 76, 35, 50)
    frames['lwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(463, 76, 35, 50)
    frames['lwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(529, 76, 35, 50)
    frames['lwalk9'] = sheet.subsurface(rect)

    return frames

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
frames = strip_from_sheet()
dimensions = (29,37)
speed = 3
sprite = AnimatedSprite(screen, 250, 300, frames)
#background = pygame.image.load("background.jpg")


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
    if pressed[pygame.K_a]:
        if counter == 1:
            sprite.frame_name = "lwalk1"
        if counter == 3:
            sprite.frame_name = "lwalk2"
        if counter == 5:
            sprite.frame_name = "lwalk3"
        if counter == 7:
            sprite.frame_name = "lwalk4"
        if counter == 9:
            sprite.frame_name = "lwalk5"
        if counter == 11:
            sprite.frame_name = "lwalk6"
        if counter == 13:
            sprite.frame_name = "lwalk7"
        if counter == 15:
            sprite.frame_name = "lwalk8"
        if counter == 17:
            sprite.frame_name = "lwalk9"
        counter = counter + 1
        sprite.default_frame = "lwalk2"
        sprite.x = sprite.x -speed

        #sprite.setSequence(leftwalk_sequence, leftwalk_motion)

    if pressed[pygame.K_d]:
        if counter == 1:
            sprite.frame_name = "rwalk1"
        if counter == 3:
            sprite.frame_name = "rwalk2"
        if counter == 5:
            sprite.frame_name = "rwalk3"
        if counter == 7:
            sprite.frame_name = "rwalk4"
        if counter == 9:
            sprite.frame_name = "rwalk5"
        if counter == 11:
            sprite.frame_name = "rwalk6"
        if counter == 13:
            sprite.frame_name = "rwalk7"
        if counter == 15:
            sprite.frame_name = "rwalk8"
        if counter == 17:
            sprite.frame_name = "rwalk9"
        counter = counter + 1
        sprite.default_frame = "rwalk3"
        sprite.x = sprite.x +speed
        #sprite.setSequence(rightwalk_sequence, rightwalk_motion)
        pass
    if pressed[pygame.K_s]:
        if counter == 1:
            sprite.frame_name = "dwalk1"
        if counter == 3:
            sprite.frame_name = "dwalk2"
        if counter == 5:
            sprite.frame_name = "dwalk3"
        if counter == 7:
            sprite.frame_name = "dwalk4"
        if counter == 9:
            sprite.frame_name = "dwalk5"
        if counter == 11:
            sprite.frame_name = "dwalk6"
        if counter == 13:
            sprite.frame_name = "dwalk7"
        if counter == 15:
            sprite.frame_name = "dwalk8"
        if counter == 17:
            sprite.frame_name = "dwalk9"
        counter = counter + 1
        sprite.default_frame = "dwalk3"
        sprite.y = sprite.y +speed
        #sprite.setSequence(downwalk_sequence, downwalk_motion)
    if pressed[pygame.K_w]:
        if counter == 1:
            sprite.frame_name = "upwalk1"
        if counter == 3:
            sprite.frame_name = "upwalk2"
        if counter == 5:
            sprite.frame_name = "upwalk3"
        if counter == 7:
            sprite.frame_name = "upwalk4"
        if counter == 9:
            sprite.frame_name = "upwalk5"
        if counter == 11:
            sprite.frame_name = "upwalk6"
        if counter == 13:
            sprite.frame_name = "upwalk7"
        if counter == 15:
            sprite.frame_name = "upwalk8"
        if counter == 17:
            sprite.frame_name = "upwalk9"
        counter = counter + 1
        sprite.default_frame = "upwalk3"
        sprite.y = sprite.y -speed
        #sprite.setSequence(upwalk_sequence, upwalk_motion)
    if counter >= 17:
        counter = 1
    screen.fill((0,0,0)) #fill screen with white
    sprite.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()