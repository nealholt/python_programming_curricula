import pygame, random, math

class WallRectangular:
    def __init__(self, surface, color, rect):
        self.surface = surface
        self.rect = rect
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def collidedAboveBelow(self, other):
        '''Pre: self and other collided.
        Post: Returns true if the collision was bove and below.
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



class WallRound:
    def __init__(self, surface, color, x, y, radius):
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.color = color
        self.radius = radius

    def angleTo(self, other):
        r = self.getRect()
        other_r = other.getRect()
        x = other_r.centerx - r.centerx
        y = other_r.centery - r.centery
        return math.atan2(y,x)

    def putOut(self, other):
        angle = self.angleTo(other)
        depth = self.radius+other.radius - self.distanceTo(other)
        other.x += math.cos(angle)*depth
        other.y += math.sin(angle)*depth

    def distanceTo(self, other):
        r = self.getRect()
        other_r = other.getRect()
        return math.sqrt((r.centerx-other_r.centerx)**2 + (r.centery-other_r.centery)**2)

    def collidedWith(self, other):
        distance = self.distanceTo(other)
        radius_sum = other.radius + self.radius
        return distance < radius_sum

    '''Bounce off the other sprite off of this using vectors
    http://stackoverflow.com/questions/573084/how-to-calculate-bounce-angle
    '''
    def bounceOff(self, other):
        self_rect = self.getRect()
        other_rect = other.getRect()
        normal_vector = [self_rect.centerx - other_rect.centerx,
                        self_rect.centery - other_rect.centery]
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
        new_dx = w_vector[0]*(1-bounce_friction)-u_vector[0]*elasticity
        new_dy = w_vector[1]*(1-bounce_friction)-u_vector[1]*elasticity
        return new_dx,new_dy

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
        elif self.y+self.radius*2 > self.surface.get_height():
            self.y=self.surface.get_height()-self.radius*2
            self.dy = -self.dy
        self.dx = self.dx/friction
        self.dy = self.dy/friction

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

width = 900
height = 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

friction = 1.005


#Create balls
ball = WallRound(screen,
            WHITE,
            250, #x
            250, #y
            15) #radius
ball_list = [ball]
for i in range(16):
    ball = WallRound(screen,
            WHITE,
            random.randint(20,width-20), #x
            random.randint(20,height-20), #y
            15) #radius
    ball_list.append(ball)

running = True
while running:
    #Fill the screen with black
    screen.fill(BLACK)
    #Move all balls
    for b in ball_list:
        b.move()
    #Check for collision with balls
    for i in range(len(ball_list)-1):
        for j in range(i+1,len(ball_list)):
            if ball_list[i].collidedWith(ball_list[j]):
                i_dx, i_dy = ball_list[i].bounceOff(ball_list[j])
                j_dx, j_dy = ball_list[j].bounceOff(ball_list[i])
                ball_list[i].dx = i_dx
                ball_list[i].dy = i_dy
                ball_list[j].dx = j_dx
                ball_list[j].dy = j_dy
                #ball_list[i].putOut(ball_list[j])
    #Draw the balls
    for b in ball_list:
        b.draw()
    #Respond to events such as closing the game or moving the hippo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == 32: #Space bar
                const = 8
                for b in ball_list:
                    b.dx = (random.random()-0.5)*const
                    b.dy = (random.random()-0.5)*const
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball.dy -= 0.1
    if keys[pygame.K_DOWN]:
        ball.dy += 0.1
    if keys[pygame.K_LEFT]:
        ball.dx -= 0.1
    if keys[pygame.K_RIGHT]:
        ball.dx += 0.1
    #Update screen display
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()