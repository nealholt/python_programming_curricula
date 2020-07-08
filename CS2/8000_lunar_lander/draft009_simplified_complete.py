import pygame, math

'''
I cut a helluva lot out compared to the last draft including
screen wrapping and a random landscape. This version is much simpler.
'''

#Setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
large_font = pygame.font.SysFont('Arial', 48)
small_font = pygame.font.SysFont('Arial', 24)
black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0

gravity = 0.05

landing_pad_index = 8

class GameManager:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        #Create player
        self.player = Ship(screen, 400, 0)
        #Create the ground
        self.ground = Ground(screen)
        #List of intangible animation objects
        self.animation_list = []
        self.victory = False

    def update(self):
        #Move and draw
        self.ground.draw(self.player.x, self.player.y)
        for item in self.animation_list:
            item.move()
            item.draw(self.player.x, self.player.y)
        #Draw the player if the player is still alive
        if self.player.lives > 0:
            self.player.move()
            self.player.draw()
            #Check for a collision with the ground or a landing
            if self.ground.safeLanding(self.player):
                self.victory = True
            elif self.ground.shipHitGround(self.player):
                self.player.lives = 0


class Ground:
    def __init__(self, surface):
        self.surface = surface
        self.ground_heights = [[0,0],[200,700],[400,200],[600,550],
                              [800,0],[1000,300],[1200,800],[1400,400],
                              [1600,600],[1650,600],#Landing pad start and end
                              [1800,500],[2000,500],[2200,100]]

    def overLandingPad(self,x):
        return x>self.ground_heights[landing_pad_index][0] and x<self.ground_heights[landing_pad_index+1][0]

    def shipHitGround(self, ship):
        points = ship.getCorners(ship.x, ship.y)
        for p in points:
            if p[1] >= self.getHeightAt(p[0]):
                return True
        return False

    def safeLanding(self, player_ship):
        print('Over pad: '+str(self.overLandingPad(player_ship.x)))
        print('Collided: '+str(self.shipHitGround(player_ship)))
        print('Good dx: '+str(abs(player_ship.dx)<1))
        print('Good dy: '+str(player_ship.dy>0 and player_ship.dy<1.5))
        print('Good angle: '+str(abs((player_ship.angle%math.pi)-math.pi/2)<math.pi/32))
        print('angle: '+str(player_ship.angle))
        print('angle difference to pi/2: '+str(abs((player_ship.angle%math.pi)-math.pi/2)))
        print('dx: '+str(player_ship.dx))
        print('dy: '+str(player_ship.dy))
        if self.overLandingPad(player_ship.x) and self.shipHitGround(player_ship):
            #Check that the player is facing upright, and
            #has minimal dx and sufficiently small dy for a safe landing.
            if abs(player_ship.dx)<1 and player_ship.dy>0 and player_ship.dy<1.5:
                return abs((player_ship.angle%math.pi)-math.pi/2)<math.pi/32
        else:
            return False

    def getHeightAt(self, x):
        #Get coordinates that x is between and use those coordinates
        #as a line to calculate the height of the ground at that x value.
        if x<=self.ground_heights[0][0] or x>=self.ground_heights[-1][0]:
            return 0
        for i in range(len(self.ground_heights)-1):
            if x>=self.ground_heights[i][0] and x<self.ground_heights[i+1][0]:
                start = self.ground_heights[i]
                end = self.ground_heights[i+1]
                slope = (end[1]-start[1]) / (end[0]-start[0])
                #Point slope form:
                return slope*(x-end[0])+end[1]

    def draw(self, povx, povy):
        x_adjust = self.surface.get_width()/2 - povx
        y_adjust = self.surface.get_height()/2 - povy
        #Draw the line segments
        for i in range(len(self.ground_heights)-1):
            coord1 = [self.ground_heights[i][0]+x_adjust, self.ground_heights[i][1]+y_adjust]
            coord2 = [self.ground_heights[i+1][0]+x_adjust, self.ground_heights[i+1][1]+y_adjust]
            color = white
            thickness = 3
            if i == landing_pad_index:
                color = green
                thickness = 5
            pygame.draw.line(self.surface, color, coord1, coord2, thickness)


