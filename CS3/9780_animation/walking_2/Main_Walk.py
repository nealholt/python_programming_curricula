
import pygame

pygame.init()

#Dwell on each image for this many frames_2.
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


class Animatedsprite:
    def __init__(self, screen, x, y, frames_2):
        self.screen = screen
        #x and y are the center of this object
        self.x = x
        self.y = y
        #A dictionary of all the images
        self.frames_2 = frames_2
        self.default_frame = 'dwalk3'
        self.frame_name = 'dwalk3'
        self.rect = self.frames_2[self.frame_name].get_rect()
        self.sequence = []
        self.motion = []
        #Dwell is a countdown that lets sprite_orc dwell on each frame of an image
        #for longer to make the transition look smoother.
        self.dwell = dwell_reset

    def draw(self):

        screen.blit(self.frames_2[self.frame_name],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))

def load_image(name, colorkey=None):
    #Load the image from file
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print('ERROR: Failed to load image named "'+name+'". Probably a typo.')
        pygame.quit()
        exit()
    #This next line creates a copy that will draw more quickly on the screen.
    image = image.convert()
    #If colorkey is None, then don't worry about transparency
    if colorkey is not None:
        #colorkey of -1 means that the color of upper left most pixel should
        #be used as transparency color.
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        '''The optional flags argument can be set to pygame.RLEACCEL to provide better performance on non accelerated displays. An RLEACCEL Surface will be slower to modify, but quicker to blit as a source.'''
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    #Return the image and its rectangle
    return image, image.get_rect()

