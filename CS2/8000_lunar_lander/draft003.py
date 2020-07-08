import pygame, math, random

'''
Next steps:
    Infinitely scrolling ground. Just make it loop around.
    More interesting ups and downs in the ground.
    Adding a landing pad to the ground.
    Collision with the ground.
    Ability to land.
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

ground_segments = 10
segment_spacing = 200
height_variation = 500


class Line:
    def __init__(self, screen, x1, y1, x2, y2, dx, dy):
        self.screen = screen
        #Get the length of the line
        self.length = math.sqrt((x1-x2)**2+(y1-y2)**2)
        #Get the midpoint of the line. We do this so we can draw the line
        #based on an angle, which makes it possible to more easily rotate the line.
        self.x = (x2+x1)/2
        self.y = (y2+y1)/2
        #Get the velocity of the line
        self.dx = dx
        self.dy = dy
        #Get the angle of the line
        self.angle = math.atan2(y2-y1, x2-x1)
        #Randomly rotate +-math.pi/256 per frame
        self.rotation_rate = random.random()*math.pi/128
        self.rotation_rate = self.rotation_rate-math.pi/256

    def move(self):
        self.angle = self.angle + self.rotation_rate
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def draw(self, povx, povy):
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        #Calculate the coordinates of both ends of the line
        coord1 = [x_adjust + self.x+math.cos(self.angle)*self.length/2,
                  y_adjust + self.y+math.sin(self.angle)*self.length/2]
        coord2 = [x_adjust + self.x-math.cos(self.angle)*self.length/2,
                  y_adjust + self.y-math.sin(self.angle)*self.length/2]
        pygame.draw.line(self.screen, white, coord1, coord2, 3)


class GameManager:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        #Create player
        self.player = Ship(screen, self.screen.get_width()/2, self.screen.get_height()/2)
        #Create the ground
        self.ground = Ground(screen)
        #List of intangible animation objects
        self.animation_list = []

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

    def animatePlayerDeath(self):
        #Add dead player lines to simulate ship breaking apart.
        corners = self.player.getCorners()
        for i in range(len(corners)):
            x1 = corners[i][0]
            y1 = corners[i][1]
            dx = self.player.dx+random.random()-0.5
            dy = self.player.dy+random.random()-0.5
            if i<len(corners)-1:
                x2 = corners[i+1][0]
                y2 = corners[i+1][1]
            else: #This else wraps end of the list to the start.
                x2 = corners[0][0]
                y2 = corners[0][1]
            self.animation_list.append(Line(self.screen, x1,y1, x2,y2, dx, dy))


class Ground:
    def __init__(self, surface):
        self.surface = surface
        self.ground_heights = []
        for i in range(ground_segments):
            self.ground_heights.append([i*segment_spacing,
                                self.surface.get_height()/2+random.randint(0,height_variation)])

    def draw(self, povx, povy):
        x_adjust = self.surface.get_width()/2 - povx
        y_adjust = self.surface.get_height()/2 - povy
        adjusted_heights = []
        for coord in self.ground_heights:
            #If the x value is off screen, ignore it. Otherwise, include it.
            #TODO
            #if coord[0]+x_adjust > 0 and coord[0]+x_adjust < self.surface.get_width():
            adjusted_heights.append([coord[0]+x_adjust, coord[1]+y_adjust])
        for i in range(len(adjusted_heights)-1):
            pygame.draw.line(self.surface, white, adjusted_heights[i], adjusted_heights[i+1], 3)


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
        gravity = 2
        #Move dx and dy
        self.x += self.dx
        self.y += self.dy + gravity
        #Wrap the world.
        if self.x > ground_segments*segment_spacing:
            self.x -= ground_segments*segment_spacing

    def getCorners(self):
        #Returns list of points to draw the ship
        points = []
        #Nose
        angle = self.angle+math.pi*2
        x = self.surface.get_width()/2 + math.cos(angle)*self.radius*1.5
        y = self.surface.get_height()/2 + math.sin(angle)*self.radius*1.5
        points.append([x, y])
        #wing 1
        angle = self.angle+math.pi*2*(1.2/self.sides)
        x = self.surface.get_width()/2 + math.cos(angle)*self.radius
        y = self.surface.get_height()/2 + math.sin(angle)*self.radius
        points.append([x, y])
        #rear
        angle = self.angle+math.pi
        x = self.surface.get_width()/2 + math.cos(angle)*self.radius*0.5
        y = self.surface.get_height()/2 + math.sin(angle)*self.radius*0.5
        points.append([x, y])
        #wing 2
        angle = self.angle+math.pi*2*(1.8/self.sides)
        x = self.surface.get_width()/2 + math.cos(angle)*self.radius
        y = self.surface.get_height()/2 + math.sin(angle)*self.radius
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
        points = self.getCorners()
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
            if event.key == pygame.K_RETURN and gm.player.lives <= 0:
                gm = GameManager(screen, 0) #Reset to level 0
    #Send user input to the player if it's alive
    if gm.player.lives > 0:
        userInputToPlayer(gm.player)
    #fill screen with black
    screen.fill(black)
    gm.update()
    #Display level
    position = (width-150, 10)
    screen.blit(small_font.render("Level "+str(gm.level),True,white),position)
    #Check for game over
    if gm.player.lives <= 0:
        position = (width/2-100, height/2-20)
        screen.blit(large_font.render("Game Over",True,white),position)
        position = (width/2-75, height/2+40)
        screen.blit(small_font.render("[ENTER] to reset",True,white),position)
    #Update the screen
    pygame.display.flip()
    pygame.display.update()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()