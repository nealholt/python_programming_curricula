import math, random, pygame, time
"""Snake head will return a position, which is added to a list. This list is trimmed
at a value, the legth of the snake, upon which snake parts are created. The size
of the list increases as the snake size increases, and decreases as it decreases."""

#0---------------------------------------------------------------------------
#Snake Head Object
#An object which moves at a constant speed (delta) and changes direction
#given presses on the arrow keys. Contains the "size" variable which controls
#snake length and contains a function which returns its current position.

class SnakeHead():
    def __init__(self, width, height, length):
        #Initial position is in the center of the screen.
        self.x = width/2
        self.y = height/2

        #The distance traveled each revolution.
        self.delta = 10

        #The direction being faced. Either 0, which is to the right;
        #1, up; 2, left; 3, down.
        self.direction = 0

        #The length of the snake's body.
        self.length = length

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 10, 10))

    def move(self):
        if self.direction == 0:
            self.x = self.x + self.delta
        elif self.direction == 1:
            self.y = self.y + self.delta
        elif self.direction == 2:
            self.x = self.x - self.delta
        elif self.direction == 3:
            self.y = self.y - self.delta

    def sizeChange(self, size_delta):
        self.length = self.length + size_delta

    def changeDirection(self, num):
        self.direction = num

    def getPosition(self):
        return (self.x, self.y)

    def getLength(self):
        return self.length

#0---------------------------------------------------------------------------
#Apple Object
#An object which appears at a point which, when hit, goes to a different
#point.

class AppleBoi():
    def __init__(self, x, y):
        self.x = x - x%10
        self.y = y - y%10

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))

    def goToNewPlace(self, width, heigth):
        x = random.randint(5, width - 5)
        y = random.randint(5, heigth - 5)
        self.x = x - x%10
        self.y = y - y%10

    def getPos(self):
        return (self.x, self.y)

#0---------------------------------------------------------------------------
#Powerups Object
#An object similar to the "Apple" object with variable colors and whose type,
#a string variable, changes its benefit or downside.

class PowerUps():
    def __init__(self, x, y, ty):
        self.x = x - x%10
        self.y = y - y%10
        self.t = 500

        if ty == 0:
            self.color = (255, 255, 0)
        elif ty == 1:
            self.color = (0, 0, 255)
        elif ty == 2:
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 255)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))

    def goToNewPlace(self, width, heigth):
        x = random.randint(5, width - 5)
        y = random.randint(5, heigth - 5)
        self.x = x - x%10
        self.y = y - y%10

        rando = random.randint(0, 4)
        if rando == 0:
            self.color = (255, 255, 0)
        elif rando == 1:
            self.color = (0, 0, 255)
        elif rando == 2:
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 255)

    def getPos(self):
        return (self.x, self.y)

    def getTime(self):
        return self.t

    def getColor(self):
        return self.color

#0---------------------------------------------------------------------------
#Functions

def clipList(li, des_length):
    #Clips a given list, here a list of positions, to a given goal number.
    #Takes in the list and the goal number, and returns a list with the
    #goal number's worth of positions.
    if des_length > len(li):
        des_length = len(li)

    temp_list = []
    temp_list_two = []
    temp_list_three = []

    for i in range(len(li)):
        temp_list.append(li[len(li) - 1 - i])

    for i in range(des_length):
        temp_list_two.append(temp_list[i])

    for i in range(len(temp_list_two)):
        temp_list_three.append(temp_list_two[len(temp_list_two) - 1 - i])

    return temp_list_three

def drawSnakeParts(screen, x, y):
    #Draws a square at the positions in the given list.
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 10, 10))

def checkDeath(pos_list):
    #Verifies the snake doesn't run into a wall or itself.
    for pos in pos_list:
        if head.getPosition() == pos:
            return True

    if head.getPosition()[0] > 390 or head.getPosition()[0] < -5:
        return True
    elif head.getPosition()[1] > 390 or head.getPosition()[1] < -5:
        return True

    return False

#0---------------------------------------------------------------------------
#Central Code

#Initiates the pygame library.
pygame.init()