def strip_from_sheet(image_file):
    '''Strips individual frames_2 from specific sprite_orc sheet.'''
    frames_2 = {} #dictionary
    #Image source: sprite_orc_sheet_test_by_pfunked
    #pfunked.deviantart.com/art/sprite_orc-Sheet-test-80837813
    sheet,_ = load_image(image_file, -1)
    rect = pygame.Rect(16, 140, 35, 50)
    frames_2['dwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(80, 140, 35, 50)
    frames_2['dwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(144, 140, 35, 50)
    frames_2['dwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 140, 35, 50)
    frames_2['dwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(272, 140, 35, 50)
    frames_2['dwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(335, 140, 35, 50)
    frames_2['dwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(399, 140, 35, 50)
    frames_2['dwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(463, 140, 35, 50)
    frames_2['dwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(527, 140, 35, 50)
    frames_2['dwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(15, 11, 35, 50)
    frames_2['upwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(80, 11, 35, 50)
    frames_2['upwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(145, 11, 35, 50)
    frames_2['upwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 11, 35, 50)
    frames_2['upwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(271, 11, 35, 50)
    frames_2['upwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(336, 11, 35, 50)
    frames_2['upwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(399, 11, 35, 50)
    frames_2['upwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(465, 11, 35, 50)
    frames_2['upwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(527, 11, 35, 50)
    frames_2['upwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(20, 205, 35, 50)
    frames_2['rwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(83, 205, 35, 50)
    frames_2['rwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(148, 205, 35, 50)
    frames_2['rwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 205, 35, 50)
    frames_2['rwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(272, 205, 35, 50)
    frames_2['rwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(334, 205, 35, 50)
    frames_2['rwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(401, 205, 35, 50)
    frames_2['rwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(466, 205, 35, 50)
    frames_2['rwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(530, 205, 35, 50)
    frames_2['rwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(14, 76, 35, 50)
    frames_2['lwalk1'] = sheet.subsurface(rect)
    rect = pygame.Rect(78, 76, 35, 50)
    frames_2['lwalk2'] = sheet.subsurface(rect)
    rect = pygame.Rect(142, 76, 35, 50)
    frames_2['lwalk3'] = sheet.subsurface(rect)
    #Next set
    rect = pygame.Rect(208, 76, 35, 50)
    frames_2['lwalk4'] = sheet.subsurface(rect)
    rect = pygame.Rect(269, 76, 35, 50)
    frames_2['lwalk5'] = sheet.subsurface(rect)
    rect = pygame.Rect(334, 76, 35, 50)
    frames_2['lwalk6'] = sheet.subsurface(rect)
    rect = pygame.Rect(399, 76, 35, 50)
    frames_2['lwalk7'] = sheet.subsurface(rect)
    rect = pygame.Rect(463, 76, 35, 50)
    frames_2['lwalk8'] = sheet.subsurface(rect)
    rect = pygame.Rect(529, 76, 35, 50)
    frames_2['lwalk9'] = sheet.subsurface(rect)

    rect = pygame.Rect(581, 76, 35, 50)
    frames_2['lpunch'] = sheet.subsurface(rect)
    rect = pygame.Rect(585, 205, 35, 50)
    frames_2['rpunch'] = sheet.subsurface(rect)
    rect = pygame.Rect(585, 11, 35, 50)
    frames_2['uppunch'] = sheet.subsurface(rect)
    rect = pygame.Rect(585, 140, 35, 50)
    frames_2['dpunch'] = sheet.subsurface(rect)

    return frames_2

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
frames_2 = strip_from_sheet('orc_walk.png')
dimensions = (29,37)
speed = 3
sprite_orc = Animatedsprite(screen, 250, 300, frames_2)
direction_1 = 'north'
direction_2 = 'north'


#Reminder: this is how you resize the image if you want.
scaling = 3
dimensions = (dimensions[0]*scaling,dimensions[1]*scaling)
for key in frames_2.keys():
    frames_2[key] = pygame.transform.scale(
                            frames_2[key],
                            dimensions)

frames_1 = strip_from_sheet('pixle_walk.png')
sprite_man = Animatedsprite(screen, 250, 300, frames_1)
dimensions = (29,37)

#Reminder: this is how you resize the image if you want.
scaling = 3
dimensions = (dimensions[0]*scaling,dimensions[1]*scaling)
for key in frames_1.keys():
    frames_1[key] = pygame.transform.scale(
                            frames_1[key],
                            dimensions)

#Draw all images on the screen
done = False
counter_1 = 1
counter_2 = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    #moves the paddle when u press left and right

    if pressed[pygame.K_LEFT]:
        direction_1 = 'west'
        if counter_2 == 1:
            sprite_orc.frame_name = "lwalk1"
        if counter_2 == 3:
            sprite_orc.frame_name = "lwalk2"
        if counter_2 == 5:
            sprite_orc.frame_name = "lwalk3"
        if counter_2 == 7:
            sprite_orc.frame_name = "lwalk4"
        if counter_2 == 9:
            sprite_orc.frame_name = "lwalk5"
        if counter_2 == 11:
            sprite_orc.frame_name = "lwalk6"
        if counter_2 == 13:
            sprite_orc.frame_name = "lwalk7"
        if counter_2 == 15:
            sprite_orc.frame_name = "lwalk8"
        if counter_2 == 17:
            sprite_orc.frame_name = "lwalk9"
        counter_2 = counter_2 + 1
        sprite_orc.default_frame = "lwalk2"
        sprite_orc.x = sprite_orc.x -speed
        #sprite_orc.setSequence(leftwalk_sequence, leftwalk_motion)
    if pressed[pygame.K_RIGHT]:
        direction_1 = 'east'
        if counter_2 == 1:
            sprite_orc.frame_name = "rwalk1"
        if counter_2 == 3:
            sprite_orc.frame_name = "rwalk2"
        if counter_2 == 5:
            sprite_orc.frame_name = "rwalk3"
        if counter_2 == 7:
            sprite_orc.frame_name = "rwalk4"
        if counter_2 == 9:
            sprite_orc.frame_name = "rwalk5"
        if counter_2 == 11:
            sprite_orc.frame_name = "rwalk6"
        if counter_2 == 13:
            sprite_orc.frame_name = "rwalk7"
        if counter_2 == 15:
            sprite_orc.frame_name = "rwalk8"
        if counter_2 == 17:
            sprite_orc.frame_name = "rwalk9"
        counter_2 = counter_2 + 1
        sprite_orc.default_frame = "rwalk3"
        sprite_orc.x = sprite_orc.x +speed
        #sprite_orc.setSequence(rightwalk_sequence, rightwalk_motion)
        pass
    if pressed[pygame.K_DOWN]:
        direction_1 = 'south'
        if counter_2 == 1:
            sprite_orc.frame_name = "dwalk1"
        if counter_2 == 3:
            sprite_orc.frame_name = "dwalk2"
        if counter_2 == 5:
            sprite_orc.frame_name = "dwalk3"
        if counter_2 == 7:
            sprite_orc.frame_name = "dwalk4"
        if counter_2 == 9:
            sprite_orc.frame_name = "dwalk5"
        if counter_2 == 11:
            sprite_orc.frame_name = "dwalk6"
        if counter_2 == 13:
            sprite_orc.frame_name = "dwalk7"
        if counter_2 == 15:
            sprite_orc.frame_name = "dwalk8"
        if counter_2 == 17:
            sprite_orc.frame_name = "dwalk9"
        counter_2 = counter_2 + 1
        sprite_orc.default_frame = "dwalk3"
        sprite_orc.y = sprite_orc.y +speed
        #sprite_orc.setSequence(downwalk_sequence, downwalk_motion)
    if pressed[pygame.K_UP]:
        direction_1 = 'north'
        if counter_2 == 1:
            sprite_orc.frame_name = "upwalk1"
        if counter_2 == 3:
            sprite_orc.frame_name = "upwalk2"
        if counter_2 == 5:
            sprite_orc.frame_name = "upwalk3"
        if counter_2 == 7:
            sprite_orc.frame_name = "upwalk4"
        if counter_2 == 9:
            sprite_orc.frame_name = "upwalk5"
        if counter_2 == 11:
            sprite_orc.frame_name = "upwalk6"
        if counter_2 == 13:
            sprite_orc.frame_name = "upwalk7"
        if counter_2 == 15:
            sprite_orc.frame_name = "upwalk8"
        if counter_2 == 17:
            sprite_orc.frame_name = "upwalk9"
        counter_2 = counter_2 + 1
        sprite_orc.default_frame = "upwalk3"
        sprite_orc.y = sprite_orc.y -speed
        #sprite_orc.setSequence(upwalk_sequence, upwalk_motion)

      #upward punch
    if pressed[pygame.K_0] and direction_1 == 'north':
        sprite_orc.frame_name = "uppunch"
   # else:
        #sprite_man.frame_name = "upwalk1"
    #left punch
    if pressed[pygame.K_0] and direction_1 == 'west':
        sprite_orc.frame_name = "lpunch"
#    else:
        #sprite_man.frame_name = "lwalk1"
    #right punch
    if pressed[pygame.K_0] and direction_1 == 'east':
        sprite_orc.frame_name = "rpunch"
    #else:
     #   sprite_man.frame_name = "rwalk1"
    #down punch
    if pressed[pygame.K_0] and direction_1 == 'south':
        sprite_orc.frame_name = "dpunch"
   # else:
    #    sprite_man.frame_name = "dwalk1"
    #    sprite_man.frame_name = "dwalk1"


    if pressed[pygame.K_a]:
        direction_2 = 'west'
        if counter_1 == 1:
            sprite_man.frame_name = "lwalk1"
        if counter_1 == 3:
            sprite_man.frame_name = "lwalk2"
        if counter_1 == 5:
            sprite_man.frame_name = "lwalk3"
        if counter_1 == 7:
            sprite_man.frame_name = "lwalk4"
        if counter_1 == 9:
            sprite_man.frame_name = "lwalk5"
        if counter_1 == 11:
            sprite_man.frame_name = "lwalk6"
        if counter_1 == 13:
            sprite_man.frame_name = "lwalk7"
        if counter_1 == 15:
            sprite_man.frame_name = "lwalk8"
        if counter_1 == 17:
            sprite_man.frame_name = "lwalk9"
        counter_1 = counter_1 + 1
        sprite_man.default_frame = "lwalk2"
        sprite_man.x = sprite_man.x -speed
        #sprite_man.setSequence(leftwalk_sequence, leftwalk_motion)
    if pressed[pygame.K_d]:
        direction_2 = 'east'
        if counter_1 == 1:
            sprite_man.frame_name = "rwalk1"
        if counter_1 == 3:
            sprite_man.frame_name = "rwalk2"
        if counter_1 == 5:
            sprite_man.frame_name = "rwalk3"
        if counter_1 == 7:
            sprite_man.frame_name = "rwalk4"
        if counter_1 == 9:
            sprite_man.frame_name = "rwalk5"
        if counter_1 == 11:
            sprite_man.frame_name = "rwalk6"
        if counter_1 == 13:
            sprite_man.frame_name = "rwalk7"
        if counter_1 == 15:
            sprite_man.frame_name = "rwalk8"
        if counter_1 == 17:
            sprite_man.frame_name = "rwalk9"
        counter_1 = counter_1 + 1
        sprite_man.default_frame = "rwalk3"
        sprite_man.x = sprite_man.x +speed
        #sprite_man.setSequence(rightwalk_sequence, rightwalk_motion)
        pass
    if pressed[pygame.K_s]:
        direction_2 = 'south'
        if counter_1 == 1:
            sprite_man.frame_name = "dwalk1"
        if counter_1 == 3:
            sprite_man.frame_name = "dwalk2"
        if counter_1 == 5:
            sprite_man.frame_name = "dwalk3"
        if counter_1 == 7:
            sprite_man.frame_name = "dwalk4"
        if counter_1 == 9:
            sprite_man.frame_name = "dwalk5"
        if counter_1 == 11:
            sprite_man.frame_name = "dwalk6"
        if counter_1 == 13:
            sprite_man.frame_name = "dwalk7"
        if counter_1 == 15:
            sprite_man.frame_name = "dwalk8"
        if counter_1 == 17:
            sprite_man.frame_name = "dwalk9"
        counter_1 = counter_1 + 1
        sprite_man.default_frame = "dwalk3"
        sprite_man.y = sprite_man.y +speed
        #sprite_man.setSequence(downwalk_sequence, downwalk_motion)
    if pressed[pygame.K_w]:
        direction_2 = 'north'
        if counter_1 == 1:
            sprite_man.frame_name = "upwalk1"
        if counter_1 == 3:
            sprite_man.frame_name = "upwalk2"
        if counter_1 == 5:
            sprite_man.frame_name = "upwalk3"
        if counter_1 == 7:
            sprite_man.frame_name = "upwalk4"
        if counter_1 == 9:
            sprite_man.frame_name = "upwalk5"
        if counter_1 == 11:
            sprite_man.frame_name = "upwalk6"
        if counter_1 == 13:
            sprite_man.frame_name = "upwalk7"
        if counter_1 == 15:
            sprite_man.frame_name = "upwalk8"
        if counter_1 == 17:
            sprite_man.frame_name = "upwalk9"
        counter_1 = counter_1 + 1
        sprite_man.default_frame = "upwalk3"
        sprite_man.y = sprite_man.y -speed

        #upward punch
    if pressed[pygame.K_SPACE] and direction_2 == 'north':
        sprite_man.frame_name = "uppunch"
   # else:
        #sprite_man.frame_name = "upwalk1"
    #left punch
    if pressed[pygame.K_SPACE] and direction_2 == 'west':
        sprite_man.frame_name = "lpunch"
#    else:
        #sprite_man.frame_name = "lwalk1"
    #right punch
    if pressed[pygame.K_SPACE] and direction_2 == 'east':
        sprite_man.frame_name = "rpunch"
    #else:
     #   sprite_man.frame_name = "rwalk1"
    #down punch
    if pressed[pygame.K_SPACE] and direction_2 == 'south':
        sprite_man.frame_name = "dpunch"
   # else:
    if not sprite_man.rect.colliderect(sprite_orc) and pygame.pressed(a):
        sprite_man.motion == done


        #sprite_man.setSequence(upwalk_sequence, upwalk_motion)
    if counter_1 >= 17:
        counter_1 = 1
    if counter_2 >= 17:
        counter_2 = 1
    screen.fill((0,0,0)) #fill screen with white
    if sprite_orc.y > sprite_man.y:
        sprite_man.draw()
        sprite_orc.draw()
    else:
        sprite_orc.draw()
        sprite_man.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()