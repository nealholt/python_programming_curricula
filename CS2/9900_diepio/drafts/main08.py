import pygame, math, random

pygame.init()

friction = 0.1
acceleration = 0.03
border_shove_impulse = 0.1
world_size = 2000

'''TODO next steps:
6. Shove out borders and show the borders.
7. Objects shove each other out
Keep this initially separate then make a third project integrating this with maze navigator.

    void moveToward(double elapsed_seconds, double x, double y)
    {
        if(y < this.getYCenter())
        {	//up
            this.changeVelocity(0, -speed*elapsed_seconds);
        }else
        {   //down
            this.changeVelocity(0, speed*elapsed_seconds);
        }
        if(x < this.getXCenter())
        {	//left
            this.changeVelocity(-speed*elapsed_seconds, 0);
        }else
        {   //right
            this.changeVelocity(speed*elapsed_seconds, 0);
        }
    }

    void moveAwayFrom(double elapsed_seconds, double x, double y)
    {
        if(y < this.getYCenter())
        {	//down
            this.changeVelocity(0, speed*elapsed_seconds);
        }else
        {   //up
            this.changeVelocity(0, -speed*elapsed_seconds);
        }
        if(x < this.getXCenter())
        {	//right
            this.changeVelocity(speed*elapsed_seconds, 0);
        }else
        {   //left
            this.changeVelocity(-speed*elapsed_seconds, 0);
        }
    }

    public void update(double elapsed_seconds)
    {
        //Apply friction
        this.changeVelocity(this.getdx() * friction * elapsed_seconds, this.getdy() * friction * elapsed_seconds);
        //Move
        //Cloak and mimic ships gain a burst of speed when they are not stationary
        //and they have positive stamina.
        if(stamina > 0 && //stamina up
                Math.abs(this.getdx())+Math.abs(this.getdy())>10) //not stationary
        {    //Used by mimic and cloak ships to put on a burst of speed temporarily.
            this.move(elapsed_seconds*3);
            stamina -= elapsed_seconds;
        }
        else
        {   //All other ships move normally.
            this.move(elapsed_seconds);
            //Cloak and mimic ships recover stamina while stationary.
            //Up to 1.5 seconds of burst speed.
            if((this.shape==Constants.SHAPE_MIMIC || this.shape==Constants.SHAPE_CLOAK) &&
                    Math.abs(this.getdx())+Math.abs(this.getdy())<10 &&
                    stamina<1.5)
            {
                stamina += elapsed_seconds;
            }
        }
        //Keep this sprite in bounds
        if(((BoardTopDown)board_reference).pushy_walls)
        {
            this.pushInBounds(elapsed_seconds);
        }
        else
        {
            this.bounceInBounds();
        }
        //Cooldown the damage immunity from most recent source of damage to this sprite.
        redamage_cooldown -= elapsed_seconds;
    }

	/* Moves the other sprite out of collision with this sprite */
	public void shoveOut(SpritePhysics other)
	{
		//Get angle to other
		double angle = this.angleToDestination(other.getXCenter(), other.getYCenter());
		//get dx and dy towards other.
		double temp_dx = Math.cos(angle);
		double temp_dy = Math.sin(angle);
		/* Rectangular collision is the default so only
		use a circular collision check if the other
		sprite is also circular, otherwise defer to the
		other sprite. */
		if(other instanceof SpriteCircular)
		{	//Get the amount of overlap.
			double overlap = depthOfPenetration((SpriteCircular)other);
			//Move other out by the appropriate amount
			other.setX(other.getX() + temp_dx*overlap);
			other.setY(other.getY() + temp_dy*overlap);
			//Bounce other out
			((SpriteCircular) other).bounceOff(this);
		}
		else
		{
			System.out.println("WARNING: in SpriteCircular. Shoving a rectangular object out of a circular object has not been implemented.");
		}
	}

	/* Bounce off the other sprite off of this using vectors
	 * http://stackoverflow.com/questions/573084/how-to-calculate-bounce-angle
	 */
	public void bounceOff(Sprite other)
	{
		//Get the dy and dx components of the line from
		//this.center to other.center
		double[] normal_vector =
			{
				this.getXCenter() - other.getXCenter(),
				this.getYCenter() - other.getYCenter()
			};
		//Separate other's velocity into the part perpendicular
		//to other, u, and the part parallel to other, w.
		double v_dot_n = this.getdx()*normal_vector[0] + this.getdy()*normal_vector[1];
		double square_of_norm_length = Math.pow(normal_vector[0],2) + Math.pow(normal_vector[1],2);
		double multiplier = v_dot_n / square_of_norm_length;
		double[] u_vector =
			{
				normal_vector[0]*multiplier,
				normal_vector[1]*multiplier
			};
		double[] w_vector =
			{
					this.getdx() - u_vector[0],
					this.getdy() - u_vector[1]
			};
		//Determine the velocity post collision while
		//factoring in the elasticity and friction of
		//the wall.
		this.setVelocity(
				w_vector[0]*(1-this.getBounceFriction())-u_vector[0]*this.getElasticity(),
				w_vector[1]*(1-this.getBounceFriction())-u_vector[1]*this.getElasticity());
		//Get the collision angle mainly to see if we were hit
		//from behind
		double angle_difference = getCollisionAngle(other);
		//Change direction from having bounced out.
		if(this.getFlipDirection())
		{	//Don't do this if this sprite struck other from behind.
			if(Math.abs(angle_difference) < Math.PI/2)
			{
				this.setAngle(Math.atan2(this.getdy(),this.getdx()));
			}
		}
	}
'''