#Creates the pygame screen and sets the caption of the screen to "Snake!"
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake!")

#Creates an empty list which will be used later to hold positions the snake head
#was at.
positions_list = []

#A variable which is used to run the below loop. Changes when the snake hits itself or
#"starves."
dead = False

#Creates the three necessary objects: the snake's head, the apple and the power
#up. Note that there is only ONE apple object and ONE power-up object, both of
#which change position when hit.
head = SnakeHead(400, 400, 10)
apple = AppleBoi(random.randint(0, 400), random.randint(0, 400))
power = PowerUps(random.randint(0, 400), random.randint(0, 400), 0)

#The number of times the snake hits the apple.
points = 0

#Counters used to reset the effects of power ups and limit the amount of time a
#power up is available.
counter = 0
counter_two = 0

#Whether or not the game is paused, activated by pressing the space key.
pause = False

#Whether or not a power up is visible.
power_time = False

#The speed at which the screen changes. Will change with certain power ups.
tick_speed = 0.1

while dead != True:

    #This bunch of code checks for key hits, including that which pauses the
    #game.
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and pause != True:
                    head.changeDirection(2)
                if event.key == pygame.K_RIGHT and pause != True:
                    head.changeDirection(0)
                if event.key == pygame.K_UP and pause != True:
                    head.changeDirection(3)
                if event.key == pygame.K_DOWN and pause != True:
                    head.changeDirection(1)
                if event.key == pygame.K_SPACE:
                    pause = not pause

    #Assuming the game has not been paused, the following occurs.
    if pause == False:
        body_hit = False

        #Appends the position of the snake head into the position list, then
        #clips the list so that the snake size doesn't increase forever.
        #If you want to play a game of "don't hit yourself," disable the second
        #line and see how long you can survive.
        positions_list.append(head.getPosition())
        positions_list = clipList(positions_list, head.getLength())

        #Fills the background with black. One can switch it to white by setting
        #the color to (255, 255, 255).
        screen.fill((0, 0, 0))

        #Moves the snake head, then draws it.
        head.move()
        head.draw()

        #Draws a green square like the snake head's at the positions the head
        #was at.
        for i in range(len(positions_list)):
            drawSnakeParts(screen, positions_list[i][0], positions_list[i][1])

        #Draws the apple.
        apple.draw()

        #Checks if a power up is not already on the screen and then slightly
        #randomzies the time between power ups.
        power_num = random.randint(0, 30)
        if power_num == 27 and power_time == False:
            power_time = True
            counter_two = 25

        #When a power up is on the screen, this piece of code draws it, checks
        #if the snake head hits the power up, and makes sure the power up only
        #has limited screen time.
        if power_time == True and counter_two > 0:
            if head.getPosition() == power.getPos():
                if power.color == (255, 255, 0):
                    tick_speed = 0.05
                elif power.color == (0, 0, 255):
                    tick_speed = 0.2
                elif power.color == (0, 255, 0):
                    head.length = head.length * 2
                else:
                    head.length = int(head.length/2)
                power.goToNewPlace(400, 400)

            power.draw()
            counter_two -= 1
            if counter_two == 1:
                power_time = False
                power.goToNewPlace(400, 400)

        #Checks if the snake head hits the apple, adds a point to the score,
        #moves the apple to a new position and adds length to the snake.
        if head.getPosition() == apple.getPos():
            points = points + 1
            apple.goToNewPlace(400, 400)
            head.sizeChange(3)

        #Verfyies the snake is still alive.
        dead = checkDeath(positions_list)

        #Pauses for approx. 1/10 of a second.
        time.sleep(tick_speed)

        #Updates display.
        pygame.display.flip()

        #Resets powerups at certain points.
        counter = counter + 1
        if counter%50 == 0:
            head.sizeChange(-1)
        elif counter%25 == 0:
            tick_speed = 0.1

        #Checks if the snake "starves."
        if head.length == 0:
            dead = True

#After the snake's death, prints the number of points one got.
print("Game Over! You had " + str(points) + " points!")
pygame.quit()