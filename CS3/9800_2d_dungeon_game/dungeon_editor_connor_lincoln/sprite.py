
class Sprite:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, (int(self.x),int(self.y)))

    def drawCentered(self):
        self.screen.blit(self.image,
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))




class AnimatedSprite(Sprite):
    def __init__(self, screen, x, y, frames, image_dwell):
        super().__init__(screen, x, y, frames[0])
        #index of the current animation frame
        self.index = 0
        #Countdown before transitioning to next frame
        self.dwell = image_dwell
        #How long to dwell on each frame
        self.dwell_reset = image_dwell
        #List of all frames
        self.frames = frames

    def advanceImage(self):
        '''Advance to the next frame'''
        self.dwell -= 1
        if self.dwell < 0:
            self.index = (self.index+1)%len(self.frames)
            self.dwell = self.dwell_reset
            self.image = self.frames[self.index]

    def update(self):
        self.advanceImage()
