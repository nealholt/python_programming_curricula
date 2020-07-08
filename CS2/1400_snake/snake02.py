import pygame, random

#Sarah Maurice found this online.
#Modified by nholtschulte

def getRandX():
    return random.randint(0, x_increments) * block_size

def getRandY():
    return random.randint(0, y_increments) * block_size


SNAKE_BODY = 0
FOOD_OBJ = 1
NOTHING = 2
def getObjectAt(x,y,snake,food):
    for body in snake.body:
        if body == [x,y]:
            return SNAKE_BODY
    if food == [x,y]:
        return FOOD_OBJ
    return NOTHING

def avoidSelfCollision(snake, food):
    x,y = snake.getNextPosition()
    if getObjectAt(x,y,snake,food) == SNAKE_BODY:
        if snake.direction == "LEFT":
            snake.direction = "UP"
        elif snake.direction == "RIGHT":
            snake.direction = "DOWN"
        elif snake.direction == "UP":
            snake.direction = "LEFT"
        elif snake.direction == "DOWN":
            snake.direction = "RIGHT"



def turnTowardFood(snake, food):
    if food[0] < snake.body[0][0] and snake.direction != "RIGHT":
        snake.direction = "LEFT"
    elif food[0] > snake.body[0][0] and snake.direction != "LEFT":
        snake.direction = "RIGHT"
    elif food[1] < snake.body[0][1] and snake.direction != "DOWN":
        snake.direction = "UP"
    elif food[1] > snake.body[0][1] and snake.direction != "UP":
        snake.direction = "DOWN"
    elif snake.direction == "LEFT":
        snake.direction = "DOWN"
    elif snake.direction == "RIGHT":
        snake.direction = "UP"
    elif snake.direction == "UP":
        snake.direction = "LEFT"
    elif snake.direction == "DOWN":
        snake.direction = "RIGHT"



class Snake():
    def __init__(self, x, y, length, color):
        self.body = [[x,y]]
        for i in range(1,length):
            temp = [self.body[0][0],self.body[0][1]] #must make deep copy
            temp[0] -= i*block_size
            self.body.append(temp)
        self.direction = "RIGHT"  # Initial direction
        self.color = color

    def getNextPosition(self):
        new_pos = [self.body[0][0],self.body[0][1]] #must make deep copy
        if self.direction == "RIGHT":
            new_pos[0] += block_size
        elif self.direction == "LEFT":
            new_pos[0] -= block_size
        elif self.direction == "DOWN":
            new_pos[1] += block_size
        elif self.direction == "UP":
            new_pos[1] -= block_size
        return new_pos

    def move(self):
        #Calculate new head position
        new_pos = self.getNextPosition()
        #Insert new head position
        self.body.insert(0, new_pos)
        #Remove the tail
        self.body.pop()

    def draw(self):
        for position in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(position[0], position[1], block_size, block_size))

    def collidedSelf(self):
        for block in self.body[1:]:
            if self.body[0] == block:
                return True
        return False

    def collidedWall(self):
        return self.body[0][0]<0 or self.body[0][0]>width or self.body[0][1]<0 or self.body[0][1]>height



block_size = 40
width = 1000
height = 600
x_increments = width/block_size - 1
y_increments = height/block_size - 1

fps = pygame.time.Clock()

red = pygame.Color("red")
green = pygame.Color("green")
black = pygame.Color("black")
orange = pygame.Color("orange")
white = pygame.Color("white")

snake = Snake(block_size, block_size, 3, green)

# Place the food randomly, excluding the border
food_position = [getRandX(), getRandY()]

screen = pygame.display.set_mode((width, height))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Choose direction by user input, block opposite directions
            key_right = event.key == pygame.K_RIGHT or event.key == ord("d")
            key_left = event.key == pygame.K_LEFT or event.key == ord("a")
            key_down = event.key == pygame.K_DOWN or event.key == ord("s")
            key_up = event.key == pygame.K_UP or event.key == ord("w")
            if key_right and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            elif key_left and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif key_down and snake.direction != "UP":
                snake.direction = "DOWN"
            elif key_up and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_ESCAPE:
                done = True # It will quit when esc is pressed

    #TODO TESTING
    turnTowardFood(snake, food_position)
    avoidSelfCollision(snake, food_position)

    snake.move()
    #Check food collision
    if snake.body[0] == food_position:
        #Duplicate tail of snake
        snake.body.append(snake.body[-1])
        #Respawn food
        food_position = [getRandX(), getRandY()]
    if snake.collidedWall() or snake.collidedSelf():
        done = True # Game over

    # Drawing
    screen.fill(black)
    snake.draw()
    #draw food
    pygame.draw.rect(screen, orange, pygame.Rect(food_position[0], food_position[1], block_size, block_size))
    pygame.display.flip()
    fps.tick(16)

pygame.quit()