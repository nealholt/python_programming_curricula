import pygame, math, random

'''
Draw waves (cut out waves from the water) - draw water then, having remembered color of bottom atmosphere layer, draw evenly spaced circles along the top of the water to make it look like there are waves. Do this before draing land.
    Move waves side to side (move the cut out circles)
Draw splash when the ship flies low (make it same color as water). Narrow vertical water bars rise up and then sink down at player's most recent location
Change physics based on conditions: friction, lift when flying close to horizontal.
	-ballistic asteroids controls kept
	-friction is a function of height in atmosphere, zero in space, sharp transition to high friction in water.
	-constant gravity
	-lift at angles near horizontal
Make player screen wrap.
Contrails - thin straight lines off of edgepoints of ship in opposite direction of line of motion, appearing only in atmosphere.

Complete game:
Levels to complete for high score.
Levels are beaten by acquiring certain amount of money. Score is based on time only.
Levels are little solar systems to trade in.
Features: Use gravity sling shot to conserve fuel, use atmopheric braking to conserve fuel, scoop fuel out of upper atmosphere in dangerous maneuver, mine resources in asteroid belt, trade goods between locations in dynamic economy, upgrade ship to be able to visit hot planets, high gravity planets, high radiation planets, etc. Upgrade cargo space, aerodynamic-ness, thrust. Buy weapons to fight off pirates or just flee from them.

Get snes controller input and play with snes? Make it easy to transition between control schemes. Array of buttons and just switch out the arrays.
Fuel
Pickups
Enemies
Dirty rects for efficiency
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
blue = 0,0,255
purple = 200,25,200

gravity = 0.05

landing_pad_index = 8

ground_lower_limit = 500
atmo_upper_limit = -2000
atmo_lower_limit = 0
atmo_layer_width = 100
atmo_total_width = abs(atmo_upper_limit)
water_upper_limit = 0

wave_radius = 20

cloud_size = 70
cloud_count = 50

star_count = 100

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
        #Create clouds
        for i in range(cloud_count):
            x = random.randint(0,self.screen.get_width()*2)
            y = int(atmo_upper_limit/3+random.randint(-3*atmo_layer_width,2*atmo_layer_width))
            self.animation_list.append(Clouds(screen, x, y))
        #Create stars
        for i in range(star_count):
            x = random.randint(0,self.screen.get_width()*2)
            y = int(random.randint(2*atmo_upper_limit,atmo_upper_limit))
            self.animation_list.append(Star(screen, x, y))


    def update(self):
        #Move and draw and possibly delete animations
        self.ground.draw(self.player.x, self.player.y)
        for i in reversed(range(len(self.animation_list))):
            item = self.animation_list[i]
            item.move()
            item.draw(self.player.x, self.player.y)
            if item.remove_me:
                del self.animation_list[i]
        #Draw the player if the player is still alive
        if self.player.lives > 0:
            self.player.move()
            self.player.draw()
            #Check for a collision with the ground
            if self.ground.shipHitGround(self.player):
                self.player.lives = 0
            #Check if animations should be added.
            #If the player is in water, add bubbles
            if self.player.y>water_upper_limit:
                self.animation_list.append(Bubbles(self.screen, self.player.x, self.player.y))


class Animation:
    def __init__(self, screen, x, y, dx, dy):
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy


class Bubbles(Animation):
    def __init__(self, screen, x, y):
        self.size = random.randint(10,25)
        Animation.__init__(self, screen,
                int(x-self.size/2)+random.randint(-20,20),
                int(y-self.size/2)+random.randint(-20,20),
                0,-1) #dx, dy
        self.timeout = 35+random.randint(-20,20)
        self.remove_me = False

    def move(self):
        Animation.move(self)
        self.timeout -= 1
        self.remove_me = self.timeout < 0 or self.y+self.size/2 < water_upper_limit+wave_radius

    def draw(self, povx, povy):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        pygame.draw.ellipse(self.screen, white, [self.x+x_adjust, self.y+y_adjust, self.size, self.size],1)


class Clouds(Animation):
    def __init__(self, screen, x, y):
        Animation.__init__(self, screen, x, y, 0, 0)
        self.xs = []
        self.ys = []
        num_puffs = random.randint(3,6)
        for i in range(num_puffs):
            self.xs.append(x+random.randint(100,160))
            self.ys.append(y+random.randint(50,80))
        self.remove_me = False

    def draw(self, povx, povy):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        #Check if the cloud is remotely near the player before drawing
        y = y_adjust+self.ys[0]
        x = x_adjust+self.xs[0]
        if y>-cloud_size and y-cloud_size<self.screen.get_height() and \
        x>-cloud_size and x-cloud_size<self.screen.get_width():
            #Draw the cloud
            for i in range(len(self.xs)):
                pygame.draw.ellipse(self.screen, white, [self.xs[i]+x_adjust, self.ys[i]+y_adjust, cloud_size, cloud_size])


class Star(Animation):
    def __init__(self, screen, x, y):
        Animation.__init__(self, screen, x, y, 0, 0)
        self.remove_me = False

    def draw(self, povx, povy):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        #Check if the star is remotely near the player before drawing
        y = y_adjust+self.y
        x = x_adjust+self.x
        if y>0 and y<self.screen.get_height() and \
        x>0 and x<self.screen.get_width():
            #Draw star
            coord1 = [self.x+x_adjust, self.y+y_adjust-1]
            coord2 = [self.x+x_adjust, self.y+y_adjust+1]
            pygame.draw.line(self.screen, white, coord1, coord2)
            coord1 = [self.x+x_adjust-1, self.y+y_adjust]
            coord2 = [self.x+x_adjust+1, self.y+y_adjust]
            pygame.draw.line(self.screen, white, coord1, coord2)


class Ground:
    def __init__(self, screen):
        self.screen = screen
        self.ground_heights = [[0,400],[200,250],[400,200],[600,350],
                              [800,50],[1000,300],[1200,-100],[1400,100],
                              [1600,200],[1650,200],#Landing pad start and end
                              [1800,150],[2000,450],[2200,475]]

    def overLandingPad(self,x):
        return x>self.ground_heights[landing_pad_index][0] and x<self.ground_heights[landing_pad_index+1][0]

    def shipHitGround(self, ship):
        points = ship.getCorners(ship.x, ship.y)
        for p in points:
            if p[1] >= self.getHeightAt(p[0]):
                return True
        return False

    def getHeightAt(self, x):
        #Get coordinates that x is between and use those coordinates
        #as a line to calculate the height of the ground at that x value.
        if x<=self.ground_heights[0][0] or x>=self.ground_heights[-1][0]:
            return ground_lower_limit
        for i in range(len(self.ground_heights)-1):
            if x>=self.ground_heights[i][0] and x<self.ground_heights[i+1][0]:
                start = self.ground_heights[i]
                end = self.ground_heights[i+1]
                slope = (end[1]-start[1]) / (end[0]-start[0])
                #Point slope form:
                return slope*(x-end[0])+end[1]

    def onScreen(self,x,y):
        return x>=0 and x<=self.screen.get_width() and y>=0 and y<=self.screen.get_height()

    def draw(self, povx, povy):
        #Store bottom atmosphere color for drawing waves
        lowest_atmo_color = 0,0,0
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        #Draw atmosphere
        for i in range(atmo_upper_limit,atmo_lower_limit,atmo_layer_width):
            atmo_top = max(i+y_adjust,0)
            atmo_bottom = max(i+y_adjust+atmo_layer_width,0)
            if atmo_bottom!=atmo_top:
                if atmo_top<self.screen.get_height(): #If atmo is on screen
                    temp = 255+int(i*240/atmo_total_width)
                    lowest_atmo_color = temp,temp,temp
                    pygame.draw.rect(self.screen, lowest_atmo_color, [0,atmo_top,self.screen.get_width(), min(atmo_layer_width,self.screen.get_height()-atmo_top)])
                else:
                    return
        #Draw the water
        water_top = max(water_upper_limit+y_adjust, 0)
        if water_top<self.screen.get_height(): #If water is on screen
            pygame.draw.rect(self.screen, blue, [0,water_top,self.screen.get_width(), self.screen.get_height()-water_top])
            #Draw cut out circles as waves
            adjust = povx%wave_radius
            i = 0
            while i*wave_radius*2 < self.screen.get_width()+wave_radius*2:
                r = pygame.Rect(i*wave_radius*2-adjust, water_top-wave_radius, wave_radius*2, wave_radius*2)
                pygame.draw.ellipse(self.screen, lowest_atmo_color, r)
                i = i+1
        else:
            return
        #Draw the ground
        is_visible = False #is any ground visible? if not, save on the drawing.
        adjusted_coords = []
        #This next line just adds an extra point so there can be a complete
        #polygon to fill in.
        adjusted_coords.append([0+x_adjust,1000+y_adjust])
        #Adjust all the other coordinates
        for coord in self.ground_heights:
            temp = [coord[0]+x_adjust,coord[1]+y_adjust]
            adjusted_coords.append(temp)
            if self.onScreen(temp[0], temp[1]):
                is_visible = True
        #This next line just adds an extra point so there can be a complete
        #polygon to fill in.
        adjusted_coords.append([2200+x_adjust,1000+y_adjust])
        #If any points are visible on screen, draw the whole polygon.
        if is_visible:
            pygame.draw.polygon(self.screen, green, adjusted_coords)
        #Draw pseudo ground
        if self.onScreen(0,ground_lower_limit+y_adjust):
            pygame.draw.rect(self.screen, green, [0,ground_lower_limit+y_adjust,self.screen.get_width(), self.screen.get_height()-(ground_lower_limit+y_adjust)])


class Ship(Animation):
    def __init__(self, screen, x, y):
        Animation.__init__(self, screen, x, y, 0, 0)
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
        Animation.move(self)
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
            x = self.screen.get_width()/2 + math.cos(angle)*self.radius*0.7
            y = self.screen.get_height()/2 + math.sin(angle)*self.radius*0.7
            radius = 5
            r = pygame.Rect(x-radius,y-radius,radius*2,radius*2)
            pygame.draw.ellipse(self.screen, red, r)
        #Reset thrust
        self.thrust_on = False
        #Draw ship
        points = self.getCorners(self.screen.get_width()/2, self.screen.get_height()/2)
        pygame.draw.polygon(self.screen, purple, points)



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