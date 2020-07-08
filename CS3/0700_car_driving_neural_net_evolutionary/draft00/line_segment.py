import pygame

def isBetween(x,left,right):
    '''Returns True if is greater than or equal to left
    and less than or equal to right.'''
    if left > right:
        temp = left
        left = right
        right = temp
    return left<=x and x<=right

class LineSeg:
    def __init__(self, screen, color, x1, y1, x2, y2):
        self.screen = screen
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getSlope(self):
        if self.x2-self.x1 == 0:
            return None
        return (self.y2-self.y1)/(self.x2-self.x1)

    def getYIntercept(self):
        m = self.getSlope()
        if m == None:
            if self.x1 == 0:
                return 0
            else:
                return None
        return self.y1 - self.x1*m

    def getIntersection(self,other):
        '''Returns x,y pair of intersection point.'''
        pass #TODO

    def intersect(self, other):
        m1 = self.getSlope()
        m2 = other.getSlope()
        b1 = self.getYIntercept()
        b2 = other.getYIntercept()
        #vertical lines
        if m1==None and m2==None:
            #Two vertical lines intersect only if they are identical
            return self.x1==other.x1
        elif m1==None:
            #get the y value of the intersection
            y = self.x1*m2+b2
            return isBetween(self.x1,other.x1,other.x2) and isBetween(y,self.y1,self.y2)
        elif m2==None:
            #get the y value of the intersection
            y = other.x1*m1+b1
            return isBetween(other.x1,self.x1,self.x2) and isBetween(y,other.y1,other.y2)
        #parallel lines
        elif m1==m2:
            #Parallel lines intersect only if they are identical
            return b1==b2
        else:
            #Calculate x coordinate of intersection
            x = (b2-b1)/(m1-m2)
            #If this x is between both line segments' x values, then
            #they intersect.
            return isBetween(x,self.x1,self.x2) and isBetween(x,other.x1,other.x2)

    def draw(self):
        pygame.draw.line(self.screen,
            self.color,
            (self.x1,self.y1),
            (self.x2,self.y2),
            3) #thickness




if __name__ == "__main__":
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    #Width and height of the screen are both 500
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    #Make two lines
    line1 = LineSeg(screen, BLUE, 50, 150, 200, 200)
    line2 = LineSeg(screen, GREEN, 50, 50, 200, 200)


    running = True
    while running:
        #Respond to events such as closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            line1.x1+=1
            line1.x2+=1
        if pressed[pygame.K_DOWN]:
            line1.y1+=1
            line1.y2+=1
        if pressed[pygame.K_LEFT]:
            line1.x1-=1
            line1.x2-=1
        if pressed[pygame.K_UP]:
            line1.y1-=1
            line1.y2-=1

        if line1.intersect(line2):
            line1.color = BLUE
        else:
            line1.color = RED

        #Update screen display
        screen.fill(BLACK)
        line1.draw()
        line2.draw()
        pygame.display.flip()
        #Delay to get 60 fps
        clock.tick(60)
    pygame.quit()