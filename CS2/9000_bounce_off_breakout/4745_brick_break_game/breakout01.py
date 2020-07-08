import pygame, random, math

class WallRound:
    def __init__(self, surface, color, x, y, dx, dy, radius):
        self.surface = surface
        self.dx = dx
        self.dy = dy
        self.color = color
        self.radius = radius
        self.rect = pygame.Rect(x,y,radius*2,radius*2)

    def angleTo(self, other):
        x = other.rect.centerx - self.rect.centerx
        y = other.rect.centery - self.rect.centery
        return math.atan2(y,x)

    def angleToCoord(self, x, y):
        x = x - self.rect.centerx
        y = y - self.rect.centery
        return math.atan2(y,x)

    def putOut(self, other):
        angle = self.angleTo(other)
        depth = self.radius+other.radius - self.distanceTo(other)
        other.rect.centerx += math.cos(angle)*depth
        other.rect.centery += math.sin(angle)*depth

    def distanceTo(self, other):
        return math.sqrt((self.rect.centerx-other.rect.centerx)**2 + (self.rect.centery-other.rect.centery)**2)

    def collidedWith(self, other):
        distance = self.distanceTo(other)
        radius_sum = other.radius + self.radius
        return distance < radius_sum

    '''Bounce off the other sprite off of this using vectors
    http://stackoverflow.com/questions/573084/how-to-calculate-bounce-angle
    '''
    def bounceOff(self, other):
        normal_vector = [self.rect.centerx - other.rect.centerx,
                        self.rect.centery - other.rect.centery]
        #Separate other's velocity into the part perpendicular
        #to other, u, and the part parallel to other, w.
        v_dot_n = self.dx*normal_vector[0] + self.dy*normal_vector[1];
        square_of_norm_length = normal_vector[0]**2 + normal_vector[1]**2
        multiplier = v_dot_n / square_of_norm_length
        u_vector = [normal_vector[0]*multiplier,
                    normal_vector[1]*multiplier]
        w_vector = [self.dx - u_vector[0],
                    self.dy - u_vector[1]]
        #Determine the velocity post collision while
        #factoring in the elasticity and friction of
        #the wall.
        bounce_friction = 0
        elasticity = 1
        self.dx = w_vector[0]*(1-bounce_friction)-u_vector[0]*elasticity
        self.dy = w_vector[1]*(1-bounce_friction)-u_vector[1]*elasticity

    def move(self):
        self.can_jump = False #Default is that ball can't jump
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left<0:
            self.rect.left=0
            self.dx = -self.dx
        elif self.rect.right > self.surface.get_width():
            self.rect.right = self.surface.get_width()
            self.dx = -self.dx
        if self.rect.top<0:
            self.rect.top=0
            self.dy = -self.dy

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.rect)


class WallRectangular:
    def __init__(self, surface, color, rect, hp):
        self.surface = surface
        self.rect = rect
        self.color = color
        self.hp = hp
        self.corners = [
            WallRound(surface, color, rect.left, rect.top, 0,0,1),
            WallRound(surface, color, rect.right, rect.top, 0,0,1),
            WallRound(surface, color, rect.right, rect.bottom, 0,0,1),
            WallRound(surface, color, rect.left, rect.bottom, 0,0,1)
            ]

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def putOut(self, other):
        '''Pre: the rectangles of self and other overlap.
        Post: other is pushed out so no further collision occurs.
        other is also bounced off of self in accordance with
        platformer physics rules.'''
        #Top of other collided
        if self.rect.collidepoint((other.rect.centerx,other.rect.top)):
            other.rect.top = self.rect.bottom+1
            other.dy = -other.dy
            #print("top")
        #Bottom of other collided
        elif self.rect.collidepoint((other.rect.centerx,other.rect.bottom)):
            other.rect.bottom = self.rect.top
            other.dy = -other.dy
            #print("bottom")
        #Left side of other collided
        elif self.rect.collidepoint((other.rect.x,other.rect.centery)):
            other.rect.x = self.rect.right
            other.dx = -other.dx
            #print("left")
        #Right side of other collided
        elif self.rect.collidepoint((other.rect.right,other.rect.centery)):
            other.rect.right = self.rect.x
            other.dx = -other.dx
            #print("right")
        #Upper left corner of other collided
        elif self.rect.collidepoint((other.rect.left,other.rect.top)):
            #print("top_left")
            other.bounceOff(self.corners[2])
            self.corners[2].putOut(other)
        #Upper right corner of other collided
        elif self.rect.collidepoint((other.rect.right,other.rect.top)):
            #print("top_right")
            other.bounceOff(self.corners[3])
            self.corners[3].putOut(other)
        #Lower right corner of other collided
        elif self.rect.collidepoint((other.rect.right,other.rect.bottom)):
            #print("lower_right")
            other.bounceOff(self.corners[0])
            self.corners[0].putOut(other)
        #Lower left corner of other collided
        elif self.rect.collidepoint((other.rect.left,other.rect.bottom)):
            #print("lower_left")
            other.bounceOff(self.corners[1])
            self.corners[1].putOut(other)

    def setLocation(self):
        pos = pygame.mouse.get_pos()
        self.rect.centerx = pos[0]



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
ball = WallRound(screen, WHITE,
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
            if p.rect.colliderect(b.rect):
                p.putOut(b)
                #Decrease the wall's hp by one
                p.hp = p.hp-1
            #Check collision with paddle
            if paddle.rect.colliderect(b.rect):
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
        if balls[i].rect.y > height:
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
            ball = WallRound(screen, WHITE,
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