class Ship:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 0.3
        self.sides = 3
        self.radius = 20
        self.angle = 0
        self.rotation_rate = math.pi/16
        self.thrust_on = False
        self.lives = 1
        self.remove = False

    def rotateLeft(self):
        self.angle -= self.rotation_rate

    def rotateRight(self):
        self.angle += self.rotation_rate

    def thrust(self):
        self.dx += math.cos(self.angle)*self.speed
        self.dy += math.sin(self.angle)*self.speed
        self.thrust_on = True

    def move(self):
        #Move dx and dy
        self.x += self.dx
        self.y += self.dy
        #Apply gravity
        self.dy += gravity

    def getCorners(self, x_to_use, y_to_use):
        '''x_to_use, y_to_use are arguments that are either
        the center of the screen (for drawing the ship)
        or the "actual" x and y coordinates of the ship
        (for checking collisions with the ground).'''
        #Returns list of points to draw the ship
        points = []
        #Nose
        angle = self.angle+math.pi*2
        x = x_to_use + math.cos(angle)*self.radius*1.5
        y = y_to_use + math.sin(angle)*self.radius*1.5
        points.append([x, y])
        #wing 1
        angle = self.angle+math.pi*2*(1.2/self.sides)
        x = x_to_use + math.cos(angle)*self.radius
        y = y_to_use + math.sin(angle)*self.radius
        points.append([x, y])
        #rear
        angle = self.angle+math.pi
        x = x_to_use + math.cos(angle)*self.radius*0.5
        y = y_to_use + math.sin(angle)*self.radius*0.5
        points.append([x, y])
        #wing 2
        angle = self.angle+math.pi*2*(1.8/self.sides)
        x = x_to_use + math.cos(angle)*self.radius
        y = y_to_use + math.sin(angle)*self.radius
        points.append([x, y])
        return points

    def draw(self):
        #Draw thrust
        if self.thrust_on:
            angle = self.angle+math.pi
            x = self.surface.get_width()/2 + math.cos(angle)*self.radius*0.7
            y = self.surface.get_height()/2 + math.sin(angle)*self.radius*0.7
            radius = 10
            r = pygame.Rect(x-radius/2,y-radius/2,radius,radius)
            pygame.draw.ellipse(self.surface, red, r)
        #Reset thrust
        self.thrust_on = False
        #Draw outline of ship. Note: 3 is line thickness.
        points = self.getCorners(self.surface.get_width()/2, self.surface.get_height()/2)
        pygame.draw.polygon(self.surface, white, points,3)



def userInputToPlayer(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.thrust()
    if keys[pygame.K_LEFT]:
        player.rotateLeft()
    if keys[pygame.K_RIGHT]:
        player.rotateRight()



#Create game manager object to manage updating and moving everything
gm = GameManager(screen, 0) #Start on level 0


#Main loop
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            #Press enter to reset game after death
            if event.key == pygame.K_RETURN and (gm.player.lives <= 0 or gm.victory):
                gm = GameManager(screen, 0) #Reset to level 0
    #Send user input to the player if it's alive
    if gm.player.lives > 0:
        userInputToPlayer(gm.player)
    #fill screen with black
    screen.fill(black)
    #Display level
    position = (width-150, 10)
    screen.blit(small_font.render("Level "+str(gm.level),True,white),position)
    #Check for game over
    if gm.victory:
        position = (width/2-100, height/2-20)
        screen.blit(large_font.render("CONGRATULATIONS",True,white),position)
        position = (width/2-75, height/2+40)
        screen.blit(small_font.render("[ENTER] to reset",True,white),position)
    elif gm.player.lives <= 0:
        position = (width/2-100, height/2-20)
        screen.blit(large_font.render("Game Over",True,white),position)
        position = (width/2-75, height/2+40)
        screen.blit(small_font.render("[ENTER] to reset",True,white),position)
    else:
        gm.update()
    #Update the screen
    pygame.display.flip()
    pygame.display.update()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()