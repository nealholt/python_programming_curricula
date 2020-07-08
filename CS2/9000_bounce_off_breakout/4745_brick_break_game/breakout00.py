import pygame, random, math

class WallRectangular:
    def __init__(self, surface, color, rect, hp):
        self.surface = surface
        self.rect = rect
        self.color = color
        self.hp = hp

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def collidedAboveBelow(self, other):
        '''Pre: self and other collided.
        Post: Returns true if the collision was above and below.
        Returns false if the collision was along the side.'''
        r = other.getRect()
        normalized_x_diff = abs(r.centerx-self.rect.centerx)/self.rect.width
        normalized_y_diff = abs(r.centery-self.rect.centery)/self.rect.height
        return normalized_x_diff < normalized_y_diff

    def putOut(self, other):
        r = other.getRect()
        if self.collidedAboveBelow(other):
            if r.centery<self.rect.centery:
                other.y = self.rect.y-r.height
            elif r.centery>self.rect.centery:
                #Plus 1 so no more collisions occur
                other.y = self.rect.y+self.rect.height+1
        else:
            if r.centerx<self.rect.centerx:
                other.x = self.rect.x-r.width
            elif r.centerx>self.rect.centerx:
                #Plus 1 so no more collisions occur
                other.x = self.rect.x+self.rect.width+1

    def bounceOff(self, other):
        '''This is different from the WallRound's bounceOff function,
        which bounces the self off the other. This function bounces the
        other off of the self.'''
        r = other.getRect()
        if self.collidedAboveBelow(other):
            other.dy = -other.dy
        else:
            other.dx = -other.dx

    def setLocation(self):
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]



class Ball:
    def __init__(self, surface, color, x, y, dx, dy, radius):
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.radius = radius

    def angleToCoord(self, x, y):
        r = self.getRect()
        x = x - r.centerx
        y = y - r.centery
        return math.atan2(y,x)

    def angleTo(self, other):
        r = self.getRect()
        other_r = other.getRect()
        x = other_r.centerx - r.centerx
        y = other_r.centery - r.centery
        return math.atan2(y,x)

    def distanceTo(self, other):
        r = self.getRect()
        other_r = other.getRect()
        return math.sqrt((r.centerx-other_r.centerx)**2 + (r.centery-other_r.centery)**2)

    def collidedWith(self, other):
        distance = self.distanceTo(other)
        radius_sum = other.radius + self.radius
        return distance < radius_sum

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x<0:
            self.x=0
            self.dx = -self.dx
        elif self.x+self.radius*2 > self.surface.get_width():
            self.x=self.surface.get_width()-self.radius*2
            self.dx = -self.dx
        if self.y<0:
            self.y=0
            self.dy = -self.dy

    def getRect(self):
        return pygame.Rect(self.x,
                            self.y,
                            self.radius*2, #width
                            self.radius*2) #height

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.getRect())




BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,100,0)
BLUE = (0,0,255)

#Width and height of the screen are both 500
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

balls = []

#Add a ball indicating where balls start from
ball = Ball(screen, WHITE,
    width/2, #x
    height-10, #y
    0, #dx
    0, #dy
    15) #radius
balls.append(ball)

#Create rectangular walls
platform_list = []
for x in range(10):
    for y in range(5):
        r = pygame.Rect(x*90,y*30, 80, 20)
        platform_list.append(WallRectangular(screen, ORANGE, r, 1)) #1 is hitpoints

r = pygame.Rect(200,570, 80, 20)
paddle = WallRectangular(screen, BLUE, r, 999999)

running = True
while running:
    #Fill the screen with black
    screen.fill(BLACK)
    #Check for collision with platform
    for p in platform_list:
        for b in balls:
            if p.rect.colliderect(b.getRect()):
                p.bounceOff(b)
                p.putOut(b)
                #Decrease the wall's hp by one
                p.hp = p.hp-1
            #Check collision with paddle
            if paddle.rect.colliderect(b.getRect()):
                paddle.bounceOff(b)
                paddle.putOut(b)
    #Draw the balls and walls
    for b in balls:
        b.move()
        b.draw()
    for p in platform_list:
        p.draw()
    paddle.draw()
    #Remove balls that touched bottom of the screen
    for i in reversed(range(len(balls))):
        if balls[i].y > height:
            del balls[i]
    #Remove dead walls
    for i in reversed(range(len(platform_list))):
        if platform_list[i].hp <= 0:
            del platform_list[i]
    #Respond to events such as closing the game or moving the hippo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            #Add a ball headed toward the mouse click
            ball = Ball(screen, WHITE,
                width/2, #x
                height-10, #y
                0, #dx
                0, #dy
                15) #radius
            angle = ball.angleToCoord(pos[0], pos[1])
            speed = 10
            ball.dx = math.cos(angle)*speed
            ball.dy = math.sin(angle)*speed
            balls.append(ball)
    paddle.setLocation()
    #Update screen display
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()