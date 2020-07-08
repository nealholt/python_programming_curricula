import pygame, math, random

'''
Next steps:
    Collision with the ground.
    Stronger gravity
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
green = 0,255,0

ground_segments = 10
segment_spacing = 200
height_variation = 500
landing_pad_index = 8
landing_pad_width = 50


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
            #Check for a collision with the ground
            points = self.player.getCorners(self.player.x, self.player.y)
            for p in points:
                if p[1] >= self.ground.getHeightAt(p[0]):
                    self.player.lives = 0
                    break


class Ground:
    def __init__(self, surface):
        self.surface = surface
        self.ground_heights = []
        for i in range(ground_segments):
            self.ground_heights.append([i*segment_spacing,
                                self.surface.get_height()/2+random.randint(0,height_variation)])

    def getHeightAt(self, x):
        #Get coordinates that x is between and use those coordinates
        #as a line to calculate the height of the ground at that x value.
        start = self.ground_heights[int(x/segment_spacing)]
        end = self.ground_heights[int(x/segment_spacing)+1]
        slope = (end[1]-start[1]) / (end[0]-start[0])
        #Point slope form:
        return slope*(x-end[0])+end[1]

    def draw(self, povx, povy):
        x_adjust = self.surface.get_width()/2 - povx
        y_adjust = self.surface.get_height()/2 - povy
        #Get starting index
        start = int((povx - self.surface.get_width()/2)/segment_spacing)-1
        #Get ending index
        end = int((povx + self.surface.get_width()/2)/segment_spacing)+1
        #Get line segments
        adjusted_heights = []
        landing_index = -1
        for i in range(start,end+1):
            index = i%len(self.ground_heights)
            adjusted_heights.append([i*segment_spacing+x_adjust,
                                    self.ground_heights[index][1]+y_adjust])
            #Check for a match with the landing pad and make it a special case
            if index == landing_pad_index:
                landing_index = len(adjusted_heights)-1
                adjusted_heights.append([i*segment_spacing+x_adjust+landing_pad_width,
                                         adjusted_heights[landing_index][1]])
        #Draw the line segments
        for i in range(len(adjusted_heights)-1):
            color = white
            thickness = 3
            if i == landing_index:
                color = green
                thickness = 5
            pygame.draw.line(self.surface, color, adjusted_heights[i], adjusted_heights[i+1], thickness)


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
        elif self.x < 0:
            self.x += ground_segments*segment_spacing

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