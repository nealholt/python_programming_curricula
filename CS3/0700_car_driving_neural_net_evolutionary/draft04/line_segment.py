import pygame, math

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

    def intersect(self, other):
        '''Returns True if the lines intersect.'''
        return self.getIntersection(other)!=None

    def getIntersection(self,other):
        '''Returns x,y pair of intersection point.
        Return the closest intersection point to x1,y1.'''
        m1 = self.getSlope()
        m2 = other.getSlope()
        b1 = self.getYIntercept()
        b2 = other.getYIntercept()
        print('m1 '+str(m1)) #TODO TESTING
        print('b1 '+str(b1))
        print('m2 '+str(m2))
        print('b2 '+str(b2))
        #vertical lines
        if m1==None and m2==None:
            #Two vertical lines intersect only if they are identical
            if self.x1==other.x1 and (isBetween(other.y1,self.y1,self.y2) or isBetween(other.y2,self.y1,self.y2)):
                if isBetween(self.y1,other.y1,other.y2):
                    return (self.x1,self.y1)
                else:
                    return (self.x1,min(other.y1,other.y2))
        elif m1==None:
            #get the y value of the intersection
            y = self.x1*m2+b2
            #print('values',y,self.x1,m2,b2) #TODO TESTING
            #print(self.y1,self.y2) #TODO TESTING
            if isBetween(self.x1,other.x1,other.x2) and isBetween(y,self.y1,self.y2):
                #print('is between') #TODO TESTING
                return (self.x1,y)
            else:
                pass #print('not between') #TODO TESTING
        elif m2==None:
            #get the y value of the intersection
            y = other.x1*m1+b1
            if isBetween(other.x1,self.x1,self.x2) and isBetween(y,other.y1,other.y2):
                return (other.x1,y)
        #parallel lines
        elif m1==m2:
            #Parallel lines intersect only if they are identical
            if b1==b2 and (isBetween(other.x1,self.x1,self.x2) or isBetween(other.x2,self.x1,self.x2)):
                if isBetween(self.x1,other.x1,other.x2):
                    return (self.x1,self.y1)
                else:
                    return (min(other.x1,other.x2),other.y1)
        else:
            #Calculate x coordinate of intersection
            x = (b2-b1)/(m1-m2)
            #If this x is between both line segments' x values, then
            #they intersect.
            if isBetween(x,self.x1,self.x2) and isBetween(x,other.x1,other.x2):
                #Near vertical lines create incredibly large slopes
                #that cause problems in these calculations.
                #Check for very large values and avoid using them.
                if abs(m1)>2**31:
                    y=x*m2+b2
                else:
                    y=x*m1+b1
                if isBetween(y,self.y1,self.y2) and isBetween(y,other.y1,other.y2):
                    return (x,y)#print(self.x1,self.x2,self.y1,self.y2, x*m2+b2)
        return None

    def getLength(self):
        return math.sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2)

    def draw(self):
        pygame.draw.line(self.screen,
            self.color,
            (self.x1,self.y1),
            (self.x2,self.y2),
            1) #thickness


def xMarksSpot(screen,point,color):
    pygame.draw.line(screen, color,
        (point[0]-10,point[1]-10),
        (point[0]+10,point[1]+10),
        1) #thickness
    pygame.draw.line(screen, color,
        (point[0]-10,point[1]+10),
        (point[0]+10,point[1]-10),
        1) #thickness


if __name__ == "__main__":
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (255,255,0)
    #Width and height of the screen are both 500
    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    #Make two lines
    line1 = LineSeg(screen, BLUE, 50, 50, 50, 200)#LineSeg(screen, BLUE, 50, 150, 200, 200)
    line2 = LineSeg(screen, GREEN, 50, 50, 200, 200)
    line3 = LineSeg(screen, GREEN, 300, 50, 300, 200)
    line4 = LineSeg(screen, GREEN, 350, 150, 500, 200)
    line5 = LineSeg(screen, GREEN, 50, 450, 200, 200)


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

        screen.fill(BLACK)

        line1.color = RED
        point1 = line1.getIntersection(line2)
        point2 = line1.getIntersection(line3)
        point3 = line1.getIntersection(line4)
        point4 = line1.getIntersection(line5)
        if point1!=None:
            line1.color = BLUE
            xMarksSpot(screen,point1,YELLOW)
        if point2!=None:
            line1.color = BLUE
            xMarksSpot(screen,point2,YELLOW)
        if point3!=None:
            line1.color = BLUE
            xMarksSpot(screen,point3,YELLOW)
        if point4!=None:
            line1.color = BLUE
            xMarksSpot(screen,point4,YELLOW)

        #Update screen display
        line1.draw()
        line2.draw()
        line3.draw()
        line4.draw()
        line5.draw()
        pygame.display.flip()
        #Delay to get 60 fps
        clock.tick(60)
    pygame.quit()