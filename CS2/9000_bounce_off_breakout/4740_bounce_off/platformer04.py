import pygame, random, math


'''
Make the corners circular collision points.

READY FOR TESTING

Then consider testing with larger circles and larger squares.
Slow it down too to see the collision better.

Then further consider making the older bounce off code use
this method if this method works better.
'''



class WallRectangular:
    def __init__(self, surface, color, rect):
        self.surface = surface
        self.rect = rect
        self.color = color
        self.corners = [
            WallRound(surface, color, rect.left, rect.top, 1),
            WallRound(surface, color, rect.right, rect.top, 1),
            WallRound(surface, color, rect.right, rect.bottom, 1),
            WallRound(surface, color, rect.left, rect.bottom, 1)
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
            other.dy = 0
            print("top")
        #Bottom of other collided
        elif self.rect.collidepoint((other.rect.centerx,other.rect.bottom)):
            other.rect.bottom = self.rect.top
            other.dy = 0
            other.can_jump = True
            print("bottom")
        #Left side of other collided
        elif self.rect.collidepoint((other.rect.x,other.rect.centery)):
            other.rect.x = self.rect.right
            other.dx = -other.dx
            print("left")
        #Right side of other collided
        elif self.rect.collidepoint((other.rect.right,other.rect.centery)):
            other.rect.right = self.rect.x
            other.dx = -other.dx
            print("right")
        #Upper left corner of other collided
        elif self.rect.collidepoint((other.rect.left,other.rect.top)):
            print("top_left")
            other.bounceOff(self.corners[2])
            self.corners[2].putOut(other)
        #Upper right corner of other collided
        elif self.rect.collidepoint((other.rect.right,other.rect.top)):
            print("top_right")
            other.bounceOff(self.corners[3])
            self.corners[3].putOut(other)
        #Lower right corner of other collided
        elif self.rect.collidepoint((other.rect.right,other.rect.bottom)):
            print("lower_right")
            other.bounceOff(self.corners[0])
            self.corners[0].putOut(other)
        #Lower left corner of other collided
        elif self.rect.collidepoint((other.rect.left,other.rect.bottom)):
            print("lower_left")
            other.bounceOff(self.corners[1])
            self.corners[1].putOut(other)


class WallRound:
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.dx = 0
        self.dy = 0
        self.color = color
        self.radius = radius
        self.can_jump = False
        self.rect = pygame.Rect(x,y,radius*2,radius*2)

    def angleTo(self, other):
        x = other.rect.centerx - self.rect.centerx
        y = other.rect.centery - self.rect.centery
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
        elif self.rect.bottom > self.surface.get_height():
            self.rect.bottom = self.surface.get_height()
            self.dy = -self.dy
            #Ball can jump after hitting the floor
            self.can_jump = True

    def draw(self):
        pygame.draw.ellipse(self.surface, self.color, self.rect)




BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,100,0)

#Width and height of the screen are both 500
width = 900
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


ball = WallRound(screen,
            WHITE,
            250, #x
            250, #y
            50) #radius


round_wall = WallRound(screen,
            ORANGE,
            250, #x
            250, #y
            40) #radius



#Create rectangular walls
platform_list = []
r = pygame.Rect(250,100, 300, 300)
platform_list.append(WallRectangular(screen, ORANGE, r))

running = True
while running:
    #Fill the screen with black
    screen.fill(BLACK)
    ball_can_jump = False
    ball.move()
    #Check for collision with platform
    for p in platform_list:
        if p.rect.colliderect(ball.rect):
            p.putOut(ball)
    if ball.collidedWith(round_wall):
        ball.bounceOff(round_wall)
        round_wall.putOut(ball)
    #Draw the balls and walls
    round_wall.draw()
    ball.draw()
    for p in platform_list:
        p.draw()
    #Respond to events such as closing the game or moving the hippo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball.can_jump:
        ball.dy -= 30
    #if keys[pygame.K_DOWN]:
    #    ball.dy += 0.1
    if keys[pygame.K_LEFT]:
        ball.dx -= 0.5
    if keys[pygame.K_RIGHT]:
        ball.dx += 0.5
    #Ball is pulled by gravity
    ball.dy += 1
    #Friction affects ball
    ball.dx *= 0.9
    ball.dy *= 0.9
    #Update screen display
    pygame.display.flip()
    #Delay to get 10 fps
    clock.tick(10)
pygame.quit()