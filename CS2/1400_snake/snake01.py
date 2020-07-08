import pygame, sys, time, random

#Sarah Maurice found this online.
#Modified by nholtschulte

def getRandX():
    return random.randint(0, x_increments) * block_size

def getRandY():
    return random.randint(0, y_increments) * block_size

block_size = 40
width = 1000
height = 600
x_increments = width/block_size - 1
y_increments = height/block_size - 1

fps = pygame.time.Clock()
direction = "RIGHT"  # Initial direction
snake_position = [block_size, block_size]  # Initial snake position
snake_body = [[100, 50], [90, 50], [100, 50]]
# It places the food randomly, excluding the border
food_position = [getRandX(), getRandY()]
food_spawn = True
# Game surface
player_screen = pygame.display.set_mode((width, height))
# Will define the colors
red = pygame.Color("red")
green = pygame.Color("green")
black = pygame.Color("black")
orange = pygame.Color("orange")
white = pygame.Color("white")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quiting()
        elif event.type == pygame.KEYDOWN:
            # Choose direction by user input, block opposite directions
            key_right = event.key == pygame.K_RIGHT or event.key == ord("d")
            key_left = event.key == pygame.K_LEFT or event.key == ord("a")
            key_down = event.key == pygame.K_DOWN or event.key == ord("s")
            key_up = event.key == pygame.K_UP or event.key == ord("w")
            if key_right and direction != "LEFT":
                direction = "RIGHT"
            elif key_left and direction != "RIGHT":
                direction = "LEFT"
            elif key_down and direction != "UP":
                direction = "DOWN"
            elif key_up and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_ESCAPE:
                done = True # It will quit when esc is pressed
    # Simulates the snake movement(together with snake_body_pop)
    if direction == "RIGHT":
        snake_position[0] += block_size
    elif direction == "LEFT":
        snake_position[0] -= block_size
    elif direction == "DOWN":
        snake_position[1] += block_size
    elif direction == "UP":
        snake_position[1] -= block_size
    # Body mechanics
    snake_body.insert(0, list(snake_position))
    if snake_position == food_position:
        food_spawn = False  # It removes the food from the board
    else:
        # If the food is taken it will not remove the last body piece(raising snakes size)
        snake_body.pop()
    if food_spawn is False:  # When a food is taken it will respawn randomly
        food_position = [getRandX(), getRandY()]
    food_spawn = True  # It will set the food to True again, to keep the cycle
    # Drawing
    player_screen.fill(white)  # Set the background to white
    for position in snake_body:  # Snake representation on the screen
        pygame.draw.rect(player_screen, green, pygame.Rect(position[0], position[1], block_size, block_size))
    # Food representation on the screen
    pygame.draw.rect(player_screen, orange, pygame.Rect(food_position[0], food_position[1], block_size, block_size))
    if snake_position[0]<0 or snake_position[0]>width or snake_position[1]<0 or snake_position[1]>height:
        done = True # Game over when the Snake hit a wall
    for block in snake_body[1:]:
        if snake_position == block:
            done = True  # Game over when the Snake hits itself
    pygame.display.flip()  # It constantly updates the screen
    fps.tick(20)  # It sets the speed to a playable value

pygame.quit()
sys.exit()