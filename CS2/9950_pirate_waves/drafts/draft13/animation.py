
class AnimatedSprite:
    def __init__(self, x, y, dx, dy, frames, dwell_per_frame):
        #Sanity check
        if len(frames) != len(dwell_per_frame):
            print('ERROR: length mismatch in AnimatedSprite')
            print(len(frames))
            print(len(dwell_per_frame))
            exit()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.index = 0
        self.frames = frames
        self.rect = self.frames[self.index].get_rect()
        self.dwell_count = 0
        self.dwell_per_frame = dwell_per_frame
        #Skip forward to the first image to use
        while self.index<len(self.dwell_per_frame) and self.dwell_per_frame[self.index]==0:
            self.index += 1

    def isDone(self):
        return self.index>=len(self.frames)

    def update(self):
        if not self.isDone():
            self.dwell_count += 1
            if self.dwell_count > self.dwell_per_frame[self.index]:
                self.index += 1
                #Skip forward to the first image to use
                while self.index<len(self.dwell_per_frame) and self.dwell_per_frame[self.index]==0:
                    self.index += 1
                self.dwell_count = 0
            self.x+=self.dx
            self.y+=self.dy

    def draw(self, surface):
        if not self.isDone():
            surface.blit(self.frames[self.index],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))
