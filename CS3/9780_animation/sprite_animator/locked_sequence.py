import pygame

pygame.init()

#Dwell on each image for this many frames.
dwell_reset = 5

#The following are image sequences and corresponding x,y movements:
walk_sequence = ['walk1','walk2','walk3','walk4','walk5','walk6','walk7','walk8']
walk_motion = [(5,0), (5,0), (5,0), (5,0), (5,0), (5,0), (5,0), (5,0)]

ascend_sequence = ['ascend1','ascend2','ascend3','ascend4','ascend5', 'hurdle1']
ascend_motion = [(0,0), (0,-30), (0,-10), (0,-10), (0,-10), (20,-20)]

crawl_sequence = ['crawl1','crawl2','crawl3']
crawl_motion = [(5,0), (5,0), (5,0)]

roll_sequence = ['roll1','roll2','roll3','roll4','roll5']
roll_motion = [(20,0), (20,0), (20,0), (20,0), (20,0)]

hurdle_sequence = ['hurdle1','hurdle2','hurdle3','stand']
hurdle_motion = [(25,0),(25,0),(25,0),(25,0)]

fall_sequence = ['leap','fall','fall','fall','fall','fall','crouch']
fall_motion = [(50,-10),(0,40),(0,40),(0,40),(0,40),(0,40),(0,30)]


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
        #Dwell is a countdown that lets sprite dwell on each frame of an image
        #for longer to make the transition look smoother.
        self.dwell = dwell_reset

    def update(self):
        #STEP 1: Decrease self.dwell by 1
        self.dwell = self.dwell - 1
        #STEP 2: Make a copy of self.frame_name in a new variable
        #so later on we can detect if the image changed.
        old_frame_name = self.frame_name
        #STEP 3: If self.sequence is not empty and self.dwell has
        #counted down to zero, then delete the first value from
        #self.sequence and from self.motion.
        #Then inside that same if statement check if self.sequence
        #is still not empty and if so, reset self.dwell to dwell_reset
        #and set self.frame_name to the first value in self.sequence.

        #Advance sequences and re-center image
        if len(self.sequence) > 0 and self.dwell<=0:
            del self.sequence[0]
            del self.motion[0]
            if len(self.sequence)>0:
                self.dwell = dwell_reset
                self.frame_name = self.sequence[0]
        #STEP 4: If self.dwell has counted down to zero then reset
        #self.frame_name to self.default_frame
        elif self.dwell<=0:
            #Return to default position
            self.frame_name = self.default_frame
        #STEP 5: If self.motion is not empty then increase self.x by
        #self.motion[0][0]/dwell_reset and increase self.y by
        #self.motion[0][1]/dwell_reset

        #Move
        if len(self.motion) > 0:
            self.x = self.x + self.motion[0][0]/dwell_reset
            self.y = self.y + self.motion[0][1]/dwell_reset
        #STEP 6: Check if the image changed by comparing self.frame_name
        #with the copy of it you made at the start of this function.
        #If the values are different, set self.rect equal to the
        #new image's rectangle, which is
        #self.frames[self.frame_name].get_rect()

        #If the image changed, update the rectangle
        if old_frame_name != self.frame_name:
            self.rect = self.frames[self.frame_name].get_rect()

    def setSequence(self, sequence, motion):
        #STEP 1: Check if self.sequence is empty. We only want to start
        #a new sequence if we finished the old one already.
        if len(self.sequence)==0:
            #STEP 2: If self.sequence is empty, copy all the values of
            #sequence into self.sequence. You will need a loop to go through
            #sequence and you will need to use self.sequence.append to put
            #the values in self.sequence.
            for s in sequence:
                self.sequence.append(s)
            #STEP 2: If self.sequence is empty (meaning inside the if statement),
            #copy all the values of motion into self.motion.
            for m in motion:
                self.motion.append(m)
            #STEP 3: If self.sequence is empty, set self.frame_name equal to the
            #first value in the sequence.
            self.frame_name = self.sequence[0]
            #STEP 4: Set self.dwell equal to dwell_reset
            self.dwell = dwell_reset

    def setDefaultFrame(self, default):
        sprite.default_frame = default
        if len(self.sequence)==0:
            sprite.frame_name = 'stand'

    def draw(self):
        screen.blit(self.frames[self.frame_name],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))
        self.update()


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

'''
#Reminder: this is how you resize the image if you want.
scaling = 2
dimensions = (dimensions[0]*scaling,dimensions[1]*scaling)
for i in range(len(frames)):
    frames[i] = pygame.transform.scale(
                            frames[i],
                            dimensions)
'''

#Draw all images on the screen
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:
                if sprite.default_frame == 'stand': #walk when upright
                    sprite.setSequence(walk_sequence, walk_motion)
                else: #otherwise crawl
                    sprite.setSequence(crawl_sequence, crawl_motion)
            elif event.key == pygame.K_LEFT:
                sprite.x = 100 #Reset
            elif event.key == pygame.K_UP:
                if sprite.default_frame == 'crouch': #Stand up
                    sprite.setDefaultFrame('stand')
                else: #jump
                    sprite.setSequence(ascend_sequence, ascend_motion)
            elif event.key == pygame.K_DOWN:
                sprite.setDefaultFrame('crouch')
            elif event.key == 104: #h key
                sprite.default_frame = 'stand'
                sprite.setSequence(hurdle_sequence, hurdle_motion)
            elif event.key == 114: #r key
                sprite.default_frame = 'stand'
                sprite.setSequence(roll_sequence, roll_motion)
            elif event.key == 115: #s key
                sprite.default_frame = 'crouch'
                sprite.setSequence(fall_sequence, fall_motion)

    screen.fill((0,0,0)) #fill screen with black
    sprite.draw()
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()