class DiepSprite:
    def __init__(self, screen, x, y, color, radius, speed, draw_heading=True):
        self.screen = screen
        self.color = color
        self.x = x+radius #center x
        self.y = y+radius #center y
        self.angle = 0
        self.radius = radius
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.draw_heading = draw_heading

    def rotate(self, turn_amount):
        self.angle += turn_amount
        self.dx = math.cos(self.angle)
        self.dy = math.sin(self.angle)

    def move(self):
        self.x += self.dx*self.speed
        self.y += self.dy*self.speed
        self.rect = pygame.Rect(self.x-self.radius,
                                self.y-self.radius,
                                self.radius*2,
                                self.radius*2)

    def update(self):
        self.move()
        #apply friction
        self.dx = (1-friction)*self.dx
        self.dy = (1-friction)*self.dy
        #Keep critter in bounds
        if self.x<0:
            self.dx += border_shove_impulse
        elif self.x > world_size:
            self.dx -= border_shove_impulse
        if self.y<0:
            self.dy += border_shove_impulse
        elif self.y > world_size:
            self.dy -= border_shove_impulse

    def draw(self, povx, povy):
        #Get coordinate adjustments
        x_adjust = self.screen.get_width()/2 - povx
        y_adjust = self.screen.get_height()/2 - povy
        r = self.rect.copy()
        r.x += x_adjust
        r.y += y_adjust
        pygame.draw.ellipse(self.screen, self.color, r)
        #Draw little heading circle
        if self.draw_heading:
            heading_radius = 10
            heading = pygame.Rect(x_adjust+self.x-heading_radius+math.cos(self.angle)*100,
                                  y_adjust+self.y-heading_radius+math.sin(self.angle)*100,
                                  heading_radius*2,
                                  heading_radius*2)
            pygame.draw.ellipse(self.screen, self.color, heading)

    def distanceTo(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def angleTo(self,x,y):
        x = x - self.x
        y = y - self.y
        return math.atan2(y,x)

    def depthOfPenetration(self, other):
        #Return the depth of penetration of one sprite into the other.
        #Will return negative values if the sprites are not touching.
        return (self.radius + other.radius) - self.distanceTo(other)



class PlayerCritter(DiepSprite):
    def __init__(self, screen, x, y, color, radius, speed):
        super().__init__(screen, x, y, color, radius, speed)

    def update(self):
        pos = pygame.mouse.get_pos()
        x = pos[0] - self.screen.get_width()/2
        y = pos[1] - self.screen.get_height()/2
        self.angle = math.atan2(y,x)
        super().update()

    #Override super class's draw function
    def draw(self, povx, povy):
        r = self.rect.copy()
        center_x = self.screen.get_width()/2
        center_y = self.screen.get_height()/2
        r.x = center_x - self.radius
        r.y = center_y - self.radius
        pygame.draw.ellipse(self.screen, self.color, r)
        #Draw little heading circle
        heading_radius = 10
        heading = pygame.Rect(center_x-heading_radius+math.cos(self.angle)*100,
                              center_y-heading_radius+math.sin(self.angle)*100,
                              heading_radius*2,
                              heading_radius*2)
        pygame.draw.ellipse(self.screen, self.color, heading)
        #Draw edges of the world
        x_diff = screen_width/2 - self.x
        if x_diff > 0:
            pygame.draw.rect(self.screen, green, [0,0,x_diff,screen_height])
        elif world_size - self.x < screen_width/2:
            x_diff = screen_width/2-(world_size-self.x)
            pygame.draw.rect(self.screen, green, [screen_width-x_diff,0,x_diff,screen_height])
        y_diff = screen_height/2 - self.y
        if y_diff > 0:
            pygame.draw.rect(self.screen, green, [0,0,screen_width,y_diff])
        elif world_size - self.y < screen_height/2:
            y_diff = screen_height/2-(world_size-self.y)
            pygame.draw.rect(self.screen, green, [0,screen_height-y_diff,screen_width,y_diff])



class EnemyCritter(DiepSprite):
    def __init__(self, screen, x, y, color, radius, speed, target):
        super().__init__(screen, x, y, color, radius, speed)
        self.target = target

    #Override super class's update function
    def update(self):
        self.angle = self.angleTo(self.target.x, self.target.y)
        self.dx = math.cos(self.angle)
        self.dy = math.sin(self.angle)
        self.move()


#Initialize variables:
clock = pygame.time.Clock()
screen_width = 1100
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

critter = PlayerCritter(  screen,
                        100,#x
                        100,#y
                        blue,
                        50,#radius
                        20)#speed

npc_critter = EnemyCritter(screen,
                          200,#x
                          200,#y
                          yellow,
                          35,#radius
                          4,#speed
                          critter)#target of enemy

foods = []
for i in range(10):
    f = DiepSprite(screen, random.randint(0,1000), random.randint(0,1000),#x,y
                    red, 15, 0, draw_heading=False)
    foods.append(f)

#Main program loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #print(event.key) #Print value of key press
            if event.key == pygame.K_ESCAPE:
                done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        critter.dy -= acceleration
    if keys[pygame.K_DOWN]:
        critter.dy += acceleration
    if keys[pygame.K_LEFT]:
        critter.dx -= acceleration
    if keys[pygame.K_RIGHT]:
        critter.dx += acceleration

    screen.fill((0,0,0)) #fill screen with black
    #Update and draw critters
    critter.update()
    critter.draw(critter.x, critter.y)
    npc_critter.update()
    npc_critter.draw(critter.x, critter.y)
    for f in foods:
        f.update()
        f.draw(critter.x, critter.y)
    pygame.display.flip()
    pygame.display.update()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()