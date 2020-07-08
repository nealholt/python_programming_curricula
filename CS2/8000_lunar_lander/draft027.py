import pygame, math, random

'''
Contrails - thin straight lines off of edgepoints of ship in opposite direction of line of motion, appearing only in atmosphere.
Controls: provide lift when flying at angles near horizontal.

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

atmo_upper_limit = -2000
atmo_lower_limit = 0
atmo_layer_width = 100
atmo_total_width = abs(atmo_upper_limit)
water_upper_limit = 0

wave_radius = 20

cloud_size = 70
cloud_count = 50

star_count = 100

splash_width = 4
splash_limit = 80
splash_dampening = 30
splash_spread = 6
splash_spread_force_reduce = 0.2

#Create constants for randomly generated ground.
ground_min_width = 100
ground_max_width = 300
ground_min_height = 800
ground_max_height = -100
ground_total_width = width*3 #3 screen widths

random.seed(772)


def onScreen(x,y):
    return x>=0 and x<=width and y>=0 and y<=height


def getFriction(y):
    '''Takes the height of the ship and returns the
    friction based on that height.'''
    if y < atmo_upper_limit:
        return 0 #No friction above the atmosphere
    elif y < atmo_lower_limit:
        #Atmospheric friction is a function of height
        percent = y / (atmo_upper_limit-atmo_lower_limit)
        return percent*0.02
    else: #in water
        return 0.1 #Considerably higher friction in water


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


class GameManager:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        #Create player
        self.player = Ship(screen, 400, -400)
        #Create the ground
        self.ground = Ground(screen)
        #List of intangible animation objects
        self.animation_list = []
        self.victory = False
        #Create clouds
        for i in range(cloud_count):
            x = random.randint(-width/2, ground_total_width+width/2)
            y = int(atmo_upper_limit/3+random.randint(-3*atmo_layer_width,2*atmo_layer_width))
            self.animation_list.append(Clouds(screen, x, y))
        #Create stars
        for i in range(star_count):
            x = random.randint(-width/2, ground_total_width+width/2)
            y = int(random.randint(2*atmo_upper_limit,atmo_upper_limit))
            self.animation_list.append(Star(screen, x, y))
        #Manage splashes in the water
        self.splash_manager = SplashManager(screen)

    def update(self):
        #Get coordinate adjustments to center player on the screen
        x_adjust = self.screen.get_width()/2 - self.player.x
        y_adjust = self.screen.get_height()/2 - self.player.y
        #Move and draw and possibly delete animations
        self.ground.draw(x_adjust, y_adjust)
        for i in reversed(range(len(self.animation_list))):
            item = self.animation_list[i]
            item.move()
            item.draw(x_adjust, y_adjust)
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
        #Update and draw splashes
        self.splash_manager.update(self.player)
        self.splash_manager.draw(x_adjust, y_adjust)


class SplashManager:
    def __init__(self, screen):
        self.screen = screen
        self.splash_list = []

    def update(self, player):
        #Adjust height of splashes and delete any that are expired
        for i in reversed(range(len(self.splash_list))):
            self.splash_list[i].move()
            if self.splash_list[i].height <= 0:
                del self.splash_list[i]
        #Check player's height above water and add splashes as needed
        if player.y > water_upper_limit-splash_limit and player.y < water_upper_limit+wave_radius:
            amount_splash = (splash_limit+player.y)/splash_dampening
            #Discretize the splash's x value in order to replace previous
            #splashes. This is an efficiency change.
            x = player.x - (player.x%splash_width)
            #Create a list of new splashes in order
            new_splashes_left = []
            new_splashes_right = []
            center = Splash(self.screen, x, wave_radius+1, -amount_splash)
            #Create reduced splashes on either side of center
            for i in range(1,splash_spread):
                splash_force = -amount_splash/(i*splash_spread_force_reduce+1)
                new_splashes_right.append(Splash(self.screen, x+i*splash_width, wave_radius+1, splash_force))
                new_splashes_left = [Splash(self.screen, x-i*splash_width, wave_radius+1, splash_force)] + new_splashes_left
            self.addSplashes(new_splashes_left + [center] + new_splashes_right)

    def addSplashes(self, splash_set):
        '''Check for overlapping splashes and modify or replace old splashes
        so that multiple splash rectangles are not being drawn over top of
        each other.'''
        added = False
        for i in range(len(self.splash_list)):
            if self.splash_list[i].x == splash_set[0].x:
                for s in splash_set:
                    if i >= len(self.splash_list):
                        self.splash_list.append(s)
                    else:
                        self.splash_list[i].dy = min(self.splash_list[i].dy, s.dy)
                        self.splash_list[i].height = max(self.splash_list[i].height, s.height)
                        i += 1
                added = True
                break
        if not added:
            self.splash_list = self.splash_list + splash_set

    def draw(self, x_adjust, y_adjust):
        for s in self.splash_list:
            s.draw(x_adjust, y_adjust)


class Splash(Animation):
    def __init__(self, screen, x, y, dy):
        super().__init__(screen, x,y, 0, dy)
        self.height = 0

    def move(self):
        #Override the parent class's move method
        self.height -= self.dy
        self.dy += gravity

    def draw(self, x_adjust, y_adjust):
        r = pygame.Rect(self.x+x_adjust, self.y+y_adjust-self.height, splash_width, self.height)
        pygame.draw.rect(self.screen, blue, r)


class Bubbles(Animation):
    def __init__(self, screen, x, y):
        self.size = random.randint(10,25)
        super().__init__(screen,
                int(x-self.size/2)+random.randint(-20,20),
                int(y-self.size/2)+random.randint(-20,20),
                0,-1) #dx, dy
        self.timeout = 35+random.randint(-20,20)
        self.remove_me = False

    def move(self):
        super().move()
        self.timeout -= 1
        self.remove_me = self.timeout < 0 or self.y+self.size/2 < water_upper_limit+wave_radius

    def draw(self, x_adjust, y_adjust):
        pygame.draw.ellipse(self.screen, white, [self.x+x_adjust, self.y+y_adjust, self.size, self.size],1)


class Clouds(Animation):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 0, 0)
        self.xs = []
        self.ys = []
        num_puffs = random.randint(3,6)
        for i in range(num_puffs):
            self.xs.append(x+random.randint(100,160))
            self.ys.append(y+random.randint(50,80))
        self.remove_me = False

    def draw(self, x_adjust, y_adjust):
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
        super().__init__(screen, x, y, 0, 0)
        self.remove_me = False

    def draw(self, x_adjust, y_adjust):
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
        #Start the ground off with a point at x=0 and y= a random height
        ground_coords = [[0,random.randint(ground_max_height,ground_min_height)]]
        #While the most recently added x value is less than the total
        #desired ground width, keep adding new random points.
        while ground_coords[-1][0] < ground_total_width:
            new_point = [ground_coords[-1][0]+random.randint(ground_min_width, ground_max_width),
                        random.randint(ground_max_height,ground_min_height)]
            ground_coords.append(new_point)
        #Delete last point to stop weird wrapping issues
        del ground_coords[-1]
        #Sanity check that the x values are monotonically increasing
        for i in range(len(ground_coords)-1):
            if ground_coords[i][0] > ground_coords[i+1][0]:
                print('ERROR in Ground constructor. ground_coords x values out of order')
                pygame.quit()
                exit()
        #The easiest solution to ground wrapping is creating a whole copy of
        #the ground before and after the generated ground, so we do that now.
        ground_left = []
        ground_right = []
        for g in ground_coords:
            ground_left.append([g[0]-ground_total_width, g[1]])
            ground_right.append([g[0]+ground_total_width, g[1]])
        #Put it all together
        self.ground_heights = ground_left+ground_coords+ground_right
        #Sanity check that the x values are monotonically increasing
        for i in range(len(self.ground_heights)-1):
            if self.ground_heights[i][0] > self.ground_heights[i+1][0]:
                print('ERROR in Ground constructor. self.ground_heights x values out of order')
                pygame.quit()
                exit()

    def shipHitGround(self, ship):
        points = ship.getCorners(ship.x, ship.y)
        for p in points:
            if p[1] >= self.getHeightAt(p[0]):
                return True
        return False

    def getHeightAt(self, x):
        #Get coordinates that x is between and use those coordinates
        #as a line to calculate the height of the ground at that x value.
        for i in range(len(self.ground_heights)-1):
            if x>=self.ground_heights[i][0] and x<self.ground_heights[i+1][0]:
                start = self.ground_heights[i]
                end = self.ground_heights[i+1]
                slope = (end[1]-start[1]) / (end[0]-start[0])
                #Point slope form:
                return slope*(x-end[0])+end[1]

    def draw(self, x_adjust, y_adjust):
        #Store bottom atmosphere color for drawing waves
        lowest_atmo_color = 0,0,0
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
            if water_upper_limit+y_adjust > 0:
                adjust = x_adjust%wave_radius
                i = 0
                while i*wave_radius*2 < self.screen.get_width()+wave_radius*2:
                    r = pygame.Rect(i*wave_radius*2-adjust, water_top-wave_radius, wave_radius*2, wave_radius*2)
                    pygame.draw.ellipse(self.screen, lowest_atmo_color, r)
                    i = i+1
        #Draw the ground
        is_visible = False #is any ground visible? if not, sskip drawing.
        adjusted_coords = []
        #This next line just adds an extra point at the bottom left corner
        #of the screen so there can be a complete polygon to fill in.
        adjusted_coords.append([0,height])
        #Add in adjusted coordinates
        add_coordinates = False
        for i in range(len(self.ground_heights)):
            #If one coordinate is off screen and the next is on, then we've
            #found our starting point.
            if not add_coordinates and\
            self.ground_heights[i][0]+x_adjust < 0 and\
            self.ground_heights[i+1][0]+x_adjust >= 0:
                add_coordinates = True
            if add_coordinates:
                temp = [self.ground_heights[i][0]+x_adjust, self.ground_heights[i][1]+y_adjust]
                adjusted_coords.append(temp)
                #If any ground coordinate is on screen, draw the whole ground
                #polygon. This will sometimes be a little wonky when no points
                #are on screen, but the line between points should be.
                #I'm ok with that.
                if onScreen(temp[0], temp[1]):
                    is_visible = True
            #If current coordinate is off screen and the next is off, then we've
            #found our ending point.
            if add_coordinates and\
            self.ground_heights[i][0]+x_adjust >= width and\
            self.ground_heights[i+1][0]+x_adjust > width:
                break
        #This next line just adds an extra point at the bottom right corner
        #of the screen so there can be a complete polygon to fill in.
        adjusted_coords.append([width,height])
        #If any points are visible on screen, draw the whole polygon.
        if is_visible:
            pygame.draw.polygon(self.screen, green, adjusted_coords)
        #TODO
        print()
        for a in adjusted_coords:
            print(a)


class Ship(Animation):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, 0, 0)
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
        super().move()
        #Apply gravity
        self.dy += gravity
        #Apply friction
        f = getFriction(self.y)
        self.dx = self.dx*(1-f)
        self.dy = self.dy*(1-f)
        #Screen wrap the player
        if self.x<0:
            self.x += ground_total_width
        if self.x>ground_total_width:
            self.x -= ground_total_width

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